# encoding: utf-8

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import admin
from data import get_ingredients, get_cocktails

admin.autodiscover()

def ingredients(request):
    return render(request, "ingredients.haml", {"ingredients": get_ingredients(request.GET.get("filtering_string", []))})

def cocktails(request):
    print request.GET.keys()
    cocktails = get_cocktails(request.GET.keys())
    if cocktails:
        return render(request, "cocktails.haml", {"cocktails": cocktails})
    else:
        return HttpResponse(u"<p>Aucun cocktails ne peut être fait avec ces ingrédients</p>")

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^ingredients/$', ingredients, name='ingredients'),
    url(r'^cocktails/$', cocktails, name='cocktails'),
    # url(r'^cocktails/', include('cocktails.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
