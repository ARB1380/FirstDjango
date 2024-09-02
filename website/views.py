from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django import forms
from django.contrib import messages
from website.forms import ContactForm, NewsLetterForm


def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contacts_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.instance.name = 'Unknown'
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submitted successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket didnt submitted!')

    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submitted successfully!')
            return HttpResponseRedirect('/')

    else:
        messages.add_message(request, messages.ERROR, 'your ticket didnt submitted!')
        return HttpResponseRedirect('/')


