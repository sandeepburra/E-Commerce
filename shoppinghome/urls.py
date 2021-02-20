from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-page'),
    #path('home', views.home, name='home'),
    path('titleindex', views.titleindex, name='titleindex'),
    path('search', views.search, name='search'),
    path('product/uploaded/', views.uploaded, name="uploaded"),
    path('product/?P<int:qid>/', views.similar, name="similar"),
    path('title/?P<int:qid>/', views.similartitle, name="similartitle")
    
]