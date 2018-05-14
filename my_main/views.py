from django.shortcuts import render
from django.http import HttpResponse
import json

from my_main.utils import get_my_sql
from my_main.utils import my_custom_sql

def index(request):
    return render(request,'index.html')
def main_page(request):
    return render(request,'main.html')
def sql_search_page(request):
    return render(request,"sql_search.html")
def select_search_page(request):
    return render(request,"select_search.html")
def idef1x_show(request):
    return render(request,"idef1x_show.html")

def get_sql(request):
    sql = request.GET.get('sql')
    if str(sql).startswith("select"):
        result_json = {"result":my_custom_sql(sql),"code":200}
        return HttpResponse(json.dumps(result_json), content_type='application/json')
    else:
        result_json = {"result":{},"code":400}
        return HttpResponse(json.dumps(result_json), content_type='application/json')

def select_search(request):
    num = request.GET.get("num")
    para = request.GET.get("para")
    sql = get_my_sql(num,para)
    if(sql=="error"):
        result_json = {"code": 500,"result": {}}
        return HttpResponse(json.dumps(result_json),content_type='application/json')
    else:
        result_json = {"code": 200,"result": my_custom_sql(sql)}
        return HttpResponse(json.dumps(result_json), content_type='application/json')
