import time

from django.conf import settings

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from celery import shared_task
from main.models import Contact
from .models import Recipe

# @shared_task
# def send_mail_to_subscribers():
#     email_list = Contact.objects.values_list('email', flat=True)
#     recipes = Recipe.objects.all()

#     message = render_to_string('blog/email_subscribers.html', {
#                 'recipes': recipes
#             })
#     subject = 'New blog from out website'
#     mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
#     mail.content_subtype = 'html'
#     mail.send()
    
@shared_task
def send_message():
    print("hello f")
    print("hello fa")
    print("hello far")
    print("hello fari")
    print("hello fariz")