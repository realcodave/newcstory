from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get("post_id"))
	liked = False
	if post.likes.filter(id = request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse("article-detail",  args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ["-id"]
    
    def get_context_data(self, *args, **kwargs):
    	cat_menu = Category.objects.all()
    	context = super(HomeView, self).get_context_data(*args, **kwargs)
    	context['cat_menu'] = cat_menu
    	
    	return context

class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
    
    def get_context_data(self, *args, **kwargs):
    	cat_menu = Category.objects.all()
    	stuff = get_object_or_404(Post, id=self.kwargs['pk'])
    	total_likes = stuff.total_likes()
    	
    	liked = False
    	if stuff.likes.filter(id = self.request.user.id).exists():
    		liked = True
    	
    	context = super(ArticleView, self).get_context_data(*args, **kwargs)
    	context['cat_menu'] = cat_menu
    	context["total_likes"] = total_likes
    	context["liked"] = liked
    	return context
    

def CategoryView(request, cats):
	cat_menu = Category.objects.all()
	category_posts = Post.objects.filter(category=cats.title())
	return render(request,  'categories.html', {"cats": cats,"category_posts": category_posts, "cat_menu":cat_menu})
	
	   	
class AddCommentView(CreateView):
     model = Comment
     form_class = CommentForm
     #fields = '__all__'
     template_name = 'add_comment.html'
    
     
     def form_valid(self, form):
     	form.instance.post_id = self.kwargs['pk']
     	return super().form_valid(form)

     		
     	   	
	   	
class AddPostView(CreateView):
     model = Post
     form_class = PostForm
     template_name = 'add_post.html'
     success_url = reverse_lazy("home")
     def get_context_data(self, *args, **kwargs):
     	cat_menu = Category.objects.all()
     	context = super(AddPostView, self).get_context_data(*args, **kwargs)
     	context['cat_menu'] = cat_menu
     	return context
   
     #fields = "__all__"
 
 
class AddCategoryView(CreateView):
     model = Category
     #form_class = PostForm
     template_name = 'add_category.html'
     success_url = reverse_lazy("home")
   
     fields = "__all__"
     
     def get_context_data(self, *args, **kwargs):
     	cat_menu = Category.objects.all()
     	context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
     	context['cat_menu'] = cat_menu
     	return context
     	
class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	#fields = ['title', 'title_tag', 'body']
	def get_context_data(self, *args, **kwargs):
	   	cat_menu = Category.objects.all()
	   	context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
	   	context['cat_menu'] = cat_menu
	   	return context
    	
class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')
	def get_context_data(self, *args, **kwargs):
	   	cat_menu = Category.objects.all()
	   	context = super(DeletePostView, self).get_context_data(*args, **kwargs)
	   	context['cat_menu'] = cat_menu
	   	return context