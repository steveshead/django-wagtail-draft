from django.views import generic
from contact.forms import ContactForm


class HomePage(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args, **kwargs):
        context=super(HomePage, self).get_context_data(*args, **kwargs)
        context['form'] = ContactForm

        return context

class AboutPage(generic.TemplateView):
    template_name = "about.html"
