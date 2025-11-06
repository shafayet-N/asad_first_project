from django.shortcuts import render

def home(request):
    """Home page"""
    return render(request, 'home.html')

def services(request):
    """Services page"""
    return render(request, 'services.html')

def enterprise_domain(request):
    """Enterprise/Expertise Domains page"""
    return render(request, 'enterprise-Domain.html')

def pricing(request):
    """Pricing page"""
    return render(request, 'pricing.html')

def for_writers(request):
    """For Writers page"""
    return render(request, 'for_writers.html')

def client_dashboard(request):
    """Client Dashboard page"""
    return render(request, 'client-dashboard.html')

def writer_dashboard(request):
    """Writer Dashboard page"""
    return render(request, 'writer-dashboard.html')

def admin_dashboard(request):
    """Admin Dashboard page"""
    return render(request, 'admin-dashboard.html')

def order_content(request):
    """Order Content page"""
    return render(request, 'order_content.html')
