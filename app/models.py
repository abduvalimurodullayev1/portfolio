from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q


class Blog(models.Model):
    title = models.CharField(max_length=122)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=155)


class Contact(models.Model):
    name = models.CharField(max_length=122)
    subject = models.TextField(max_length=122)
    message = models.TextField(max_length=155)
    email = models.EmailField(max_length=155)


class Portfolio(models.Model):
    title = models.CharField(max_length=112)
    image = models.ImageField(upload_to='portfolio/')


@receiver(post_save, sender=Contact)
def send_contact_email(sender, instance, **kwargs):
    subject = 'Yangi kontakt: {}'.format(instance.name)
    message = 'Email: {}\n\n{}'.format(instance.email, instance.message)
    from_email = 'murodullayevabduvali972@gmail.com'  # O'zgarmas elektron pochta manzilingiz
    recipient_list = ['murodullayevabduvali972@gmail.com']  # O'zgarmas administrator pochta manzilingiz
    send_mail(subject, message, from_email, recipient_list)
