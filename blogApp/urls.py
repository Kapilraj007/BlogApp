from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.BlogGetPostGenericViewset.as_view(),name='home'),
   
    #path('blog_details/<str:pk>/',views.blog_details,name = 'blog_details'),
    
    #class-based views
    #category_urls
    #path('category_list/',views.CategoryListView.as_view(),name = 'category_list'),
    #path('category_detials/<int:pk>',views.CategoryDetailsListView.as_view(),name = 'category-detail'),
    
    #generic Viewset
    #path('blogs/',views.BlogGetPostGenericViewset.as_view(),name = 'blogs'),

    #concerete view
    path('blogs/',views.CreateBlog.as_view(),name='create-blog'),
    path('blogslist/',views.ListBlogCon.as_view(),name='blog-list'), 
]
