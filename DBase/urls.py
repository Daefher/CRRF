from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libro/', include('libro.urls')),
    path('users/', include('users.urls')),
    path('',user_views.login_view, name='home'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
