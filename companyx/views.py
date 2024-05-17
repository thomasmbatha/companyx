from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class LandingPage(TemplateView):
    template_name = 'landing_page.html'

class ReEntry(TemplateView):
    template_name = 're-entry_page.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("re-entry_page"))
        return super().get(request, *args, **kwargs)