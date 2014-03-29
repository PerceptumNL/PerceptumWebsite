from django.shortcuts import render
from django.http import Http404
from organisation.models import *
from frontend.models import *

# Create your views here.
def index(request):
    interface_id = request.GET.get("interface", None)
    if interface_id is None:
        interface = Interface.objects.filter(active=True)[0]
    else:
        try:
            interface = Interface.objects.get(pk=interface_id)
        except:
            raise Http404
    return render(request, interface.template, {
        "interface": interface,
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
