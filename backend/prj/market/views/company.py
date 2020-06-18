from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from market.models import Company
from rest_framework import serializers

from market.views.category import CategorySerializer

class CompanySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Company
        firlds =['id', 'name', 'category', 'subcategory']

class CompanyListView(ListModelMixin, GenericAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    def get (self, *args, **kwargs):
        return self.list(request, *args, **kwargs)