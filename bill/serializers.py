from rest_framework import serializers

from . models import * 


class CompanySerializer(serializers.ModelSerializer):


    class Meta:

        model = Company

        fields = "__all__"



class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product

        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category

        fields = "__all__"

