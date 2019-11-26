from django.contrib import admin
# from  import views

from django.urls import path
from . import views

urlpatterns = [
    path('insert_data',views.adelphoi_insert,name = 'insert_d'),
    path('CBV',views.CBView.as_view(success_url="/CBV")),
    path('AboutView',views.AboutView.as_view()),
    path('model_test',views.ModelView.as_view(success_url="/model_test"))

]