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

