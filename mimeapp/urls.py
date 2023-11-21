from django.urls import path
from .views import htmlview,xmlview,excelview
urlpatterns=[
    path("html",htmlview.as_view()),
    path("xml",xmlview.as_view()),
    path("excel",excelview.as_view())
]