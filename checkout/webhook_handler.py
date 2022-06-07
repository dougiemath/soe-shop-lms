from django.http import HttpResponse

from .models import Order, OrderLineItem
from courses.models import Course
from profiles.models import UserProfile

import json
import time

class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """handles generic webhook events"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handles the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            username = intent.metadata.username
            for item_id, item_data in json.loads(bag).items():
                print(item_id, '1st try')
                username = intent.metadata.username
                course = Course.objects.get(id=item_id)
                print(course)
                user = UserProfile.objects.get(user__username=username)
                print(user)
                print(user.course_bought)
                user.course_bought.add(course)
                user.save()
                print(user.course_bought)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    name=billing_details.name,
                    email=billing_details.email,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    print(item_id, '2nd try')
                    username = intent.metadata.username
                    course = Course.objects.get(id=item_id)
                    print(course)
                    user = UserProfile.objects.get(user__username=username)
                    print(user)
                    # user.course_bought.add(course)
                    user.save()
                    print(user.course_bought)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            course=course,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """handles the payment_intent.payment_failed webhook from Stripe"""
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )
