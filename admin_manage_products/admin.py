from django.contrib import admin
from .models import AwWineType,AwProducts , AwProductImage , AwProductPrice,AwProductImageFullView , AwProductReviews
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AwProductPriceAdmin(ImportExportModelAdmin):
    list_display = ('Product', 'Vintage_Year','Bottle','Retail_Cost','Retail_Stock','Descount_Cost','Duty','GST','Bond_Cost','Bond_Stock','Created_by', 'Created_date','Created_date','Updated_date')
    list_filter = ('Created_date','Vintage_Year','Product','Updated_date',)
admin.site.register(AwProductPrice,AwProductPriceAdmin)


class AwProductReviewsAdmin(ImportExportModelAdmin):
    list_display = ('LWineCode', 'Publication','reviewer','reviewDate','scoreRaw','scoreFrom','scoreTo','scoreMedian','drinkFrom','drinkTo','externalReference', 'externalLink','externalId')
    list_filter = ('LWineCode','Publication',)
admin.site.register(AwProductReviews,AwProductReviewsAdmin)

class AwProductImageAdmin(ImportExportModelAdmin):
    list_display = ('Product', 'Image_Type','Image','Created_by', 'Created_date','Created_date','Updated_date')
    list_filter = ('Created_date','Image_Type','Product','Updated_date',)
admin.site.register(AwProductImage,AwProductImageAdmin)


class AwWineTypeAdmin(ImportExportModelAdmin):
    list_display = ('Type', 'Status','Created_by', 'Created_date','Created_date','Updated_date')
    list_filter = ('Created_date','Updated_date',)
admin.site.register(AwWineType,AwWineTypeAdmin)

class AwProductsAdmin(ImportExportModelAdmin):
    list_display = ('Product_id', 'LWineCode' , 'Select_Type','Product_name','Producer','Country','Regions','Status', 'Created_date','Created_date','Updated_date')
    list_filter = ('Select_Type','Producer','Created_date','Updated_date',)
    readonly_fields = ["Product_id", 'Product_slug']
admin.site.register(AwProducts,AwProductsAdmin)



class AwProductImageFullViewAdmin(ImportExportModelAdmin):
    list_display = ('Product', 'Image','Create_date')
    list_filter = ('Product','Create_date',)
admin.site.register(AwProductImageFullView,AwProductImageFullViewAdmin)