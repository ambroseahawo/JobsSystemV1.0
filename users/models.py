import os
from django.db import models
from django.contrib.auth.models import User
from jobs.models import Job, Industry


class Education(models.Model):
    user = models.ForeignKey(User, related_name='education', on_delete=models.CASCADE)
    school = models.CharField(max_length=120, null=False, blank=False)
    degree = models.CharField(max_length=120, null=True, blank=True)
    grade = models.CharField(max_length=2, null=True, blank=True)
    activities = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.school


class Experience(models.Model):
    user = models.ForeignKey(User, related_name='experiences', blank=False, null=False, on_delete=models.CASCADE)
    position = models.CharField(max_length=120, null=False, blank=False)
    role = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.position


class Skill(models.Model):
    user = models.ForeignKey(User, related_name='skills', blank=False, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=False, blank=False)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Account(models.Model):
    user = models.OneToOneField(User, related_name='account', null=False, blank=False, on_delete=models.CASCADE)
    dp = models.ImageField(null=True, blank=True, upload_to='users/accounts/media')
    headline = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=120, null=True, blank=True)
    interests = models.ManyToManyField(Industry, blank=True, related_name='industry')
    hobbies = models.TextField(null=True, blank=True)
    summary = models.CharField(max_length=120, null=True, blank=True)
    jobs = models.ManyToManyField(Job, blank=True, related_name='account_jobs')
    address_line_1 = models.CharField(max_length=120, blank=True, null=True)
    address_line_2 = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    postal_code = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Media(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, related_name='media', on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True, upload_to='users/accounts/media')

    def __str__(self):
        return os.path.basename(self.file.name)

    def filename(self):
        return os.path.basename(self.file.name)

