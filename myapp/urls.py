from django.urls import path
from .import views
from .views import PostListView
from .feed import LatestPostFeed
from .import api
app_name='myapp'
urlpatterns = [
	path('post',PostListView.as_view(),name='post_list'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_details,name='post_detail'),
	path('<int:post_id>/share/',views.post_share, name='post_share'),
	path('tag/<slug:tag_slug>/',views.post_list,name='post_list_by_tag'),
    path('feed/',LatestPostFeed(),name='post_feed'),
    #api url
    path('api/v2/post',api.post_list_api,name='post_list_api'),
    path('api/v2/<int:id>',api.post_detail,name='post_detail_detail'),
	#path('',views.post_list,name='post_list'),
	#path('publisher/',PublisherList.as_view()),
    #path('publisher/<int:id>/',PublisherDetail.as_view()),
    #path('ex1',TemplateView.as_view(template_name='myapp/author1.html',extra_context={'title':'Custom Title'})),
    #path('ex2',AuthorView.as_view(),name='auther'),
] 