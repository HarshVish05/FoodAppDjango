from django.urls import path
from .views import index, detail, create_item, update_item, delete_item, IndexClassView, DetailClassView, CreateItemView

app_name = 'core'

urlpatterns = [
    path('', IndexClassView.as_view(), name='index'),
    # path('', index, name= 'index'),
    path('detail/<str:pk>/', DetailClassView.as_view(), name='detail'),
    # path('detail/<str:pk>/', detail, name= 'detail'),

    # add items
    path('add/', CreateItemView.as_view(), name='create_item'),
    # path('add/', create_item, name= 'create_item'),
    # edit items
    path('update/<int:id>', update_item, name='update_item'),
    # delete items
    path('delete/<int:id>', delete_item, name='delete_item'),
]
