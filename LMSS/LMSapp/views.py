from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from nbformat import NBFormatError
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from LMSapp.models import IB,RB,ABB,NAB
from LMSapp.serializers import IBSerializers,RBSerializers,ABBSerializers,NABSerializers

# Create your views here.






@csrf_exempt
def IssueApi(request,id=0):
    if request.method == 'GET':
        Issue_book = IB.objects.filter(Book_id=id)
        Issue_book_serializers= IBSerializers(Issue_book,many = True)
        return JsonResponse(Issue_book_serializers.data, safe = False)
    elif request.method == 'POST':
        Issue_book_data = JSONParser().parse(request)
        Issue_book_serializers =IBSerializers(data=Issue_book_data)
        if Issue_book_serializers.is_valid():
            Issue_book_serializers.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        Issue_book_data = JSONParser().parse(request)
        Issue_book = IB.objects.get(Book_id=Issue_book_data['Book_id'])
        Issue_book_serializers = IBSerializers(Issue_book,data = Issue_book_data)
        if Issue_book_serializers.is_valid():
            Issue_book_serializers.save()
            return JsonResponse("Updated Succesfully",safe=False)
        return JsonResponse("Failed to update")

    elif request.method== 'DELETE':
        Issue_book= IB.objects.get(Book_id = id)
        Issue_book.delete()
        return JsonResponse("Deleted Successfully",safe=False)


    
@csrf_exempt
def ReturnApi(request,id=0):
    if request.method == 'GET':
        Return_book = RB.objects.all()
        Return_book_serializers= RBSerializers(Return_book,many = True)
        return JsonResponse(Return_book_serializers.data, safe = False)
    elif request.method == 'POST':
        Return_book_data = JSONParser().parse(request)
        Return_book_serializers =RBSerializers(data=Return_book_data)
        if Return_book_serializers.is_valid():
            Return_book_serializers.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        Return_book_data = JSONParser().parse(request)
        Return_book = RB.objects.get(Book_id=Return_book_data['Book_id'])
        Return_book_serializers = RBSerializers(Return_book,data = Return_book_data)
        if Return_book_serializers.is_valid():
            Return_book_serializers.save()
            return JsonResponse("Updated Succesfully",safe=False)
        return JsonResponse("Failed to update")
    elif request.method== 'DELETE':
        Return_book= RB.objects.get(Book_id = id)
        Return_book.delete()
        return JsonResponse("Deleted Successfully",safe=False)



@csrf_exempt
def ABApi(request,id=0):
    if request.method == 'GET':
        AB_book = ABB.objects.all()
        AB_book_serializers= ABBSerializers(AB_book,many = True)
        return JsonResponse(AB_book_serializers.data, safe = False)
    elif request.method == 'POST':
        AB_book_data = JSONParser().parse(request)
        AB_book_serializers =ABBSerializers(data=AB_book_data)
        if AB_book_serializers.is_valid():
            AB_book_serializers.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        AB_book_data = JSONParser().parse(request)
        AB_book = ABB.objects.get(Book_id=AB_book_data['Book_id'])
        AB_book_serializers = ABBSerializers(AB_book,data = AB_book_data)
        if AB_book_serializers.is_valid():
            AB_book_serializers.save()
            return JsonResponse("Updated Succesfully",safe=False)
        return JsonResponse("Failed to update")
    elif request.method == 'DELETE':
        AB_book= ABB.objects.get(Book_id = id)
        AB_book.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def NewaddApi(request,id=0):
    if request.method == 'GET':
        Newadd_book = NAB.objects.filter(Book_id=id)
        Newadd_book_serializers= NABSerializers(Newadd_book,many = True)
        return JsonResponse(Newadd_book_serializers.data, safe = False)
    elif request.method == 'POST':
        Newadd_book_data = JSONParser().parse(request)
        Newadd_book_serializers =NABSerializers(data=Newadd_book_data)
        if Newadd_book_serializers.is_valid():
            Newadd_book_serializers.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == 'PUT':
        Newadd_book_data = JSONParser().parse(request)
        Newadd_book = NAB.objects.get(Book_id=Newadd_book_data['Book_id'])
        Newadd_book_serializers = NABSerializers(Newadd_book,data = Newadd_book_data)
        if Newadd_book_serializers.is_valid():
            Newadd_book_serializers.save()
            return JsonResponse("Updated Succesfully",safe=False)
        return JsonResponse("Failed to update")
