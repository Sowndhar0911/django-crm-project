from django.urls import path
from .views import dashboard, lead_list, add_lead
from . import views


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('leads/', lead_list, name='lead_list'),
    path('leads/add/', add_lead, name='add_lead'),
    path('update/<int:pk>/', views.update_lead, name='lead_update'),
    path('delete/<int:pk>/', views.delete_lead, name='lead_delete'),
    path('dashboard/', views.dashboard, name='dashboard'),

    ]