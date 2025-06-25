from django.contrib import admin
from django.urls import path, include  # Add include to the imports

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # This will include all URLs from your app
]