from django.contrib import admin
from django.urls import path
from . import views
from .views import LoginView,   LogoutView, PasteUpdate
#RegisterView, DashboardView,

urlpatterns = [
  # path('register/', RegisterView.as_view(), name='register-view'),
  # path('dashboard/', DashboardView.as_view(), name='dashboard-view'),
    path('login/', LoginView.as_view(), name='login-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('pdf/', views.GeneratePdf.as_view(), name='pdf'),
    path('table_eggs/', views.GenerateHt.as_view(), name='table_eggs'),
    path('MyView/', views.MyView.as_view(), name='MyView'),
    path('edit/<int:id>', PasteUpdate.as_view(), name='edit'),

]