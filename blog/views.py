from datetime import timedelta, date, datetime

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment
from django.db.models import Q

from blog.tasks import PostTask


class PostListView(ListView):
    PostTask.post_update_is_activate()
    model = Post
    template_name = "blog/post.html"
    paginate_by = 6
    ordering = ['create_date']

    def get_queryset(self):
        queryset = self.request.GET.get("buscar")
        queryset_date1 = self.request.GET.get("date1")
        queryset_date2 = self.request.GET.get("date2")

        object_list = self.model.objects.filter(is_activate=True)
        if queryset:
            object_list = self.model.objects.filter(
                Q(title__icontains=queryset) |
                Q(category__name__icontains=queryset)
            ).distinct()

        if queryset_date1 and queryset_date2:
            una_fecha = queryset_date2
            fecha_dt = datetime.strptime(una_fecha, '%Y-%m-%d')
            queryset_date2 = fecha_dt + timedelta(1)

            object_list = self.model.objects.filter(create_date__range=(queryset_date1, queryset_date2), is_activate=True)

        return object_list



class PostDetailView(DetailView, CreateView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post__slug=self.object.slug)
        return context

    def get_success_url(self):
        post_id = self.request.POST.get('post')
        post_slug = Post.objects.filter(id=post_id).values('slug')[0]['slug']
        return reverse('post_detail', kwargs={'slug': post_slug})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        kwargs['object'] = self.object
        return kwargs


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_create.html"
    success_url = reverse_lazy('post')
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datetimenow'] = datetime.now().strftime("%Y-%m-%dT%H:%M")
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_update.html"
    success_url = reverse_lazy('post')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        elif request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        elif request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        return redirect('post')



class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy('post')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        elif request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        elif request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        return redirect('post')
