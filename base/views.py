from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Post
from .forms import AddPostForm, CreateUserForm
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group
@unauthenticated_user
def signinForm(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist!')

        # try:
        #     user = User.objects.get(username=username)
        # except:
        #     messages.error(request, 'User does not exist!')
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home')
        # else:
        #     messages.error(request, 'Username & password does not exist!')

    context = { 'page':page }
    return render(request, 'base/form_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('signin-form')

@unauthenticated_user
def signupForm(request):
    # form = UserCreationForm()
    form = CreateUserForm()
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            user = form.save()
            user.username = user.username.lower()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            # user.save()
            # login(request, user)
            # return redirect('home')
            return redirect('signin-form')
        else:
            messages.error(request, 'something went wrong!')

    return render(request, 'base/form_register.html', {'form': form})

@login_required(login_url='signin-form')
@allowed_users(allowed_roles=['customer', 'admin'])
def homePage(request):
    show_all = Post.objects.all().order_by('-created')
    library = {'show_all':show_all}
    return render(request, 'base/home.html', library)


@login_required(login_url='signin-form')
@allowed_users(allowed_roles=['admin'])
def detailPage(request, pk):
    detail = Post.objects.get(id=pk)
    library = {'detail':detail}
    return render(request, 'base/detail.html', library)

@login_required(login_url='signin-form')
def addPost(request):
    form = AddPostForm()
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    library = {'form':form}
    return render(request, 'base/add_post.html', library)

@login_required(login_url='signin-form')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = AddPostForm(instance=post)
    if request.method == 'POST':
        form = AddPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    library = {'form':form}
    return render(request, 'base/add_post.html', library)

@login_required(login_url='signin-form')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    library = {'postDelete': post}
    return render(request, 'base/delete.html', library)

@login_required(login_url='signin-form')
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    library = {'user':user}
    return render(request, 'base/user_profile.html', library)
    
