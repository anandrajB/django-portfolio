from django.urls import path
from . import views
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from django.conf.urls import handler404


urlpatterns = [
    path('', views.index, name='home'),
    path('resume',views.resume , ),
    path('contact', views.contact ,),
    path('portfolio', views.portfolio,),
    url(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('maintanance',views.maintanace_mode,),
   ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
