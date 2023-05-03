from django.urls import path
from . import views

urlpatterns = [
    # path('buy/<int:item_id>/session/', views.create_payment, name='create_payment'),
    path('buy/<int:item_id>/', views.create_payment, name='create_payment'),
    path('item/<int:item_id>/', views.get_item_page, name='get_item_page'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
]