from django.shortcuts import render


def home(request):
    return render(request, 'techie/index.html')


def portfolio_details(request):
    return render(request, 'techie/portfolio-details.html')


def service_details(request):
    return render(request, 'techie/service-details.html')


def starter_page(request):
    return render(request, 'techie/starter-page.html')
