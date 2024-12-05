from django.shortcuts import render
from users.models import Users
from users.serializer import UserSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render,get_object_or_404


# Create your views here.
@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UserSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)

    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data = users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data,status = status.HTTP_201_CREATED)

        return JsonResponse(users_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_details(request,pk):
    try:
        user = Users.objects.get(pk = pk)
    except Exception as e:
        return JsonResponse({"Message": str(e)},status = status.HTTP_404_NOT_FOUND)

    try:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data)
        
        elif request.method == 'PUT':
            user_data = JSONParser().parse(request)
            user_serializer = UserSerializer(user, data = user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data,status = status.HTTP_201_CREATED)
            return JsonResponse(users_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            user.delete()
            return JsonResponse({"message":"Deleted Successfuly"},status = status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return JsonResponse({"message":str(e)},status = status.HTTP_404_NOT_FOUND)

#validate user
@api_view(['POST'])
def validate_user(request):
    try:
        user_data = JSONParser().parse(request)
        # user_serializer = UserSerializer(data = user_data)
        users = Users.objects.all()
        # users_serializer = UserSerializer(users,many=True)
        print(user_data)
        print(users[0].email)
        for user in users:

            if user_data['email'] == user.email and user_data['password'] == user.password:
                return JsonResponse({"Message":"Found, User Exist"})
        
        return JsonResponse({"Message":"Not Found, User Does not Exist"})

    except Exception as e:
        return JsonResponse({"Message":str(e)})
