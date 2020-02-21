from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import SignUpForm
from .models import Post
from django.urls import reverse_lazy


def index(request):
    return render(request, "users/index.html", {})

def signup(request):
    if request.method == "POST":
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username} your account is created successfully!')
            return redirect('users:login')
    else:
        forms = SignUpForm
        return render(request, "users/signup.html", {'forms' : forms})

@login_required
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, "users/home.html", context)

@login_required
def UserProfile(request):
    
    profile = UserProfile
    return render(request, "users/userProfile.html", {"profile" : profile})
# ==================================== CLASS BASED VIEWS =============================================== #

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'users/home.html'        # It looks for the Template <app>_<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'users/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user   # This will set the Author of the post as current logged in User
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'users/post_confirm_delete.html'
    success_url = reverse_lazy('users:home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False