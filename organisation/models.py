from django.db import models

class Organisation(models.Model):
    name = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255, blank=True)
    tagline = models.CharField(max_length=255)
    logo = models.URLField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255)
    timezone = models.CharField(max_length=100, blank=True)
    facebook = models.URLField(max_length=255, blank=True)
    twitter = models.URLField(max_length=255, blank=True)
    linkedin = models.URLField(max_length=255, blank=True)
    youtube = models.URLField(max_length=255, blank=True)
    pinterest = models.URLField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    description = models.TextField()
    img = models.URLField(max_length=255)
    facebook = models.URLField(max_length=255, blank=True)
    twitter = models.URLField(max_length=255, blank=True)
    linkedin = models.URLField(max_length=255, blank=True)
    youtube = models.URLField(max_length=255, blank=True)
    pinterest = models.URLField(max_length=255, blank=True)
    projects = models.ManyToManyField('Project', blank=True,
        related_name='members')

    def __unicode__(self):
        return self.name

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(max_length=255, blank=True)
    repository = models.URLField(max_length=255, blank=True)
    small_img = models.URLField(max_length=255, verbose_name="Thumbnail image")
    large_img = models.URLField(max_length=255, verbose_name="Large image")
    categories = models.ManyToManyField('ProjectCategory', blank=True)

    def __unicode__(self):
        return self.title

class ProjectCategory(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Project categories"
