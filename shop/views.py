import stripe
import requests
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Configure Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def shop(request):
    return render(request, 'shop/shop.html')

def create_checkout_session(request):
    if request.method == 'POST':
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'VIP Membership',
                        },
                        'unit_amount': 100,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://127.0.0.1:8000/shop/success/',
                cancel_url='http://127.0.0.1:8000/shop/cancel/',
            )
            return JsonResponse({'id': session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)})

def email_payment(request):
    if request.method == 'POST':
        membership_type = request.POST.get('membership_type')
        user_email = request.user.email if request.user.is_authenticated else 'anonymous@example.com'
        
        # Send email to the site owner with payment details
        send_mail(
            'New VIP Membership Payment',
            f'User {user_email} has requested the {membership_type} membership.',
            'noreply@kingsrevolution.com',
            ['chkingsimba1@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'shop/success.html')
    return redirect('shop')

def payment_success(request):
    return render(request, 'shop/success.html')

def payment_cancel(request):
    return render(request, 'shop/cancel.html')
