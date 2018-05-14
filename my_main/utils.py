from django.db import connection

def my_custom_sql(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        index = cursor.description
        print(index)
        rows = cursor.fetchall()
        result = []
        for res in rows:
            row = {}
            for i in range(len(index)-1):
                row[index[i][0]] = res[i]
            result.append(row)
    return result

def get_my_sql(num,para):
    if num=="0":
        sql = "select * from my_main_customer"
    elif num=="1":
        sql = "select * from my_main_employee"
    elif num=="2":
        sql = "select * from my_main_consume"
    elif num=="3":
        sql = "select seat.SeatNum,seat.SeatRow,seat.SeatLine,house.HouseName,customer.CusName " \
              "from my_main_movieseat as seat,my_main_moviehouse as house,my_main_customer as customer " \
              "WHERE seat.SeatHouse_id=house.HouseNum AND seat.SeatCustomer_id=customer.CusNum"
    elif num=="4":
        sql = "select * from my_main_moviehouse"
    elif num=="5":
        sql = "select * from my_main_store"
    elif num=="6":
        sql = "select * from my_main_supplier"
    elif num=="7":
        sql = "select * from my_main_movie"
    elif num=="8":
        sql = "select * from my_main_moviesupplier"
    elif num=="9":
        sql = "select * from my_main_goods"
    elif num =="00":
        sql = "select * from my_main_customer where CusName='"+para+"'"
    elif num=="01":
        sql = "select CusName,CusNum,ConsumeNum,ConsumeAmount,ConsumeType from my_main_customer as customer,my_main_consume as consume WHERE consume.Consumer_id =customer.CusNum AND customer.CusNum="+para
    elif num=="02":
        sql = "select CusName,CusNum,SeatNum,SeatLine,SeatRow,HouseName,HouseNum from my_main_customer as customer,my_main_movieseat AS movieseat,my_main_moviehouse WHERE SeatCustomer_id=CusNum AND HouseNum=SeatHouse_id AND CusNum="+para
    elif num=="10":
        sql = "select * from my_main_employee WHERE EmploeeName='"+para+"'"
    elif num=="20":
        sql = "select * from my_main_consume WHERE ConsumeNum="+para
    elif num=="30":
        sql = "select * from my_main_movieseat,my_main_customer,my_main_moviehouse WHERE SeatHouse_id=HouseNum AND SeatCustomer_id=CusNum AND SeatNum="+para
    elif num=="40":
        sql = "select * from my_main_moviehouse WHERE HouseName='"+para+"'"
    elif num=="41":
        sql = "select HouseNum,HouseName,MovieNum,MovieName,MovieProductor,MovieRank from my_main_movie,my_main_moviehouse,my_main_movie_moviehouse WHERE movie_id=my_main_movie.MovieNum AND moviehouse_id=HouseNum AND HouseNum="+para
    elif num=="42":
        sql = "select HouseNum,HouseName,EmploeeNum,EmploeeName,EmploeeDuty,EmploeeSex from my_main_employee,my_main_moviehouse WHERE HouseEmployee_id=EmploeeNum AND HouseNum="+para
    elif num=="50":
        sql = "select * from my_main_store WHERE StoreName='"+para+"'"
    elif num=="51":
        sql = "select StoreNum,StoreName,SupplierNum,SupplierName,SupplierConnect from my_main_store,my_main_supplier,my_main_supplier_supplyconsume WHERE supplier_id=SupplierNum AND store_id=my_main_store.StoreNum AND StoreNum="+para
    elif num=="52":
        sql = "select StoreNum,StoreName,EmploeeNum,EmploeeName,EmploeeDuty,EmploeeSex from my_main_store,my_main_employee WHERE StoreEmployee_id=EmploeeNum AND StoreNum="+para
    elif num=="53":
        sql = "select StoreNum,StoreName,GoodsNum,GoodsName,GoodsPrice from my_main_goods,my_main_store WHERE GoodsStore_id=StoreNum AND StoreNum="+para
    elif num=="60":
        sql = "select * from my_main_supplier WHERE SupplierName='"+para+"'"
    elif num=="61":
        sql = "select SupplierNum,SupplierName,SupplierConnect,GoodsNum,GoodsName,GoodsPrice from my_main_supplier,my_main_goods WHERE GoodsSupplier_id=SupplierNum AND SupplierNum="+para
    elif num=="70":
        sql = "select * from my_main_movie WHERE MovieName='"+para+"'"
    elif num=="71":
        sql = "select MovieNum,MovieName,HouseNum,HouseName,HousePlace from my_main_movie,my_main_movie_moviehouse,my_main_moviehouse WHERE moviehouse_id=HouseNum AND movie_id=MovieNum AND MovieNum="+para
    elif num=="72":
        sql = "select MovieNum,MovieName,SupplierNum,SupplierName,SupplierConnect from my_main_movie,my_main_moviesupplier WHERE MovieSupp_id=SupplierNum AND MovieNum="+para
    elif num=="80":
        sql = "select * from my_main_supplier WHERE SupplierName='"+para+"'"
    elif num=="81":
        sql = "select SupplierNum,SupplierName,MovieNum,MovieName,MovieRank,MovieProductor from my_main_supplier,my_main_movie WHERE MovieSupp_id=SupplierNum AND SupplierNum="+para
    elif num=="90":
        sql = "select * from my_main_goods WHERE GoodsName='"+para+"'"
    elif num=="91":
        sql = "select * from my_main_goods,my_main_store WHERE GoodsStore_id=StoreNum AND GoodsNum="+para
    elif num=="92":
        sql = "select * from my_main_goods,my_main_supplier WHERE GoodsSupplier_id=SupplierNum AND GoodsNum="+para
    else:
        sql = "error"
    return sql