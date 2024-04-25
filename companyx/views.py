from django.views.generic import TemplateView

class LandingPage(TemplateView):
    template_name = 'landing_page.html'

class ReEntryPage(TemplateView):
    template_name = 're-entry_page.html'


class HomePage(TemplateView):
    template_name = 'index.html'