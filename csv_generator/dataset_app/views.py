from django.shortcuts import render
from . import models


def schemas_list(request):
    context = {
        'schemas': models.Schema.objects.all()
    }
    return render(request, 'dataset/schemas.html', context)
