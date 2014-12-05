from ForumGeolocalizado import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from core.views import TopicView, HomeView, LoginView, LogoutView, CreateTopicView
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ForumGeolocalizado.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^topic/(?P<topic_id>\d+)', TopicView.as_view(), name='topic'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^create-topic/$', CreateTopicView.as_view(), name='create-topic'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

#
urlpatterns += patterns('',
    # ... the rest of your URLconf goes here ...
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('',
    # ... the rest of your URLconf goes here ...
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
