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
from django.shortcuts import render

def my_view(request):
    context = {
        'heading1': 'No.1',
        'content1': 'Coffee chain in Africa',
        'heading2': '300+',
        'content2': 'Shops Across Africa',
        'heading3': '20+',
        'content3': 'Years of life and coffee',
    }
    return render(request, 'example_template.html', context)
