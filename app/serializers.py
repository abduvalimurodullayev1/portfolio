from rest_framework import serializers

from app.models import Blog, Portfolio, Contact


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ()


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        exclude = ()


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ()