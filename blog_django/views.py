from django.views.generic import TemplateView

from blog.models import Post
from blog.tasks import PostTask


class HomeView(TemplateView):
    PostTask.post_update_is_activate()
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(is_activate=True)[:4]
        return context




