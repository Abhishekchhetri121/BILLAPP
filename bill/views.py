from django.shortcuts import render

from . models import *
from django.http import Http404

from .serializers import CompanySerializer, ProductSerializer, CategorySerializer

from rest_framework  import viewsets, status

from rest_framework.decorators import api_view

from rest_framework.response import Response
# Create your views here.

from django.db.models import Q


class CompanyViewset(viewsets.ModelViewSet):

    queryset=Company.objects.all()

    serializer_class = CompanySerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        org_name = request.query_params.get('org_name')
        if not org_name:
            return Response({"error": "org_name query parameter is required"}, status=400)
        try:
            company = Company.objects.get(name=org_name)
            category = Category.objects.filter(company=company.id)
            items = Product.objects.filter(company=company.id)
            serializer = ProductSerializer(items, many=True)
            return Response(serializer.data)
        except Company.DoesNotExist:
            raise Http404("Company does not exist")

            

class CategoryViewset(viewsets.ModelViewSet):

    queryset=Category.objects.all()

    serializer_class = CategorySerializer

@api_view(['POST'])
def addCompany(request):
    serializer = CompanySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201) 
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def getCompanyData(request, org_name):

    company = Company.objects.filter(name=org_name)


    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addProductData(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201) 
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def getProductData(request, org_name):

    # category = Category.objects.get(company=org_name)
    companies = Company.objects.get(name=org_name)
    category = Category.objects.filter(company=companies.id)
    print(companies.id)

    try:
        compani = Company.objects.get(name=org_name)
        # category = Category.objects.get(company=org_name)

        # print("Category",category)
        # items = Product.objects.filter(Q(company=companies) & Q(category=category))
        items = Product.objects.filter(company=compani.id)
        serializer = ProductSerializer(items, many=True)
        return Response(serializer.data)
    except Company.DoesNotExist:
        raise Http404("Company does not exist")


@api_view(['POST'])
def addCategoryData(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201) 
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def getCategoryData(request, org_name):
    try:
        companies = Company.objects.get(name=org_name)
        category = Category.objects.filter(company=companies.id)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    except Company.DoesNotExist:
        raise Http404("Company does not exist")