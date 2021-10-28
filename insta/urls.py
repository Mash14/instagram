from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.home_page,name = 'imageIndex'),
    url('signup/', views.signUp, name='signup'),
    url('^post$',views.post_image,name = 'new_posts'),
    url('^profile/update/',views.update_profile,name = 'update_profile'),
    url('^profile/',views.profile_page,name = 'profile_page'),
    url('single/(?P<id>\d+)',views.single_view, name = 'single_image'),
    url('^search/', views.search_user, name = 'searched_profiles'),
    url('^comment/<id>', views.comment_create, name='comment_page'),
    url('like/', views.like_post, name='like-post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)