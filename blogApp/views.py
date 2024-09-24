from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from .serializers import *
from .models import *

# Create your views here.

class CategoryListView(APIView):
    def get(self,request):
        all_category = Category.objects.all()
        serializer = CategorySerializer(all_category,many=True,context = {'request':request})
        return Response(serializer.data)

class CategoryDetailsListView(APIView):
    def get(self,request,pk):
        category_detials = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category_detials,context = {'request':request})
        return Response(serializer.data)
        
    '''
@api_view(['GET','POST'])
def home(request):
    if request.method=='GET':
        all_public_blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializer(all_public_blogs,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

@api_view(['GET','PUT','DELETE'])
def blog_details(request,pk):
    if request.method=='GET':
        blog = Blog.objects.get(pk=pk,is_public=True)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)    
    if request.method=='PUT':
        blog = Blog.objects.get(pk=pk,is_public=True)
        serializer =BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method=='DELETE':
        blog = Blog.objects.get(pk=pk,is_public=True)
        blog.delete()
        return Response('deleted successfully')
'''
class BlogGetPostGenericViewset(ListModelMixin,CreateModelMixin,generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.post(request,*args, **kwargs)
    
#concerete views
class CreateBlog(generics.CreateAPIView):
    queryset=Blog.objects.all()
    serializer_class= BlogSerializer
    
class ListBlogCon(generics.ListAPIView):
    queryset=Blog.objects.all()
    serializer_class = BlogSerializer
