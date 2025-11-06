from django.contrib import admin
from django.urls import path
from django.shortcuts import render

# Simple reusable view
def page(request, name="Home"):
    return render(request, f"{name}.html")

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Homepage → Home.html
    path('', lambda r: render(r, 'home.html'), name="home"),

    # ✅ Your pages
    path('login/', lambda r: render(r, 'Login.html'), name="login"),
    path('register/', lambda r: render(r, 'Register.html'), name="register"),
    path('pricing/', lambda r: render(r, 'Pricing.html'), name="pricing"),
    path('services/', lambda r: render(r, 'Services.html'), name="services"),
    path('join/', lambda r: render(r, 'Join_Our.html'), name="join"),
    path('writers/', lambda r: render(r, 'For_Writers.html'), name="writers"),
    path('client-dashboard/', lambda r: render(r, 'client-dashboard.html'), name="client_dashboard"),
    path('writer-dashboard/', lambda r: render(r, 'writer-dashboard.html'), name="writer_dashboard"),
    path('admin-dashboard/', lambda r: render(r, 'admin-dashboard.html'), name="admin_dashboard"),
    path('order-content/', lambda r: render(r, 'Order_Content.html'), name="order_content"),
    path('enterprise/', lambda r: render(r, 'Enterprise-Domain.html'), name="enterprise"),
]

