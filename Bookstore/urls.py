from django.contrib import admin
from django.urls import path 
from Books import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('addbook/', views.addbook),
    path('books/',views.booklist),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)