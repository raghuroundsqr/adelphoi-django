from django.contrib import admin
# from  import views

from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Adelphoi API documnetation')
urlpatterns = [
    path('documentation/', schema_view), #swagger_documentation

    path('list_view/',views.AdelphoiList.as_view()),
    path('result/<pk>/', views.Adelphoi_placement.as_view()),
    # path('list_view/<pk>/',views.AdelphoiSubmission.as_view()),#w --not need
    path('location/<pk>/',views.Adelphoi_location.as_view()), #w
    path('update_list/<pk>/',views.AdelphoiResult.as_view()), #w
    path('program_complete/<pk>/',views.ProgramCompletionLevel.as_view()), #w
    path('search/',views.ClientList.as_view()),
    path('admins/', views.AdminUpdate.as_view()), #<int:gender>
    # path('admins/', views.AdminUpdateDetails.as_view()),
    # path('test',views.admin_submission),
    ###
    path('program/<pk>/', views.Adelphoi_program.as_view()),  # w
    path('locations/<pk>',views.Location_Mapping.as_view()),
    path('save',views.saveData),
    ####
    path('test',views.NewAPI_1.as_view()),
    path('test2/<pk>/',views.NewAPI2.as_view()),

    path('Final/',views.Final.as_view()),
    path('music_insert',views.MusicianListView.as_view()),
    path('music_insert/<pk>/',views.MusicianView.as_view()),

    path('list_view/<pk>/',views.UpdateLogic.as_view()),

    path('new/<pk>/',views.UpDate.as_view()),

    path('update_exists_client/<pk>/',views.update_logic)
    ###
    # path('insert_data',views.adelphoi_insert,name = 'insert_d'),
    # path('CBV',views.CBView.as_view(success_url="/CBV")),
    # path('AboutView',views.AboutView.as_view()),
    # path('model_test/',views.ModelView.as_view(success_url="/model_test")),

    # path('list_view/<pk>/<gender>',views.AdelphoiSubmission.as_view()),

]