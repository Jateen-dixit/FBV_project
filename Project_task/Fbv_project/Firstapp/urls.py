from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddLaptopView, name='add_order'),
    path('show/', views.ShowLaptopView, name='show_order'),
    path('update/<int:id>/', views.UpdateLaptopView, name='update'),
    path('delete/<int:id>/', views.DeleteLaptopView, name='delete')
]
