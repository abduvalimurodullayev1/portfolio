from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView

from app.models import Blog, Portfolio, Contact
from app.serializers import BlogSerializer, PortfolioSerializer, ContactSerializer


class BlogView(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class PortfolioView(ListAPIView):
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


