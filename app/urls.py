from django.urls import path, include
from .views import HomePageView, AboutPageView, ServicesPageView 
from .import views


urlpatterns = [
    # Main Page
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('services/', ServicesPageView.as_view(), name='services'),


    # Client URLs
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('clients/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),


    # SupportTicket URLs
    path('tickets/', views.SupportTicketListView.as_view(), name='supportticket_list'),
    path('tickets/create/', views.SupportTicketCreateView.as_view(), name='supportticket_create'),
    path('tickets/<int:pk>/update/', views.SupportTicketUpdateView.as_view(), name='supportticket_update'),
    path('tickets/<int:pk>/delete/', views.SupportTicketDeleteView.as_view(), name='supportticket_delete'),
    

    # Staff URLs
    path('staff/', views.StaffListView.as_view(), name='staff_list'),
    path('staff/create/', views.StaffCreateView.as_view(), name='staff_create'),
    path('staff/<int:pk>/update/', views.StaffUpdateView.as_view(), name='staff_update'),
    path('staff/<int:pk>/delete/', views.StaffDeleteView.as_view(), name='staff_delete'),





    
]