from django.urls import path, include
from api.router import urlpatterns

urlpatterns = [
    path('staff/', include('api.staff.urls')),
]
