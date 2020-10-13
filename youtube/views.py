from django.shortcuts import render, redirect
from .forms import VideoForm, CommentForm
from .models import User, Video, Comment
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def home(request):
    videos = Video.objects.order_by('-date_created')[:4]
    
    context = {'videos':videos}
    return render(request, 'youtube/index.html', context)

def video_view(request, pk):
    video = Video.objects.get(id = pk)
    user = request.user
    #print(user)
    
    comment = CommentForm()      
    #video path
    video_path = video.path

    #load comments
    comments = Comment.objects.order_by('date_created').filter(video = video)
      
    context = {'video':video, 'comment_form':comment, 'user': user, 'video_path':video_path, 'comments':comments}
    return render(request, 'youtube/video.html', context)

def new_video(request):
    if request.user.is_authenticated == False:
        return redirect('/login')
        
    if request.user.is_staff:
        print('This person is a staff')
        form = VideoForm()

        if request.method == 'POST':
            # print(request.POST)
            # print(request.FILES)
            form = VideoForm(request.POST, request.FILES)
        
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                path = form.cleaned_data['path']
                print(path)
                new_video = Video.objects.create(user = request.user, title = title, description = description, path = path)

                new_video.save()
                
                return HttpResponseRedirect('/home')
     
        context = {'videoform': form}
        return render(request,'youtube/new_video.html',context)
    else:
        return redirect('/video/home')

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/video/home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        
        user = authenticate(username = username, password = password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/video/home')
        else:
            return HttpResponse('Error')
    context= {}
    return render(request,'youtube/login.html',context)

def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        return redirect('/video/login')
    return redirect('/video/login')

def register(request): 
    if request.user.is_authenticated:
        print("You are logged in. Redirecting to home page.")
        return redirect('/video/home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(email = email):
                print('email exists')
            else:
                if User.objects.filter(username = username):
                    print('username exists')
                else:
                    user = User.objects.create_user(username = username, password = password1, email = email)

                    user.save()

                    return redirect('/video/login')
        else:
            print('password not equal')
            return redirect('/register')


    context = {}
    return render(request,'youtube/register.html',context)

def comments(request):
    if request.method == 'POST':
        video_id = request.POST['video']
        print(video_id)
        text = request.POST['text']
        video = Video.objects.get(id = video_id)

        comment = Comment.objects.create(user = request.user, video = video, text = text)

        comment.save()

        return HttpResponseRedirect(reverse('youtube:video', args = [video_id]))


        