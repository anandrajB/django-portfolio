from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('myadminpaneldjango/', admin.site.urls),
    path('', include('app.urls')), 
]
handler404 = 'app.views.handler404'