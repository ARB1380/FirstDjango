from django import forms
from captcha.fields import CaptchaField
from website.models import Contact, NewsLetter


class NameForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):

    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'


class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields = '__all__'



