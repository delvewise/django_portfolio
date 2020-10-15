from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (
    index,
    search,
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
    IndexView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    AboutView,
    ContactView,
    ResumeListView,
    ResumeDetailView,
)
from marketing.views import email_list_signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('blog/', PostListView.as_view(), name='post-list'),
    path('search/', search, name='search'),
    path('email-signup/', email_list_signup, name='email-list-signup'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    #path('users/', include('users.urls')),
    path('contact/', ContactView.as_view(), name='contactpage'),
    path('about/', AboutView.as_view(), name='about'),
    path('resume/', ResumeListView.as_view(), name= 'resume'),
    path('resume/<pk>/', ResumeDetailView.as_view(), name='resume-detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
