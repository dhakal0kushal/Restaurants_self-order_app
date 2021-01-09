from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name="api-overview"),
  # category apis
  path('category-list', views.categoryList, name="category-list"),
  path('category-detail/<str:pk>', views.categoryDetail, name="category-detail"),
  path('category-create', views.categoryCreate, name="category-create"),
  path('category-update/<str:pk>', views.categoryUpdate, name="category-update"),
  path('category-delete/<str:pk>', views.categoryDelete, name="category-delete"),
  # Item apis
  path('item-list/', views.itemList, name="item-list"),
  path('item-detail/<str:pk>', views.itemDetail, name="item-detail"),
  path('item-create', views.itemCreate, name="item-create"),
  path('item-update/<str:pk>', views.itemUpdate, name="item-update"),
  path('item-delete/<str:pk>', views.itemDelete, name="item-delete"),
]