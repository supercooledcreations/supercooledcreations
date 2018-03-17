# Import #
# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.utils import timezone

# App
from .forms import BookmarkForm
from .models import Bookmark


# Views #
# Metrics #
class HomeView(LoginRequiredMixin, View):

    # List, Add
    def get(self, request, *args, **kwargs):

        template_name = 'scc_home/home.html'

        bookmark_list = Bookmark.objects.filter(user=request.user)

        bookmark_form = BookmarkForm

        context = {'bookmark_list': bookmark_list,
                   'bookmark_form': bookmark_form}

        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):

        form = BookmarkForm(request.POST)
        form.instance.user = request.user

        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('scc_home:home'))