from django.forms import ModelForm
from .models import Post, Comment, Like

from datetime import datetime


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control'})
        self.fields['theme'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_activate'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['image_front'].widget.attrs.update({'class': 'form-control'})

        self.fields['image'].widget.attrs.update(accept='image/png,image/jpeg, image/jpg')
        self.fields['image_front'].widget.attrs.update(accept='image/png,image/jpeg')

    class Meta:
        model = Post
        fields = ['author', 'title', 'slug', 'theme', 'category', 'description', 'image', 'image_front', 'is_activate', 'activate_date', 'due_date']


class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.object = kwargs.pop('object', None)

        super().__init__(*args, **kwargs)
        self.initial['user'] = self.request.user
        self.initial['post'] = self.object
        self.fields['user'].widget.attrs.update({'class': 'visually-hidden'})
        self.fields['post'].widget.attrs.update({'class': 'visually-hidden'})

    class Meta:
        model = Comment
        fields = ['user', 'post', 'content']


class LikeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        #self.request = kwargs.pop('request', None)
        #self.object = kwargs.pop('object', None)

        super().__init__(*args, **kwargs)
        #self.initial['user'] = self.request.user
        #self.initial['post'] = self.object
        #self.fields['user'].widget.attrs.update({'class': 'visually-hidden'})
        #self.fields['post'].widget.attrs.update({'class': 'visually-hidden'})

    class Meta:
        model = Like
        fields = ['user', 'post', 'like']