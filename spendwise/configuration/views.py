from django.shortcuts import render

def configuration(request):
    
    return render(request, 'configuration/configuration.html')