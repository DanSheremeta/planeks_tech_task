from django.conf import settings
from django.db import models

SCHEMA_TYPE_CHOICE = (
    ('Full Name', 'Full Name'),
    ('Job', 'Job'),
    ('Email', 'Email'),
    ('Domain Name', 'Domain Name'),
    ('Phone Number', 'Phone Number'),
    ('Company Name', 'Company Name'),
    ('Text', 'Text'),
    ('Integer', 'Integer'),
    ('Address', 'Address'),
    ('Date', 'Date'),
)


class Schema(models.Model):
    title = models.CharField(max_length=100, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title


class Column(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=SCHEMA_TYPE_CHOICE, default='Full Name')
    order = models.PositiveIntegerField(default=1)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='column_schema')

    def __str__(self):
        return self.name


class DataSet(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    csv_file = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, editable=False)
