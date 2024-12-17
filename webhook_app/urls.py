from django.contrib import admin
from django.urls import path,include
from . views import accountListCreateView,accountRetrieveUpdateView,destionationListCreateView,destinationRetrieveUpdateView,incoming_data

urlpatterns = [
    #Accounts Url
    path('accounts/',accountListCreateView.as_view(),name="create_account_view"),
    path('accounts/<uuid:account_id>',accountRetrieveUpdateView.as_view(),name="retrieve_update_destroy_account_view"),
    #Destination CRUD Operation URL
    path('destinations/<uuid:account_id>/',destionationListCreateView.as_view(),name="create_destination_view"),
    path('destinations/<uuid:account_id>/<int:pk>/',destinationRetrieveUpdateView.as_view(),name="retrieve_update_destroy_destintion_view"),
    #Handling Incoming Data
    path('servers/incoming_data/',incoming_data,name='incoming_data')
]