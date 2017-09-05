from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from crispy_forms.layout import Submit

class SubscribeForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('contact_name', placeholder="Full Name", autofocus=""),
            Field('contact_email', placeholder="Email Address"),
            Submit('sign_in', 'Subscribe', css_class="btn btn-primary"),
            )
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('contact_name', placeholder="Full Name", autofocus=""),
            Field('contact_email', placeholder="Email Address"),
            Field('content', placeholder=""),
            Submit('sign_in', 'Submit', css_class="btn btn-primary"),
            )
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "Your message:"
