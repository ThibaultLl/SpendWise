from django.shortcuts import render

def transactions(request):
    
    return render(request, 'transactions/transactions.html')