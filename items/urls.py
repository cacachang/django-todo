from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('edit/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete")
]
