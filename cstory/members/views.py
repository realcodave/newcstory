from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUp, EditProfile, PasswordChangingForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from post.models import Profile

class CreateProfilePageView(generic.CreateView):
	form_class = ProfilePageForm
	template_name = "registration/create_profile.html"
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
	model = Profile
	template_name = "registration/edit_profile_page.html"
	fields = ["bio", "profile_pic", "website_url", "facebook_url", "twitter_url", "instagram_url", "pinterest_url"]
	success_url = reverse_lazy("home")
	

class ShowProfilePageView(generic.DetailView):
	model = Profile
	template_name ="registration/show_profile.html"
	
	def get_context_data(self, *args, **kwargs):
	   	users = Profile.objects.all()
	   	context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
	   	page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
	   	context['page_user'] = page_user
	   	return context

class Passwords(PasswordChangeView):
	form_class = PasswordChangingForm
	success_url = reverse_lazy("password_success")

def passwords_success(request):
	return render(request, 'registration/passwords_success.html', {})

class UserRegisterView(generic.CreateView):
	form_class = SignUp
	template_name = "registration/register.html"
	success_url = reverse_lazy("login")

class UserEditView(generic.UpdateView):
	form_class = EditProfile
	template_name = "registration/edit_profile.html"
	success_url = reverse_lazy("home")
	
	def get_object(self):
		return self.request.user
	
	
	