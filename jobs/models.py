from django.db import models


class Industry(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return self.title


class Job(models.Model):
    position = models.CharField(max_length=120, null=False, blank=False)
    company = models.CharField(max_length=200, null=False, blank=False)
    company_logo = models.ImageField(null=True, blank=True, upload_to='jobs/companies/logos')
    requirements = models.TextField(null=False, blank=False)
    industries = models.ManyToManyField(Industry, related_name='job_fields')
    email = models.EmailField(null=False, blank=False)
    about = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.position
