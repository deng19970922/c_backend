from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
    # elif request.method == "PUT":
    #     request.
