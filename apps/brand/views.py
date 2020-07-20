from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

from apps.brand.models import Brand
from apps.brand.serializers import BrandSerializer


@api_view(http_method_names=['GET', 'POST', 'PUT'])
def brand_info(request):
    if request.method == "POST":
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        brands = Brand.objects.all()
        serializers = BrandSerializer(brands, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        id = request.GET.get('pk')
        brand = Brand.objects.get(pk=id)
        brand.description = request.POST.get('description')
        brand.save()
        serializer = BrandSerializer(brand)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.data)
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


def brand_list(request):
    brandlist = Brand.objects.all().values_list(flat=True)
    print(brandlist)
    return HttpResponse('llll')
