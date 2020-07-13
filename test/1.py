from apps.brand.models import Brand

brandlist = Brand.objects.all().values_list(flat=True)
print(brandlist)