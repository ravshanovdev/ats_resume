from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from portfolio.serializers.blog_serializers import BlogSerializer
from portfolio.models.blog import Blog
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


class GetAllBlogsAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['portfolio'],
        responses={200: f"{BlogSerializer}"}
    )
    def get(self, request):
        blogs = Blog.objects.all()

        serializer = BlogSerializer(blogs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AddBlogForAdminAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['blog_for_admin'],
        request_body=BlogSerializer,
        responses={201: f"{BlogSerializer}"}
    )
    def post(self, request):
        serializer = BlogSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateBlogAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['blog_for_admin'],
        request_body=BlogSerializer,
        responses={200: f"{BlogSerializer}"}
    )
    def patch(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({"error": "object not found"}, status=status.HTTP_200_OK)

        serializer = BlogSerializer(blog, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteBlogAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['blog_for_admin']
    )
    def delete(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({"error": "object not found"}, status=status.HTTP_200_OK)

        blog.delete()

        return Response({"message": "object successfully deleted"}, status=status.HTTP_200_OK)











