from django.contrib import admin
# from  import views

from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Adelphoi API documnetation')
urlpatterns = [
    path('documentation/', schema_view),  # swagger_documentation
    path('list_view/', views.AdelphoiList.as_view()),
    path('result/<pk>/', views.Adelphoi_placement.as_view()),
    path('location/<pk>/', views.Adelphoi_location.as_view()),  # w
    path('update_list/<pk>/', views.AdelphoiResult.as_view()),  # w
    path('program_complete/<pk>/', views.ProgramCompletionLevel.as_view()),  # w
    path('search/', views.ClientList.as_view()),
    path('save',views.saveData)

    # path('program/<pk>/',views.Adelphoi_program.as_view()), #w
    # path('admins/', views.AdminUpdate.as_view()), #<int:gender>
    # path('test',views.admin_submission),
    # path('locations/<pk>',views.Location_Mapping.as_view()),

]

