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


class Schema(models.Model):
    title = models.CharField(max_length=100, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Column(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=SCHEMA_TYPE_CHOICE, default='Full Name')
    order = models.PositiveIntegerField(default=1)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='column_schema')

    def __str__(self):
        return self.name
