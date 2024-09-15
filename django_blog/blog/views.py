from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm


def register_view(request):
    error = None
    form = CreateUserForm()
    if request.method == "POST":
      form = CreateUserForm(request.POST)
      if form.is_valid():
        try:
          form.save()
          return redirect("profile")
        except ValidationError as e:
          error = "An error occurred while processing your registration."
      else:
        error = "There are errors in the form. Please correct them."
      
    context = {"form": form, "error": error}
    return render(request, "blog/register.html", context)


def login_view(request):
    error = None
    if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('profile')
      else:
        error = "User not found."
    context = {"error": error}

    return render(request, "blog/login.html", context)

login_required(login_url="register")
def profile_view(request):
    context = {}

    return render(request, "blog/profile.html", context)

login_required(login_url="register")
def edit_profile_view(request):
  user = request.user
  if request.method == "POST":
    new_username = request.POST.get("new_username")
    new_email = request.POST.get("new_email")
    
    if new_username is not None:
      user.username = new_username
    if new_email is not None:
      user.email = new_email
    user.save()
    
    return redirect("profile")
  
  context = {}
  return render(request, "blog/edit_profile.html", context)


class PostListView(ListView):
  model = Post
  template_name = "blog/post_list.html"
  context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
  model = Post
  form_class = PostForm
  template_name = 'blog/post_form.html'
  
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  form_class = PostForm
  template_name = 'blog/post_form.html'

  def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

  def test_func(self):
      post = self.get_object()
      return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')
    template_name = 'blog/post_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

def logout_view(request):
    logout(request)
    return redirect("login")
  
    context = {}
    return render(request, "blog/logout.html", context)
