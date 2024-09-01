from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


