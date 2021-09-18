import uuid
from django.db import models

# Create your models here.
# models.py


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        abstract = True  # Set this model as Abstract


class Person(BaseModel):
    """A person who uses the website"""
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Thread(BaseModel):
    """A forum comment thread"""
    title = models.CharField(max_length=128)
    creator = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    """A comment by a user on a thread"""
    body = models.CharField(max_length=128)
    poster = models.ForeignKey('Person', on_delete=models.CASCADE)
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)

    def __str__(self):
        return self.body


class Club(BaseModel):
    """A group of users interested in the same thing"""
    name = models.CharField(max_length=128)
    member = models.ManyToManyField('Person')

    def __str__(self):
        return self.name
