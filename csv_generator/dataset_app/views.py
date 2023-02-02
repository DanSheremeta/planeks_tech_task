import csv

from faker import Faker
from faker.providers import internet, phone_number, company, job

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse, FileResponse
from django.views import View

from . import models, forms


class SchemaListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dataset/schemas.html', {'schemas': models.Schema.objects.all()})


def schema_delete(request, pk):
    if request.user.is_authenticated:
        schema = models.Schema.objects.get(id=pk)
        schema.delete()
        return redirect('schemas-list')
    else:
        messages.success(request, 'This is forbidden for anonymous users!')
        return redirect('schemas-list')


def schema_create(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            schema_form = forms.SchemaForm()
            column_form = forms.ColumnForm()
            return render(request, 'dataset/schema_create.html', {'schema_form': schema_form, 'column_form': column_form})
        if request.method == 'POST':
            if not request.POST['title']:
                messages.success(request, 'Enter schema\'s name')
                return redirect('schema-create')
            schema = models.Schema(title=request.POST['title'])
            schema.save()

            if ('name' and 'type' and 'order') in request.POST.keys():
                column = models.Column(name=request.POST['name'], type=request.POST['type'],
                                       order=request.POST['order'], schema=schema)
                column.save()
            return redirect('schema-update', schema.id)
    else:
        messages.success(request, 'This is forbidden for anonymous users!')
        return redirect('schemas-list')


def schema_update(request, pk):
    if request.user.is_authenticated:
        schema = models.Schema.objects.get(id=pk)
        columns = models.Column.objects.all().filter(schema__id=pk)
        if request.method == 'POST':
            if 'title' in request.POST.keys():
                schema.title = request.POST['title']
                schema.save()

            if ('name' and 'type' and 'order') in request.POST.keys():
                order = int(request.POST['order'])
                columns_orders = [x.order for x in models.Column.objects.all().filter(schema__id=pk)]

                if order in columns_orders or order < 1:
                    messages.success(request, 'Incorrect order')
                    return redirect('schema-update', pk)

                column = models.Column(name=request.POST['name'], type=request.POST['type'],
                                       order=request.POST['order'], schema=schema)
                column.save()
            return redirect('schema-update', pk)
        else:
            schema_form = forms.SchemaForm(instance=schema)
            column_form = forms.ColumnForm()

            return render(request, 'dataset/schema_update.html',
                          {'schema_form': schema_form, 'columns': columns,
                           'column_form': column_form})
    else:
        messages.success(request, 'This is forbidden for anonymous users!')
        return redirect('schemas-list')


def column_delete(request, pk):
    if request.user.is_authenticated:
        column = models.Column.objects.get(id=pk)
        schema_id = column.schema.id
        column.delete()
        return redirect('schema-update', schema_id)
    else:
        messages.success(request, 'This is forbidden for anonymous users!')
        return redirect('schema-update', pk)


def fake_data(data):
    fake = Faker()
    fake.add_provider(internet)
    fake.add_provider(phone_number)
    fake.add_provider(company)
    fake.add_provider(job)

    if data == 'Full Name':
        return fake.name()
    elif data == 'Job':
        return fake.job()
    elif data == 'Email':
        return fake.email()
    elif data == 'Domain Name':
        return fake.domain_name()
    elif data == 'Phone Number':
        return fake.phone_number()
    elif data == 'Company Name':
        return fake.company()
    elif data == 'Text':
        return fake.text()
    elif data == 'Integer':
        return fake.pyint(min_value=0, max_value=100)
    elif data == 'Address':
        return fake.address()
    elif data == 'Date':
        return fake.date()


def generate_csv(request, pk):
    if request.method == 'POST':
        columns = models.Column.objects.all().filter(schema__id=pk)

        names = [None for _ in columns]
        types = [None for _ in columns]
        for column in columns:
            names[int(column.order) - 1] = column.name
            types[int(column.order) - 1] = column.type

        form = forms.DataSetForm(request.POST)
        fake = Faker()

        if form.is_valid():
            rows = int(form['rows'].value())
            schema = models.Schema.objects.get(id=pk)
            file_name = f'{schema.title}{fake.pyint()}.csv'
            file = open(f'media/{file_name}', mode='w', newline='')
            dataset = models.DataSet(schema=schema, csv_file=f'{file_name}')
            dataset.save()

            file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(names)

            for _ in range(rows):
                data = []
                for i in types:
                    data.append(fake_data(i))
                file_writer.writerow(data)

            file.close()

            dataset.status = True
            dataset.save()
            return JsonResponse({}, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)

    return JsonResponse({'error': ''}, status=400)


def dataset_list(request, pk):
    columns = models.Column.objects.all().filter(schema__id=pk)
    datasets = models.DataSet.objects.all().filter(schema__id=pk)
    return render(request, 'dataset/datasets.html', {'datasets': datasets, 'columns': columns})


def download_csv(request, pk):
    file_name = models.DataSet.objects.get(id=pk).csv_file
    return FileResponse(open(f'media/{file_name}', 'rb'), as_attachment=True)
