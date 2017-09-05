from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth import get_user_model
from . import forms
from .forms import ContactForm, SubscribeForm
from django.shortcuts import render

User = get_user_model()

def subscribe(request):
    form_class = SubscribeForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')

            # Email the profile with the
            # contact information
            template = get_template('contact/subscribe_template.txt')
            context = dict({'contact_name': contact_name, 'contact_email': contact_email,})

            content = template.render(context)

            email = EmailMessage(
                "New subscribe form submission",
                content,
                "Your website" +'',
                ['steve@steve-shead.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return render(request, 'contact/thank_you_subscribe.html')

    return render(request, 'contact/subscribe.html', {
        'form': form_class,
    })

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact/contact_template.txt')
            context = dict({'contact_name': contact_name, 'contact_email': contact_email, 'form_content': form_content,})

            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['steve@steve-shead.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return render(request, 'contact/thank_you.html')

    return render(request, 'contact/contact.html', {
        'form': form_class,
    })
