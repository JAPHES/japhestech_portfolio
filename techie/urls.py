from django.urls import path

from . import views

app_name = 'techie'

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio-details/', views.portfolio_details, name='portfolio_details'),
    path('service-details/', views.service_details, name='service_details'),
    path('starter-page/', views.starter_page, name='starter_page'),
]
