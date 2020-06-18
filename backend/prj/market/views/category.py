from rest_framework import serializers, viewsets, permissions
from rest_framework.decorators import action

from market.models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']

class CategoryViewSet(viewsets.ModelViewSet):
    '''
        API endpoint that allows user to read any modify categories.
    '''
    queryset = Category.objects.all().order_by('-id')
    serializer_class=CategorySerializer
    permission_classes=[permissions.AllowAny]
    http_method_names=['get', 'post']

    @action(detail=False, methods=['get'])
    def set_password(self, request):
        pass 

#Subcategory serializer
from rest_framework import serializers
from market.models import Category, SubCategory

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name']