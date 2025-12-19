from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from portfolio.serializers.product_serializers import CategorySerializer, ProductSerializer
from portfolio.models.product_models import Category, Product
from rest_framework.permissions import AllowAny


class GetAllCategoryAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class GetALlProductsAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



class GetProductsByCategoryAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        products = Product.objects.filter(category=pk)

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
