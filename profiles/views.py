from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post


def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

 
@login_required
def posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {'posts': posts}
    template = 'posts.html'
    return render(request, template, context)


def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)


def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['name']
        subject = 'MESSAGE FROM MY DJANGO SITE'
        comment = form.cleaned_data['comment']
        message = '%s \n Name - %s \n From - %s' % (comment, name, form.cleaned_data['email'])
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = "Thanks!"
        confirm_message = "Thanks for your message. We will get right back to you SOON"
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message, }

    #    context = locals()
    template = 'contact.html'
    return render(request, template, context)


def team(request):
    context = locals()
    template = 'team.html'
    return render(request, template, context)


@login_required
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'account/profile.html'
    return render(request, template, context)
