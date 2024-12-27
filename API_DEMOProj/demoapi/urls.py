from django.urls import path
from .views import *

#Base URL =>>> http://127.0.0.1:8000/api/

urlpatterns = [
    path('first/', view_first_api),
    path('insert/', view_Insert_Employee),
    path('get/', view_Show_Employee),
    path('get/<int:eid>/', view_GetById_Employee),
    path('update/<int:eid>/', view_Update_Employee),
    path('delete/<int:eid>/', view_Delete_Employee),
]