from django.urls import path
from . import views
from .views import ZapasListView

urlpatterns = [
    path('', views.index, name='index'),
    path('kluby/', views.KlubListView.as_view(), name='list.html'),
    path('kluby/<int:pk>', views.KlubDetailView.as_view(), name='detail.html'),
    path('zapas/', ZapasListView.as_view(), name='zapas_list'),
]