from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class AboutPage(TemplateView):
    template_name = 'about.html'

class ContactPage(TemplateView):
    template_name = 'contacts.html'

class ProductsPage(TemplateView):
    template_name = 'products.html'

class TestimonialsPage(TemplateView):
    template_name = 'testimonials.html'
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

