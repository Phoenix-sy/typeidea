from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse

from blog.views import CommonViewMinxin
from .models import Link


class LinkListView(CommonViewMinxin, ListView):
	queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
	template_name = 'config/links.html'
	context_object_name = 'link_list'
