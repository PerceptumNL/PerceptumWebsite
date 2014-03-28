from django.db import models

# Create your models here.
class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField(max_length=255, blank=True)
    repository = models.URLField(max_length=255, blank=True)
    small_img = models.URLField(max_length=255)
    large_img = models.URLField(max_length=255)
    categories = models.ManyToManyField('PortfolioCategory', blank=True)

    def __unicode__(self):
        return self.title

class PortfolioCategory(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Portfolio categories"
