from django.urls import path
from . import views

app_name = 'grocerylist'
urlpatterns = [
    path('', views.index, name='index'),
    path('complete/', views.complete, name='complete'),
    path('create_todo', views.create_todo, name='create_todo'),
    path('complete_todo/<int:item_id>', views.complete_todo, name='complete_todo')
]
