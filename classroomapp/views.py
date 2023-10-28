from django.shortcuts import render
from .models import Teacher,Classroom,Mission,Student,Mission_Log
from rest_framework import generics
from .serializers import TeacherSerializer , ClassSerializer , StudentSerializer , MissionSerializer , MissionLogSerializer,UserRegistrationSerializer
from django.contrib.auth.views import LoginView
import django_filters.rest_framework
from django.contrib.auth.models import  User
from rest_framework.views import APIView

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import RegisterSerializer

from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
# ใช้อันนี้

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise serializers.ValidationError({"password": "Password fields didn't match."})
    #     else:
    #         print('ok')

    #     return attrs

    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username=validated_data['username'],
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name']
    #     )

        
    #     user.set_password(validated_data['password'])
    #     user.save()

    #     return user




# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            user_id = user.id
            return Response({'token': token.key , 'user_id':user_id}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)









# Create your views here.


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
@permission_classes([IsAuthenticated])
class ClassroomView(generics.ListCreateAPIView):
    # queryset = Classroom.objects.all()
    serializer_class = ClassSerializer

    filterset_fields = ['class_name','teacher']

    def get_queryset(self):
        user = self.request.user.id
        print(user)
        return Classroom.objects.filter(teacher=user)



class TeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Replace with your login template



class ClssDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassSerializer



class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['class_name','class_name__class_code']


    


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class MissionView(generics.ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    filterset_fields = ['class_mission']

class MissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class MissionLogView(generics.ListCreateAPIView):
    queryset = Mission_Log.objects.all()
    serializer_class = MissionLogSerializer

    filterset_fields = ['id','student','status','mission','classroom']
    
class MissionLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mission_Log.objects.all()
    serializer_class = MissionLogSerializer

# def login_view(request):
#     if request.method == 'POST':
        
#         form = AuthenticationForm(request, data=request.POST)
#         print(form)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
            
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('profile')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('profile')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

# def logout_view(request):
#     logout(request)
#     return redirect('login')