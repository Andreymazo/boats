from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView

from blog.models import Article
from boat.models import Boat, Like


class HomePageView(TemplateView):
    template_name = 'boat/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['blog'] = Article.objects.filter(is_published=True).order_by('?')[:4]
        context_data['blog'] = Article.objects.filter(is_published=True).order_by('-created_at')[:2]
        context_data['boats'] = Boat.objects.all()[:3]
        return context_data


class BoatDetail(DetailView):
    model = Boat

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['has_like'] = False
        if self.request.user.is_authenticated:
            context_data['has_like'] = self.object.like_set.filter(user=self.request.user).exists()
        return context_data


def make_like_toggle(request, pk):
    boat_item = get_object_or_404(Boat, pk=pk)
    existing_like_for_user = boat_item.like_set.filter(user=request.user)
    if existing_like_for_user.exists():
        existing_like_for_user.delete()
    else:
        Like.objects.create(
            user=request.user,
            boat=boat_item
        )

    return redirect(request.META.get('HTTP_REFERER'))
