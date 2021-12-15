from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


# Create your views here.
def index(request):
    """
    Index Function - Basic View that returns an HTTP Response
    """
    return HttpResponse("Hello, world. You're at the B-05's index url.")


# Index Class
class IndexView(generic.ListView):
    """
    Index View - Populates the index.html on the base URL
    """

    def get(self, request, **kwargs):
        return render(request, 'index.html')


# Profile Class
class ProfileView(generic.ListView):
    """
    Profile View - Profile Screen or redirects to login form
    """

    def get(self, request, **kwargs):
        return render(request, 'registration/profile.html')
