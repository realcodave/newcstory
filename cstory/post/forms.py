from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for choice in choices:
	choice_list.append(choice)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag","snippet", "author", 'category', "body", "header_img")
        widgets = {
        "title": forms.TextInput(attrs={"class" :"form-control"}),
        "title_tag": forms.TextInput(attrs={"class":"form-control"}),
        "snippet": forms.TextInput(attrs={"class":"form-control", 'placeholder':'Write a short description of your post, story or blog'}),
        "author": forms.TextInput(attrs={"class":"form-control", 'id':'author', 'value':'', 'type':'hidden'}),
      #  "author": forms.Select(attrs={"class":"form-control"}),
         "category": forms.Select(choices =choice_list, attrs={"class":"form-control "}),
        "body": forms.Textarea(attrs={"class":"form-control"}),
        "header_img": forms.FileInput(attrs={"class":"form-control"}),

}

		


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", 'snippet', "author",'category', "body","header_img")
        widgets = {
        "title": forms.TextInput(attrs={"class" :"form-control"}),
        "title_tag": forms.TextInput(attrs={"class":"form-control"}),
        "snippet": forms.TextInput(attrs={"class":"form-control", 'placeholder':'Edit the short description of your post, story or blog'}),
        "author": forms.TextInput(attrs={"class":"form-control", 'id':'author', 'value':'', 'type':'hidden'}),
 #       "author": forms.Select(attrs={"class":"form-control"}),
 		"category": forms.Select(choices =choice_list, attrs={"class":"form-control"}),
        "body": forms.Textarea(attrs={"class":"form-control"}),
        "header_img": forms.FileInput(attrs={"class":"form-control"}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body")
        widgets = {
        "name": forms.TextInput(attrs={"class":"form-control", 'id':'author', 'value':'', 'type':'hidden'}),
        "body": forms.Textarea(attrs={"class":"form-control"}),
}


