from django.urls import path
from .views import *

#BaseURL =>> #http://127.0.0.1:8000/ems/

urlpatterns = [
    path('show/',view_show_Employee,name='show'),
    path('add/',view_add_Employee,name='add'),
    path('update/<int:eid>/',view_update_Employee,name='update'),
    path('delete/<int:eid>/',view_delete_Employee,name='delete'),
]
