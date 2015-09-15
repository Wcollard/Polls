from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.view_post, name='view_post'),
    url(r'^(?P<pk>[0-9]+)/category/$', views.view_category, name='view_category'))


#url(r'^blog/view/(?P<slug>[^\.]+).html', 'blog.views.view_post', name='view_blog_post'),
#url(r'^blog/category/(?P<slug>[^\.]+).html','blog.views.view_category', name='view_blog_category'))
