from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('submit_property/', views.PropertyCreateView.as_view(), name='submit-property'),
    path('properties/', views.properties, name='properties'),
    path('property/<int:pk>', views.property, name='property-detail'),
    path('contact/', views.contact, name='contact'),
    path('pay/<int:pk>', views.pay, name='pay'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('register/', views.SignUpView.as_view(), name = 'register'), 
    path('api/create/', views.PropertyCreateAPIView.as_view(), name='create'),
    path('delete_property/<int:pk>/', views.delete_property, name='delete'),
    path('update_property/<int:pk>/', views.PropertyUpdateView.as_view(), name='update'),
    path('search/', views.search, name='search'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('confirm/<int:pk>/', views.confirm, name='confirm')  ,
    path('approve-transaction/<int:pk>', views.approve_transaction_view,name='approve-transaction'),
    path('reject-transaction/<int:pk>', views.disapprove_transaction_view,name='reject-transaction'),  
    path('admin_properties/', views.admin_properties, name='admin_properties'),
    path('admin_transactions/', views.admin_transactions, name='admin_transactions'),
]