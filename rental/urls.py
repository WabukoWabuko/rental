# rental/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('property/<int:property_id>/book/', views.book_property, name='book_property'),
    path('property/<int:property_id>/pay/', views.pay_rent, name='pay_rent'),
    path('property/<int:property_id>/complaint/', views.submit_complaint, name='submit_complaint'),
    path('property/<int:property_id>/chat/', views.chat, name='chat'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('properties/', views.properties_list, name='properties'),
    path('contact/', views.contact, name='contact'), 
]
