from django.shortcuts import render
from django.views.generic.base import View

from .models import Author


# Create your views here.




class AuthorViews(View):
    def get(self, request):
        author = Author.objects.all()
        return render(request, "author/author_list.html")


def AuthorView(request):
    return None