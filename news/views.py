from rest_framework import generics, status, serializers
from rest_framework.response import Response

from news.models import News
from news.pagination import NewsPaginator
from news.serializers import NewsSerializer


class NewsListAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    pagination_class = NewsPaginator

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        try:
            data = {
                "Success": True,
                "News": serializer.data
            }

            return Response(data)
        except Exception as e:
            error_data = {
                "Success": False,
                "News": str(e)
            }
            return Response(error_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class NewsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response({
                "Success": True,
                "News": serializer.data
            })

        except serializers.ValidationError as validation_error:
            return Response({
                "Success": False,
                "News": str(validation_error.detail)
            }, status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "Success": False,
                "News": str(e)
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)
