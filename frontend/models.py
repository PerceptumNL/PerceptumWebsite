from django.db import models

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
    projects = models.ManyToManyField('Project', blank=True)

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(max_length=255, blank=True)
    repository = models.URLField(max_length=255, blank=True)
    small_img = models.URLField(max_length=255)
    large_img = models.URLField(max_length=255)
    categories = models.ManyToManyField('ProjectCategory', blank=True)

    def __unicode__(self):
        return self.title

class ProjectCategory(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Project categories"
