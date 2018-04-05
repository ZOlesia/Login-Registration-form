# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class BlogManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors['first_name'] = "First name should be more than 2 characters and letters only"
        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            errors['last_name'] = "Last name should be more than 2 characters and letters only"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email1'] = "Not valid email"
        if len(User.objects.filter(email = postData['email'])) > 0:
            errors['email2'] = "Email already exists"
        if len(postData['password']) < 8:
            errors['password'] = "Passwords must be at least 8 characters in length"
        if postData['confirm'] != postData['password']:
            errors['confirm'] = "Password doesn`t match"
        return errors

    def login_validator(self, postData):
        errors = {}
        # hash1 = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        if len(postData['email']) < 1:
            errors['log_email1'] = 'Email field is empty'
        if len(User.objects.filter(email = postData['email'])) == 0 :
            errors['log_email2'] = 'Please check your email otherwie go to register'
        # if bcrypt.checkpw(postData['password'].encode(), hash1.encode()):
        #     errors['log_password'] = "Password doesn`t match"
        if len(User.objects.filter(password = postData['password'])) == 0 :
            errors['log_email2'] = 'Password is incorrect'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    conf_password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()