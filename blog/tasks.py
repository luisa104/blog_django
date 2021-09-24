from datetime import datetime
import pytz

from blog.models import Post


class PostTask:
    def post_update_is_activate():
        try:
            posts = Post.objects.all()
            for post in posts:
                post.save()
        except:
            pass

