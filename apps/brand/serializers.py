from rest_framework import serializers


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = 'brand.Brand'
        fields = ('id', 'name', 'status', 'description')
