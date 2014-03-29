from django.shortcuts import render
from django.http import Http404
from organisation.models import *
from frontend.models import *

# Create your views here.
def index(request):
    interface_id = request.GET.get("interface", None)
    if interface_id is None:
        try:
            interface = Interface.objects.filter(active=True)[0]
        except:
            raise Http404
    else:
        try:
            interface = Interface.objects.get(pk=interface_id)
        except:
            raise Http404
    organisation_id = request.GET.get("organisation", None)
    if organisation_id is None:
        try:
            organisation = Organisation.objects.all()[0]
        except:
            raise Http404
    else:
        try:
            organisation = Organisation.objects.get(pk=organisation_id)
        except:
            raise Http404
    return render(request, interface.template, {
        "interface": interface,
        "organisation": organisation,
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
