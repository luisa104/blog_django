from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView


from category.forms import CategoryForm
from category.models import Category


class CategoryView(LoginRequiredMixin, TemplateView):
    template_name = "category/category.html"
     #mandar todas las categorias
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "category/category_create.html"
    #mandar formulario
    form_class = CategoryForm
    success_url = reverse_lazy('post_create')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "category/category_update.html"
    form_class = CategoryForm
    success_url = reverse_lazy('category')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "category/category_delete.html"
    success_url = reverse_lazy('category')
