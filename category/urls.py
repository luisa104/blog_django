from django.urls import path

from category.views import CategoryCreateView, CategoryView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('', CategoryView.as_view(), name="category"),
    path('agregar/', CategoryCreateView.as_view(), name="category_create"),
    path('editar/<slug:slug>/', CategoryUpdateView.as_view(), name="category_update"),
    path('eliminar/<slug:slug>/', CategoryDeleteView.as_view(), name="category_delete"),
]