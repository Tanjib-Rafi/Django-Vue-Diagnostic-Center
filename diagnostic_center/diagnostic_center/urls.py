from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('diagnostic.urls',namespace = "diagnostic")),
    path('api/',include('diagnostic_api.urls', namespace="diagnostic_api")),

]
