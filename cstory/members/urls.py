from django.urls import path
from .views import UserRegisterView,UserEditView, Passwords, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_view
from .views import passwords_success

urlpatterns =[
	path('register/', UserRegisterView.as_view(), name="register"),
	path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
#	path('password/', Passwords.as_view(template_name ="registration/ change_password.html")),
	path('password/', Passwords.as_view(template_name = "registration/change_password.html")),
	path('password_success/', passwords_success, name = "password_success"),
	path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="show_profile_page"),
	path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name="edit_profile_page"),
	path('create_profile_page/', CreateProfilePageView.as_view(), name="create_profile_page"),
]
