from django.shortcuts import render
from django.http import Http404
from organisation.models import *
from frontend.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        "interface": Interface.objects.filter(active=True)[0],
        "organisation": Organisation.objects.all()[0],
        "members": Member.objects,
        "projects": Project.objects,
        "project_categories": ProjectCategory.objects
    })

def project(request, item):
    try:
        project = Project.objects.get(pk=item)
    except:
        raise Http404
    else:
        return render(request, 'project.html', {"item": project})

def page(request, page):
    template = "pages/%s" % (page,)
    return render(request, template, {})
