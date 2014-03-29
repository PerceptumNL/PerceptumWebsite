from django.db import models
from polymorphic import PolymorphicModel

class Interface(PolymorphicModel):
    page_title = models.CharField(max_length=255)
    page_description = models.CharField(max_length=255)
    page_icon = models.URLField(max_length=255, blank=True)
    active = models.BooleanField()
    datetime = models.DateTimeField(auto_now=True, editable=False)
    template = models.CharField(max_length=255, editable=False,
            default="index.html")

    def get_absolute_url(self):
        return "/?interface=%d" % (self.pk,)

class TrebleInterface(Interface):
    show_social = models.BooleanField(
            verbose_name="Show the social networks of the organisation")
    member_project_filter = models.BooleanField(default=True,
            verbose_name="Allow projects to be filtered by members")
    scrolldown_visual = models.URLField(max_length=255)
    scrolldown_flipped_visual = models.URLField(max_length=255)
    description_title = models.CharField(max_length=255)
    members_title = models.CharField(max_length=100,
            verbose_name="Section title for members")
    members_intro = models.TextField()
    work_title = models.CharField(max_length=100,
            verbose_name="Section title for work")
    work_intro = models.TextField()
    contact_title = models.CharField(max_length=100,
            verbose_name="Section title for contact")
    contact_intro = models.TextField()
    ganalytics_id = models.CharField(max_length=100,
        verbose_name="Google Analytics ID")


    def __init__(self, *args, **kwargs):
        kwargs['template'] = "index.html"
        super(TrebleInterface, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return "Treble interface"
