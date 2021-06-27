from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('submit_property/', views.PropertyCreateView.as_view(), name='submit-property'),
    path('properties/', views.properties, name='properties'),
    path('property/<int:pk>', views.property, name='property-detail'),
    path('contact/', views.contact, name='contact'),
    path('pay/', views.pay, name='pay'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.SignUpView.as_view(), name = 'register'), 
    path('api/create/', views.PropertyCreateAPIView.as_view(), name='create'),
    path('delete_property/<int:pk>/', views.delete_property, name='delete'),
    path('update_property/<int:pk>/', views.PropertyUpdateView.as_view(), name='update'),
    path('search/', views.search, name='search'),
    path('pay/', views.pay, name='pay')
    
]