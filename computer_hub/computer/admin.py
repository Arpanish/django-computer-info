from django.contrib import admin
from .models import ComputerBrand
from .models import ComputerSpecification
from .models import Computer


#Registration of ComputerBrand Model
@admin.register(ComputerBrand)
class ComputerBrandModel(admin.ModelAdmin):
    list_display=['id','brand_name','logo']


#Registration of ComputerSpecification Model
@admin.register(ComputerSpecification)
class ComputerBrandModel(admin.ModelAdmin):
    list_display=['id','generation','price_min','price_max','ram','brand']


#Registration of Computer Model
@admin.register(Computer)
class ComputerBrandModel(admin.ModelAdmin):
    list_display=['id','computer_code','computer','quantity','unit_rate','total_price']