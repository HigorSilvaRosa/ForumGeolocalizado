from ForumGeolocalizado import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from core.views import TopicView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ForumGeolocalizado.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^topic/', TopicView.as_view(), name='topic'),
)

#
urlpatterns += patterns('',
    # ... the rest of your URLconf goes here ...
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('',
    # ... the rest of your URLconf goes here ...
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
