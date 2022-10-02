from email.policy import default
from django.db import models
from django.forms import ValidationError


class Job(models.Model):

    TYPE_CHOICES = [("FT", "Full-time"), ("PT", "Part-time"), ("IP", "Internship"), ("CO", "Contract")]

    job_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    active = models.BooleanField()
    description = models.TextField()
    location = models.CharField(max_length=150)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title + ' - ' + self.company + ', ' + self.location

    def clean(self):
        s1 = self.min_salary
        s2 = self.max_salary
        if s1 is not None and s2 is not None and s1 > s2:
            raise ValidationError('Min salary should be less than or equal to Max Salary')
        super().clean()

class Application(models.Model):

    DEFAULT_STATUS = "AS"
    STATUS_CHOICES = [("UC", "Under Consideration"), ("AS", "Application Submitted"), ("AR", "Application Rejected"), ("PA", "Pending Action"), ("AW", "Application Withdrawn")]

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=DEFAULT_STATUS)
    applied_on = models.DateField(auto_now_add=True)  
    
    def __str__(self):
        return self.job.title + ' - ' + str(self.id)

