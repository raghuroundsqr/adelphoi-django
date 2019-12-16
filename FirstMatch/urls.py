from django.contrib import admin
# from  import views

from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Adelphoi API documnetation')
urlpatterns = [
    path('documentation/', schema_view), #swagger_documentation
    path('insert_data',views.adelphoi_insert,name = 'insert_d'),
    path('CBV',views.CBView.as_view(success_url="/CBV")),
    path('AboutView',views.AboutView.as_view()),
    path('model_test/',views.ModelView.as_view(success_url="/model_test")),
    path('list_view/',views.AdelphoiList.as_view()),
    path('list_view/<pk>/',views.AdelphoiSubmission.as_view())

]