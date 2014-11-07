from django.contrib import admin
from system.models import *

# Register your models here.

class HomeShopAdvAdmin(admin.ModelAdmin):
    list_display = ('id','ShopID', 'AdvertisementContent', 'ApplyState')
    search_fields = ('id','ShopID', 'AdvertisementContent')

class HomeCommodityAdvAdmin(admin.ModelAdmin):
    list_display = ('id', 'CommodityID', 'AdvertisementContent', 'ApplyState')
    search_fields = ('id','AdvertisementContent')

class CommodityAdmin(admin.ModelAdmin):
    list_display = ('id', 'CommodityName', 'CommodityImage')
    search_fields = ('id', 'CommodityName', 'CommodityDescription')


admin.site.register(HelpCenter)
admin.site.register(Seller)
admin.site.register(Shop)
admin.site.register(Commodity, CommodityAdmin)
admin.site.register(ShopAdv)
admin.site.register(CommodityAdv)
admin.site.register(HomeShopAdv, HomeShopAdvAdmin)
admin.site.register(HomeCommodityAdv, HomeCommodityAdvAdmin)
admin.site.register(Administrator)
admin.site.register(System)
admin.site.register(BlacklistSeller)
admin.site.register(Discount)
admin.site.register(ShopOrder)
admin.site.register(Customer)
admin.site.register(OrderList)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(Favorite)
admin.site.register(CustomerOrder)
admin.site.register(BlacklistCustomer)
admin.site.register(Income)