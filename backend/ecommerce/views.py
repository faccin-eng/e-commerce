from django.shortcuts import render

# Create your views here.
def home(request):
    return render(
        request,
        'ecommerce/home.html',
        )

def about(request):
    return render(
        request, 'ecommerce/about.html'
    )

def perfil(request):
    return render(
        request, 'ecommerce/perfil.html'
    )