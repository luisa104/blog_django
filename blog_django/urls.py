
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from blog_django.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('accounts/', include('account.urls')), # incluir la url de la aplicacion
    path('categoria/', include('category.urls')),
    path('blog/', include('blog.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #dectetar los archivos esticos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#arhivos media

