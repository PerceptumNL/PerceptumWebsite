from django.shortcuts import render
from django.http import Http404
from frontend.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        "portfolio_items": PortfolioItem.objects,
        "portfolio_categories": PortfolioCategory.objects
    })

def portfolio(request, item):
    try:
        portfolio = PortfolioItem.objects.get(pk=item)
    except:
        raise Http404
    else:
        return render(request, 'portfolio.html', {"item": portfolio})

def page(request, page):
    template = "pages/%s" % (page,)
    return render(request, template, {})
