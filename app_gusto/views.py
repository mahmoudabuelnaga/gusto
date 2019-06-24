from django.shortcuts import render, redirect
from .models import Special,Menu
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def gusto(request):
    specials    = Special.objects.filter(view=True)[:3]
    menu_bs     = Menu.objects.filter(menu_section_title='BS')
    menu_mc     = Menu.objects.filter(menu_section_title='MC')
    menu_di     = Menu.objects.filter(menu_section_title='Di')
    menu_de     = Menu.objects.filter(menu_section_title='De')
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name       = form.cleaned_data['name']
            email      = form.cleaned_data['email']
            message    = form.cleaned_data['message']
            try:
                send_mail(name+" - "+email,message,email,['worldofbooks1751998@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('gusto')
    else:
        form = ContactForm()
    context = {
        'form'    : form,
        'specials':specials,
        'menu_bs' :menu_bs,
        'menu_mc' :menu_mc,
        'menu_di' :menu_di,
        'menu_de' :menu_de,   
    }
    return render(request, 'index.html',context)