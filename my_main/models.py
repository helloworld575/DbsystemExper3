from django.db import models

# Create your models here.
class Customer(models.Model):

    SexType = (
        ("male","男"),
        ("female","女")
    )

    CusNum = models.IntegerField(primary_key=True)
    CusName = models.CharField(max_length=10)
    CusSex = models.CharField(max_length=10,choices=SexType)

    def __str__(self):
        return self.CusName

class Consume(models.Model):

    Type = (
        ("movie","电影"),
        ("products","商品")
    )

    ConsumeNum = models.IntegerField(primary_key=True)
    ConsumeType = models.CharField(max_length=10,choices=Type)
    ConsumeAmount = models.IntegerField(default=0)
    Consumer = models.ForeignKey(Customer)

    def __str__(self):
        return self.ConsumeNum

class Employee(models.Model):

    Type = (
        ("movieServer","电影院服务员"),
        ("storeServer","商店服务员"),
        ("movieAdmin","电影院管理员"),
        ("storeAdmin","商店管理员")
    )
    SexType = (
        ("male","男"),
        ("female","女")
    )

    EmploeeNum = models.IntegerField(primary_key=True)
    EmploeeName = models.CharField(max_length=10)
    EmploeeSex = models.CharField(max_length=5,choices=SexType)
    EmploeeDuty = models.CharField(max_length=20,choices=Type)

    def __str__(self):
        return self.EmploeeName

class MovieHouse(models.Model):

    HouseNum = models.IntegerField(primary_key=True)
    HousePlace = models.CharField(max_length=50)
    HouseName = models.CharField(max_length=20)
    HouseEmployee = models.ForeignKey(Employee)

    def __str__(self):
        return self.HouseName

class MovieSeat(models.Model):

    SeatNum = models.IntegerField(primary_key=True)
    SeatCustomer = models.OneToOneField(Customer)
    SeatHouse = models.ForeignKey(MovieHouse)
    SeatRow = models.IntegerField()
    SeatLine = models.IntegerField()

    def __str__(self):
        return self.SeatNum

class Store(models.Model):

    StoreNum = models.IntegerField(primary_key=True)
    StoreName = models.CharField(max_length=20)
    StorePlace = models.CharField(max_length=50)
    StoreEmployee = models.ForeignKey(Employee)

    def __str__(self):
        return self.StoreName

class Supplier(models.Model):

    SupplierNum = models.IntegerField(primary_key=True)
    SupplierName = models.CharField(max_length=20)
    SupplierConnect = models.CharField(max_length=100)

    SupplyConsume = models.ManyToManyField(Store)

    def __str__(self):
        return self.SupplierName

class Goods(models.Model):

    GoodsNum = models.IntegerField(primary_key=True)
    GoodsName = models.CharField(max_length=50)
    GoodsPrice = models.IntegerField(default=0)

    GoodsSupplier = models.ForeignKey(Supplier)
    GoodsStore = models.ForeignKey(Store)

    def __str__(self):
        return self.GoodsName

class MovieSupplier(models.Model):

    SupplierNum = models.IntegerField(primary_key=True)
    SupplierName = models.CharField(max_length=50)
    SupplierConnect = models.CharField(max_length=100)

    def __str__(self):
        return self.SupplierName

class Movie(models.Model):

    MovieNum = models.IntegerField(primary_key=True)
    MovieName = models.CharField(max_length=50)
    MovieRank = models.IntegerField()
    MovieProductor = models.CharField(max_length=20)
    MovieSupp = models.ForeignKey(MovieSupplier)
    MovieHouse = models.ManyToManyField(MovieHouse)

    def __str__(self):
        return self.MovieName

