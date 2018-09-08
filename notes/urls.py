from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('<int:note_id>/', views.index, name='index'),
  path('avatar/', views.avatar, name='avatar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
