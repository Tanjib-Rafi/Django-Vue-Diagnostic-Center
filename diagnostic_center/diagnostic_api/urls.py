# from django.urls import path
from django.urls import path
from .views import PatientEntry, getPatient, getTest,editTest,updateTest,createTest,deleteTest
# from rest_framework.routers import DefaultRouter

app_name = 'diagnostic_api'

# router = DefaultRouter()

# router.register('getTest', TestList, basename='test')

# urlpatterns = router.urls


urlpatterns = [
    #Test Entry
    # path('<int:pk>/', TestDetail.as_view(), name='detailcreate'),
    path('getTest/', getTest.as_view(), name='getTest'),
    path('editTest/<int:pk>', editTest.as_view(), name='editTest'),
    path('createTest', createTest.as_view(), name='createTest'),
    path('updateTest/<int:pk>', updateTest.as_view(), name='updateTest'),
    path('deleteTest/<int:pk>', deleteTest.as_view(), name='deleteTest'),

    #Patient Entry
    path('PatientEntry', PatientEntry.as_view(), name='patiententry'),
    path('getPatient/', getPatient.as_view(), name='getPatient'),
]