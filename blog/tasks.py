from blog.models import Post


class PostTask:
    def post_update_is_activate():
        try:

            posts = Post.objects.all()
            for post in posts:
                post.save()
            print('Try')
        except:
            #pass
            print('Excetp')
