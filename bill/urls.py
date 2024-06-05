from django.urls import path, include


from .views import getProductData, getCompanyData, addCompany, addProductData,CompanyViewset, ProductViewset, CategoryViewset, addCategoryData, getCategoryData

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"company",CompanyViewset)
router.register(r'product', ProductViewset, basename='product')
router.register(r"category",CategoryViewset)

urlpatterns = [

    path("",include(router.urls)),
    path('product/<str:org_name>/', ProductViewset.as_view({'get': 'list'}), name='product-list-org'),
    path("addCompany/",addCompany,name="addCompany"),
    path("getCompany/<str:org_name>/",getCompanyData, name="getCompany"),
    path("getProduct/<str:org_name>/",getProductData, name="getProduct"),
    path("addProduct/",addProductData, name="addProduct"),
    path("getCategory/<str:org_name>/",getCategoryData, name="getCategory"),
    path("addCategory/",addCategoryData, name="addCategory")
    
]
