from django.http import HttpResponse
from .utils import calculate_balance

def show_balance(request):
    balance = calculate_balance()
    return HttpResponse(f"El saldo actual es: {balance}")
