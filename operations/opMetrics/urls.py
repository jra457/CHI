from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('packagesperhour/', views.packagesPerHour, name='packagesperhour'),
    path('dex/', views.DEX, name='dex'),
    path('vas/', views.VAS, name='vas'),
    path('addpackages/', views.addpackages, name='addpackages'),
    path('search/', views.Search, name='search')
]