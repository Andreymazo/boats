from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Article


class HomePageView(TemplateView):
    template_name = 'boat/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['blog'] = Article.objects.filter(is_published=True).order_by('?')[:4]
        context_data['blog'] = Article.objects.filter(is_published=True).order_by('-created_at')[:4]
        return context_data
