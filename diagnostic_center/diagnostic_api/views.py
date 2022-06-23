from rest_framework import generics,viewsets
from rest_framework.response import Response
from diagnostic.models import Test,Patient
from .serializers import TestSerializer,PatientSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Count 

# class TestList(viewsets.ViewSet):
#     queryset = Test.objects.all()
#     def list(self,request):
#         serializer = TestSerializer(self.queryset, many = True)
#         return Response({'columns': serializer.data})




class createTest(generics.CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data['invoice_products'], many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)







# @api_view(['POST'])
# def createTest(request):
#     serializer = TestSerializer(data=request.data['invoice_products'],many = True)

#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)
    
    
# class createTest(APIView):
#     def post(self, request, format=None):
#         serializer = TestSerializer(data=request.data['invoice_products'], many = True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class getTest(generics.ListAPIView):
    queryset = Test.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TestSerializer(queryset, many=True)
        return Response({'columns': serializer.data})


class editTest(generics.RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class updateTest(generics.UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class deleteTest(generics.RetrieveDestroyAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()

# class PatientEntry(generics.CreateAPIView):
#     queryset = Test.objects.all()
#     serializer_class = PatientSerializer
#     def create(self, request, *args, **kwargs):
#     # Check if seats is a list
#         if isinstance(request.data['selected'], list):
#             seats = request.data.pop('selected')
#             models = []
#             for seat in seats:
#                 # validate each model with one seat at a time
#                 request.data['selected'] = seat['id']
#                 serializer = PatientSerializer(data=request.data)
#                 serializer.is_valid(raise_exception=True)
#                 models.append(serializer)
#             # Save it only after all seats are valid. 
#             # To avoid situations when one seat has wrong id 
#             # And you already save previous
#             saved_models = [model.save() for model in models]
#             result_serializer = PatientSerializer(saved_models, many=True)
#             # Return list of tickets
#             return Response(result_serializer.data)
#         # Save ticket as usual
#         serializer = PatientSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

class PatientEntry(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    # def create(self, request):
    #         event = request.data
    #         #sport = event.pop('sport')
    #         selected = event.pop('selected')
    #         #sport = Sport.objects.create(**sport)

    #         for i in selected:
    #             selected.create(**i)
    #         match = Patient.objects.create(**event, market=selected)
    #         return Response(status=status.HTTP_201_CREATED)
# {
# "name":"df",
# "email":"d@gmail.com",
# "age":"21",
# "gender":"Male",
# "phone":"234",
# "total_price":86,
# "advance":0,
# "due":86,
# "selected":[
# {"id":8,"name":"sdf","price":34},
# {"id":9,"name":"dg","price":52}
# ]
# }

    # def create(self, request, *args, **kwargs):
    #     data = request.data

    #     new_student = Patient.objects.create(
    #         name=data["name"], email=data["email"],  age=data['age'], gender=data["gender"], phone=data['phone'], total_price=data['total_price'], advance=data['advance'], due=data['due'])

    #     new_student.save()

    #     for module in data["selected"]:
    #         test_id = Test.objects.get(id=module["id"])
    #         test_name = Test.objects.get(name=module['name'])

    #         new_student.selected.create(test_id,test_name)
    #         #new_student.test_name.add(test_name)

    #     serializer = PatientSerializer(new_student)

    #     return Response(serializer.data)

    # def create(self, request, *args, **kwargs):

    #     new_car = Patient.objects.create(name=request.data['name'],email=request.data['email'],age=request.data['age'],
    #     gender=request.data['gender'],phone=request.data['phone'],total=request.data['total_price'],advance=request.data['advance'],due=request.data['due'],
    #     test_id = [i['id'] for i in request.data['selected']],
    #     test_name=[i['name'] for i in request.data['selected']])

    #     new_car.save()
    #     serializer = PatientSerializer(new_car)
    #     return Response(serializer.data)


# name=request.data['name'],email=request.data['email'],age=request.data['age'],
#         gender=request.data['gender'],phone=request.data['phone'],total_price=request.data['total_price'],advance=request.data['advance'],due=request.data['due'],test_id=[i['id'] for i in request.data['selected']],test_name=[i['name'] for i in request.data['selected']]

class getPatient(generics.ListAPIView):
    queryset = Patient.objects

    def list(self, request):
        queryset = self.get_queryset()
        #queryset =Patient.objects.values('name').annotate(name=Min('name'))
        serializer = PatientSerializer(queryset)
        return Response({'patient': serializer.data})
