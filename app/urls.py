from django.urls import path

from . import views
urlpatterns = [
    path('total-rides', views.TaxiTripView.as_view())


]