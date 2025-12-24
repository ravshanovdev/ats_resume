from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from portfolio.serializers.product_serializers import (CategorySerializer, ProductSerializer, AddProductSerializer,
                                                       UserOpinionAboutProductSerializer)
from portfolio.models.product_models import Category, Product, UserOpinionAboutProduct
from rest_framework.permissions import AllowAny, IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser


class GetAllUserOpinionAboutProductAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        user_opinions = UserOpinionAboutProduct.objects.all()

        serializer = UserOpinionAboutProductSerializer(user_opinions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
        request_body=CategorySerializer(partial=True),
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


# FOR ADMIN PANEL Product

class AddProductAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['admin_panel_product'],
        request_body=AddProductSerializer,
        responses={201: f"{AddProductSerializer}"}
    )
    def post(self, request):
        serializer = AddProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProductAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['admin_panel_product'],
        request_body=AddProductSerializer(partial=True),
        responses={200: f"{AddProductSerializer}"}
    )
    def patch(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"messgae": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProductAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_product']
    )
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"messgae": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        product.delete()

        return Response({"message": "object successfully deleted.!"}, status=status.HTTP_200_OK)


# FOR ADMIN PANEL UserOpinionAboutProduct

class AddUserOpinionAboutProductAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_user_opinion_about_product'],
        request_body=UserOpinionAboutProductSerializer,
        responses={201: f"{UserOpinionAboutProductSerializer}"}
    )
    def post(self, request):
        serializer = UserOpinionAboutProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserOpinionAboutProductAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_user_opinion_about_product'],
        request_body=UserOpinionAboutProductSerializer(partial=True),
        responses={200: f"{UserOpinionAboutProductSerializer}"}
    )
    def patch(self, request, pk):
        try:
            product = UserOpinionAboutProduct.objects.get(pk=pk)
        except UserOpinionAboutProduct.DoesNotExist:
            return Response({"messgae": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserOpinionAboutProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeleteUserOpinionAboutProductAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_user_opinion_about_product']
    )
    def delete(self, request, pk):
        try:
            product = UserOpinionAboutProduct.objects.get(pk=pk)
        except UserOpinionAboutProduct.DoesNotExist:
            return Response({"messgae": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        product.delete()

        return Response({"message": "object successfully deleted.!"}, status=status.HTTP_200_OK)


