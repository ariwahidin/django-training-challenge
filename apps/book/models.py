import uuid
from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=50)

    def __str__(self):
        return self.author
