from django.forms import ModelForm

from category.models import Category


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Category
        #campos que se quiere mostrar
        fields = ['name', 'slug']
