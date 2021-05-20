from django.db import models


class User(models.Model):
    """
    User Model
    Defines the attributes of a user
    """
    name = models.CharField(max_length=228)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"{self.name} - {self.age} years old"
