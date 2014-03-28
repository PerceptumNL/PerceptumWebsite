from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def page(request, page):
    template = "pages/%s" % (page,)
    return render(request, template, {})
