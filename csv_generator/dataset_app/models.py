from django.db import models

SCHEMA_TYPE_CHOICE = (
    ('Full Name', 'Full Name'),
    ('Job', 'Job'),
    ('Email', 'Email'),
    ('Company', 'Company'),
    ('Phone Number', 'Phone Number'),
    ('Address', 'Address'),
    ('Date', 'Date'),
)


class Column(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=SCHEMA_TYPE_CHOICE, default='Full Name')
    order = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name


class Schema(models.Model):
    title = models.CharField(max_length=100)
    columns = models.ManyToManyField(Column, related_name='schema_columns')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
