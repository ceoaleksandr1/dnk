from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from crm import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('staf/<int:id>', staf, name='staf'),
    path('create_staf/', create_staf, name='create_staf'),
    path('create_channel/', create_channel_view, name='create_channel'),
    path('channel/<int:id>', channel_view, name='channel'),
    path('<str:page>', main, name='main'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
