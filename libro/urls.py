from django.urls import path
from .views import (
    proyect_list_view,
    proyect_detail_view,
    proyect_create_view,
    proyect_update_view,
    proyect_delete_view,
)

app_name = 'libro'
urlpatterns = [
    path('',proyect_list_view.as_view(),name='proyect-list'),
    path('create/', proyect_create_view.as_view(), name='proyect-create'),
    path('<int:id>/',proyect_detail_view.as_view(), name='proyect-detail'),   
    path('<int:id>/update/', proyect_update_view.as_view(), name='proyect-update'),
    path('<int:id>/delete/',proyect_delete_view.as_view(), name='proyect-delete'),
]