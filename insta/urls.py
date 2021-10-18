from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.home_page,name = 'imageIndex'),
    url('^post$',views.post_image,name = 'new_posts'),
    url('^profile/update/',views.update_profile,name = 'update_profile'),
    url('^profile/',views.profile_page,name = 'profile_page'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)