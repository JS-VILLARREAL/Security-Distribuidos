from django.db import models
from corhuila.models import BaseModel
from django.contrib.auth.models import User

# Create your models here.
class Person(BaseModel):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=30)
    state = models.BooleanField(default=True)

    class Meta:
        db_table = 'person'
        ordering = ['first_name']

    def __str__(self):
        return self.first_name

class User(BaseModel):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    state = models.BooleanField(default=True)

    class Meta:
        db_table = 'user'
        ordering = ['username']

    def __str__(self):
        return self.username

class Role(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    state = models.BooleanField(default=True)

    class Meta:
        db_table = 'role'
        ordering = ['name']

    def __str__(self):
        return self.name

## create table pivot person and user
class UserRole(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'user_role'
        ordering = ['user']

    def __str__(self):
        return self.user

class Module(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    route = models.CharField(max_length=50, default='route')
    state = models.BooleanField(default=True)

    class Meta:
        db_table = 'module'
        ordering = ['name']

    def __str__(self):
        return self.name

class ModuleRole(BaseModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'module_role'
        ordering = ['module']

    def __str__(self):
        return self.module

class View(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    route = models.CharField(max_length=50, default='route')
    state = models.BooleanField(default=True)

    class Meta:
        db_table = 'view'
        ordering = ['name']

    def __str__(self):
        return self.name

class ViewModule(BaseModel):
    view = models.ForeignKey(View, on_delete=models.CASCADE, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'view_module'
        ordering = ['view']

    def __str__(self):
        return self.view