from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'brand.Brand'
        fields = ('id', 'name', 'status', 'description')
