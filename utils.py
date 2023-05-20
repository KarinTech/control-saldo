from .models import Transaction

def calculate_balance():
    received_transactions = Transaction.objects.filter(is_received=True)
    sent_transactions = Transaction.objects.filter(is_received=False)

    total_received = sum(t.amount for t in received_transactions)
    total_sent = sum(t.amount for t in sent_transactions)

    balance = total_received - total_sent

    return balance
