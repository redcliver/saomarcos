from django.shortcuts import render

# Create your views here.

def servico(request):
    return render(request, 'servicos.html')