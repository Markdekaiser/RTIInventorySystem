from main.views import customer
from django import template

register = template.Library()

from ..models import Requesition

@register.filter
def calc(id):
    req = Requesition.objects.get(id=id)
    total = req.Item.price * req.Qty
    return total

@register.filter
def pending(id):
    req = Requesition.objects.filter(customer_id=id,status='A')
    count = req.count()
    return count

@register.filter
def accepted(id):
    req = Requesition.objects.filter(customer_id=id,status='B')
    count = req.count()
    return count

@register.filter
def partial(id):
    req = Requesition.objects.filter(customer_id=id,status='C')
    count = req.count()
    return count

@register.filter
def delivered(id):
    req = Requesition.objects.filter(customer_id=id,status='D')
    count = req.count()
    return count

@register.filter
def checkStorage(id):
    req = Requesition.objects.get(id= id)
    num = req.Item.stock_quantity - req.Qty
    if num <= 0:
        return False
    else:
        return True