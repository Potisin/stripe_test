from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
import stripe
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from general.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def create_payment(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    payment_intent = stripe.PaymentIntent.create(
        amount=int(item.price),
        currency='usd'
    )
    return JsonResponse({'client_secret': payment_intent.client_secret})


def get_item_page(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'item': item,
        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'item.html', context)


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')
