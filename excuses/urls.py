from django.urls import path

from . import views

urlpatterns = [
    # ex: /excuses/
    path('', views.index, name='index'),
    # ex: /excuses/2
    path('<int:excuse_id>/', views.excuse, name='excuse'),
    # ex: /bugs
    path('bugs/', views.bugs_list, name='bugs_list'),
    # ex: /buglist
    path('bugs/<int:bug_id>/', views.bug_detail, name='buglist')

]