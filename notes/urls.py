from django.urls import path

from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('<int:note_id>/', views.index, name='index'),
  path('avatar/', views.avatar, name='avatar'),
]
