from BugTrackApp import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('post/<int:ticket_id>/edit/', views.edit_ticket),
    path('post/<int:ticket_id>/', views.ticket_details),
    path('newticket/', views.new_ticket),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('claim/<int:ticket_id>/', views.claim_ticket),
    path('complete/<int:ticket_id>/', views.complete_ticket),
    path('invalidate/<int:ticket_id>/', views.invalidate_ticket),
]
