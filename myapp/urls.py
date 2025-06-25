from django.urls import path
from .views import home, view_data, combined_table  # Import all your views

urlpatterns = [
    path('', home, name='home'),
    path('view-data/', view_data, name='view_data'),
    path('combined/', combined_table, name='combined_table'),  # Add this line
]