from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('email-payment/', views.email_payment, name='email_payment'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
]
