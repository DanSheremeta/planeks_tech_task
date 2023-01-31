from django.contrib import messages
from django.shortcuts import render, redirect
from . import models, forms
from django.http import HttpResponseRedirect


def schemas_list(request):
    context = {
        'schemas': enumerate(models.Schema.objects.all(), start=1)
    }
    return render(request, 'dataset/schemas.html', context)


def schema_create(request):
    if request.method == 'POST':
        form = forms.SchemaForm(request.POST)
        if form.is_valid():
            form.save()
            form_id = models.Schema.objects.get(title=form["title"].value()).id
            return HttpResponseRedirect(f'/schemas/{form_id}/create-column/')
    else:
        form = forms.SchemaForm()

    return render(request, 'dataset/schema_form.html', {'form': form})


def schema_delete(request, pk):
    schema = models.Schema.objects.get(id=pk)
    schema.delete()
    return redirect('schemas-list')


def schema_column_create(request, pk):
    schema = models.Schema.objects.get(id=pk)
    columns_orders = [x.order for x in models.Column.objects.all().filter(schema__id=pk)]

    if request.method == 'POST':
        form = forms.ColumnForm(request.POST)
        if form.is_valid():
            order = int(form['order'].value())

            if order in columns_orders or order < 1:
                messages.success(request, 'Incorrect order')
                return HttpResponseRedirect(f'/schemas/{pk}/create-column/')

            column = models.Column(
                name=form['name'].value(), type=form['type'].value(),
                order=form['order'].value(), schema=schema
            )
            column.save()
            return HttpResponseRedirect(f'/schemas/{pk}/create-column/')
    else:
        form = forms.ColumnForm()

    columns = models.Column.objects.all().filter(schema__id=pk)

    return render(request, 'dataset/column_form.html', {'form': form, 'columns': columns, 'schema': schema})





def column_delete(request, pk):
    column = models.Column.objects.get(id=pk)
    schema_id = column.schema.id
    column.delete()
    return HttpResponseRedirect(f'/schemas/{schema_id}/create-column/')


def dataset_list(request, pk):
    columns = models.Column.objects.all().filter(schema__id=pk)

    return render(request, 'dataset/datasets.html', {'columns': columns})
