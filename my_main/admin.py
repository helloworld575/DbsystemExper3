from django.contrib import admin
import my_main.models

admin.site.site_header = '数据库实验三'
admin.site.site_title = '测试中'

class MovieSupplierAdmin(admin.ModelAdmin):

    list_display = ("SupplierNum","SupplierName","SupplierConnect")
    search_fields = ("SupplierNum","SupplierName","SupplierConnect")


class MovieAdmin(admin.ModelAdmin):

    list_display = ("MovieNum","MovieName","MovieProductor","MovieRank","MovieSupp")
    search_fields = ("MovieNum","MovieName","MovieProductor","MovieRank","MovieSupp")


class CustomerAdmin(admin.ModelAdmin):

    list_display = ("CusNum","CusName","CusSex")
    search_fields = ("CusNum","CusName","CusSex")


class MovieHouseAdmin(admin.ModelAdmin):

    list_display = ("HouseNum","HouseName","HousePlace")
    search_fields = ("HouseNum","HouseName","HousePlace")


class StoreAdmin(admin.ModelAdmin):

    list_display = ("StoreNum","StoreName","StorePlace")
    search_fields = ("StoreNum","StoreName","StorePlace")

class SupplierAdmin(admin.ModelAdmin):

    list_display = ("SupplierNum","SupplierName","SupplierConnect")
    search_fields = ("SupplierNum","SupplierName","SupplierConnect","SupplyConsume__StoreName")
    filter_horizontal = ("SupplyConsume",)


class ConsumeAdmin(admin.ModelAdmin):

    list_display = ("ConsumeNum","ConsumeType","ConsumeAmount","Consumer")
    search_fields = ("ConsumeNum","ConsumeType","ConsumeAmount","Consumer__CusName")


class EmployeeAdmin(admin.ModelAdmin):

    list_display = ("EmploeeNum","EmploeeName","EmploeeSex","EmploeeDuty")
    search_fields = ("EmploeeNum","EmploeeName","EmploeeSex","EmploeeDuty")

class GoodsAdmin(admin.ModelAdmin):

    list_display = ("GoodsNum","GoodsName","GoodsPrice","GoodsSupplier","GoodsStore")
    search_fields = ("GoodsNum","GoodsName","GoodsPrice","GoodsSupplier","GoodsStore")


class MovieSeatAdmin(admin.ModelAdmin):

    list_display = ("SeatNum","SeatCustomer","SeatHouse","SeatRow","SeatLine")
    search_fields = ("SeatNum","SeatCustomer","SeatHouse","SeatRow","SeatLine")


admin.site.register(my_main.models.MovieSupplier, MovieSupplierAdmin)
admin.site.register(my_main.models.Movie,MovieAdmin)
admin.site.register(my_main.models.Customer,CustomerAdmin)
admin.site.register(my_main.models.MovieHouse,MovieHouseAdmin)
admin.site.register(my_main.models.Store,StoreAdmin)
admin.site.register(my_main.models.Supplier,SupplierAdmin)
admin.site.register(my_main.models.Consume,ConsumeAdmin)
admin.site.register(my_main.models.Employee,EmployeeAdmin)
admin.site.register(my_main.models.Goods,GoodsAdmin)
admin.site.register(my_main.models.MovieSeat,MovieSeatAdmin)