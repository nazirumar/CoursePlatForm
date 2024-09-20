import helpers
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

helpers.cloudinary_init()

class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED ='email_required', "Email required"

class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "drf", "Draft"


def handle_upload(instance, filename):
    return f"courses/{filename}"

class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to=handle_upload, blank=True,  null=True)
    image = CloudinaryField('image', null=True)
    access = models.CharField(max_length=20, choices=AccessRequirement, default=AccessRequirement.EMAIL_REQUIRED)
    status = models.CharField(max_length=10,
                              choices=PublishStatus.choices,
                              default=PublishStatus.DRAFT)