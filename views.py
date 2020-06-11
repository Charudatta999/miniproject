from .models import Entry,UserProfile,Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import  messages
from .forms import Entryform,NewUserFrom,PostForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse,_get_queryset
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User


# HttpResponse('this is joke'),
# Create your views here.
class indexView(ListView):
    model = Entry
    template_name = 'formsa/index.html'


class ArticleDetail(DetailView):
    model = Entry
    context_object_name = 'obj'

    template_name = 'formsa/detail.html'





class post(CreateView):
    model = Entry
    fields = ['title','text','photo']

    template_name = 'formsa/post.html'


def register(request):
    if request.method =="POST":
        form = NewUserFrom(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            user = form.save()
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")

            return redirect("formsa:index")
        else:
            for msg in form.error_messages:
                messages.error(request,f'{msg}:{form.error_messages[msg]}')
    else:
        form = NewUserFrom()
    return render(request, 'formsa/registera.html', {'form': form})
    # context = {"form":form}
    # return render(request,"formsa/registera.html",context)
def logout_request(request):
    logout(request)
    messages.info(request,'logged out successfully!')
    return redirect('formsa:index')

def login_request(request):
    if request.method =="POST":
            form = AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.info(request,f"You are now logged in as {username}")

                return redirect('formsa:post')



            else:messages.error(request,"Invalid Username or password")


    form = AuthenticationForm()

    messages.info(request, 'logged out successfully!')
    return render(request,'formsa/login.html',{"form":form})
@login_required
def post(request):
    if request.method == 'POST':
        aform=Entryform(request.POST or None , request.FILES or None)
        if aform.is_valid():
            aform.save()
            return redirect('formsa:index')
        else:
            for msg in aform.error_messages:
                messages.error(request, f'{msg}:{aform.error_messages[msg]}')
    aform =Entryform()
    return render(request,'formsa/post.html',{'aform':aform})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')

            return redirect('profile')
        else:
            for msg in u_form.error_messages:
                messages.error(request, f'{msg}:{u_form.error_messages[msg]}')
            for msg in p_form.error_messages:
                messages.error(request, f'{msg}:{p_form.error_messages[msg]}')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'formsa/profile.html', context)


