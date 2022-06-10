
from email.mime import image
from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth.models import User
# from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from django.http.response import JsonResponse


# Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username", "phone","gender"]


# Serializer to Register User
c_gender=[('male','Male'),('female','Female')]

class RegisterSerializer(serializers.ModelSerializer):

    # email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    # password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(write_only=True, required=True)
    DOB = serializers.DateField(write_only=True, required=True)
    gender  = serializers.ChoiceField(write_only=True, required=True,choices=c_gender)
    image  = serializers.ImageField(write_only=True, required=True)
    # image  = serializers.ImageField(max_length=None, use_url=True,)


    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name', 'phone','DOB','gender','image')
        extra_kwargs = {'first_name': {'required': True}, 'last_name':{'required': True}, 'phone': {'required': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):

        print("🚀 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ validated_data", validated_data)
       
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        CustomUser.objects.create(user=user,phone=validated_data['phone'],DOB=validated_data['DOB'],gender=validated_data['gender'],image=validated_data['image'])
        return user

    def user_detail(request, pk):
     tutorial = User.objects.get(pk=pk)
     print("🚀 ~ file: serializers.py ~ line 64 ~ tutorial", tutorial)
 
     if request.method == 'GET': 
        serializer = UserSerializer(tutorial) 
        return JsonResponse(serializer.data) 

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["phone", "user","DOB","gender","image"]
