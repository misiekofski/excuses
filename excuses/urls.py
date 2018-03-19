from django.urls import path

from . import views

urlpatterns = [
    # ex: /excuses/
    path('', views.index, name='index'),
    # ex: /excuses/2
    path('<int:excuse_id>/', views.excuse, name='excuse')
]