# projectname/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('classroom/', views.ClassroomView.as_view()),
    path('teacher/', views.TeacherView.as_view()),
    path('classroom/<int:pk>/', views.ClssDetail.as_view(), name='item-detail'),

    path('student/', views.StudentView.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
    path('mission/', views.MissionView.as_view()),
    path('missionr/<int:pk>/', views.MissionDetail.as_view()),
    path('missionlog/', views.MissionLogView.as_view()),
    path('missionlog/<int:pk>/', views.MissionLogDetail.as_view()),

    # path('register/', views.UserRegistrationView.as_view(), name='register'),
    # path('login/', views.login_view, name='login'),
    path('api/login/', views.LoginView.as_view(), name='api-login'),

    # path('login2/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register2/', views.RegisterView.as_view(), name='auth_register'),
    # path('login2/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    
]