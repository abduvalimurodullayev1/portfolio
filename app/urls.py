from django.urls import path
from .views import ContactCreateView, BlogView, PortfolioView

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),  # Add .as_view() here
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),  # Add .as_view() here
    # Other URL patterns...
]
