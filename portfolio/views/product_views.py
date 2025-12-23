from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from portfolio.serializers.product_serializers import CategorySerializer, ProductSerializer
from portfolio.models.product_models import Category, Product
from rest_framework.permissions import AllowAny, IsAdminUser
from drf_yasg.utils import swagger_auto_schema


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


# FOR ADMIN PANEL Category

class AddCategoryAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_category'],
        request_body=CategorySerializer,
        responses={201: f"{CategorySerializer}"}
    )
    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCategoryAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_category'],
        request_body=CategorySerializer,
        responses={200: f"{CategorySerializer}"}
    )
    def patch(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_200_OK)


class DeleteCategoryAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_category']
    )
    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        category.delete()

        return Response({"message": "object successfully deleted.!"}, status=status.HTTP_200_OK)
