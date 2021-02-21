from django.conf.urls import url 
from posts import views 
 
urlpatterns = [ 
    url(r'^api/posts$', views.post_list),
    url(r'^api/posts/(?P<pk>[0-9]+)$', views.post_detail),
    # url(r'^api/posts/published$', views.tutorial_list_published)
]