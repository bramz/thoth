from django.urls import path

from . import views

urlpatterns = [
    path('', views.entries, name='entries'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('entry/', views.entry, name='entry'),
    path('<int:id>/', views.read),
]