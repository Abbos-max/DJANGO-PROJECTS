from django.urls import path
from .views import IndexView, ContactView, WhyView, TrainerView, SuccessView
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path("", IndexView.as_view(), name='index_url'),
    path("contact/", ContactView.as_view(), name='contact_url'),
    path("trainer/", TrainerView.as_view(), name='trainer_url'),
    path("why/", WhyView.as_view(), name='why_url'),
    path("success/", SuccessView.as_view(), name = 'success_url'),
]