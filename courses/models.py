from django.db import models

# Create your models here.



class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED ='email_required', "Email required"
    DRAFT = "draft", "Draft"

class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "drf", "Draft"


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='')
    access = models.CharField(max_length=20, choices=AccessRequirement, default=AccessRequirement.DRAFT)
    status = models.CharField(max_length=10,
                              choices=PublishStatus.choices,
                              default=PublishStatus.DRAFT)