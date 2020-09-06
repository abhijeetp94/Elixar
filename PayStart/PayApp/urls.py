from django.contrib import admin
from django.urls import path
from . import views

app_name = 'PayApp'

urlpatterns = [
    path('', views.Home, name = "home"),
    path('FreeTrial/', views.Trial, name = "Trial"),
    path('<str:course>/RegisterPayment/', views.PaymentLogin, name = "PaymentLogin"),
    path('Verify/', views.Verify, name = "Verify"),
    path('Verify_for_payment/', views.verifyPay, name = "verifyPay"),
    path('Calender/', views.Calender, name = "Calender"),
    path('confirm_order', views.create_order, name = 'create_order'),
    path('payment_status', views.payment_status, name = 'payment_status'),
]