from api.views import (
    PersonListCreate , PersonDetail ,
    DateListCreate , DateDetail ,
    TaskListCreate , TaskDetail ,
    AllDateView
)
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.api , name='api' ) , 

    path('persons/', PersonListCreate.as_view() , name='persons'),
    path('persons/<int:pk>' ,PersonDetail.as_view(), name='person-detail') ,

    path('dates/' ,DateListCreate.as_view(), name='dates-list') ,
    path('dates/<int:pk>' , DateDetail.as_view() ,name='dates-detail' , ) ,

    path('tasks/' , TaskListCreate.as_view() , name='task-list') ,
    path('tasks/<int:pk>' , TaskDetail.as_view() , name='tasks-detail') ,
    
    path('persons/dates' , AllDateView.as_view() , name='all-dates')
]
