from rest_framework import serializers
from .models import *


class BlogSerializer(serializers.ModelSerializer):
    #SerializerMethodfield
    len_blog_title = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = '__all__'
        # three types validators in serializer
        #field -level
        #object-level
        #validators
    def get_len_blog_title(self,object):
        return len(object.blog_title) #it gives the lenth of blog title
        
        
    #field value validators
    def validate_blog_title(self, value):
      
        if len(value) < 4:
            raise serializers.ValidationError("Blog name is too short")
        return value
    
    #object level validate
    def validate(self, data):
        if data['blog_title'] == data['author']:
            raise serializers.ValidationError("name and author cannot be same")
        return data

class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField()
    category = BlogSerializer(many=True,read_only=True)
      #string-related field - is retrun __str__ function
    #category = serializers.StringRelatedField(many=True)
        #primaryRelatedField - is give the primary id of data
    #category = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
        #hyperLinked FIeld - is give the url of blog
    #category = serializers.HyperlinkedRelatedField(
        #many=True,
        #read_only=True,
        #view_name='blog_details')
        #slug relatedfield - is return slugvalue
    #category = serializers.SlugRelatedField(many=True,slug_field='slug',read_only=True)
    
    class Meta:
        model = Category
        exclude =['id',]
    
    
'''
#HyperlinkedModelSerializer
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category_name = serializers.CharField()
    category = BlogSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields ='__all__'

'''
    
        