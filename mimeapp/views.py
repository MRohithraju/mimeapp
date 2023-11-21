from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
data="""<table><tr><td>ENUMBER</td><td>ENAME</td><td>ESAL</td></tr>
<tr><td>9989</td><td>rohith</td><td>60000.00</td></tr>
<tr><td>7788</td><td>raju</td><td>80000.00</td></tr>
<tr><td>8877</td><td>ravi</td><td>66000.00</td></tr></table>"""
class htmlview(View):
    def get(self,request):
        res=HttpResponse(data,content_type="text/html")
        return  res
class xmlview(View):
    def get(self,request):
        res=HttpResponse(data,content_type="application/xml")
        return res
class excelview(View):
    def get(self,request):
        res=HttpResponse(data,content_type="application/vnd.ms-excel")
        return  res

