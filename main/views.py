from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404

# Create your views here.

#first page - signup page
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()

    return render(request,'signup.html',locals())

#landing page - home page
def home_index(request):

    index_images = Image.objects.all()
    forms=CommentForm()
    comments = Comments.objects.all()
    return render(request,'home.html',locals())

#comment view functions
def save_comment(request):

    comment = request.POST.get('comment')
    image_id = request.POST.get('image_id')
    image = get_object_or_404(Image, id=image_id)
    comments = Comments.objects.create(image_id=image,comment=comment)
    return redirect('homePage')

#profile page
def profile_index(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form =UploadForm()

        images = Image.objects.all()
        all_profile = Profile.objects.all()
    return render(request,'profile.html', locals())


def edit(request):
    if request.method == 'POST':
        print(request.FILES)
        new_profile = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if new_profile.is_valid():
            new_profile.save()
            print(new_profile.fields)
            # print(new_profile.fields.profile_picture)
            return redirect('myaccount')
    else:
        new_profile = ProfileForm(instance=request.user.profile)
    return render(request, 'edit.html', locals())

def togglefollow(request, user_id):
    target = get_object_or_404(User, pk=user_id).profile
    request.user.profile.togglefollow(target)
    response = [target.followers.count(),target.following.count()]
    return JsonResponse(response, safe=False)

def like(request, post_id):
    post = get_object_or_404(Image, pk=Image_id)
    request.user.profile.like(post)
    return JsonResponse(post.count_likes, safe=False)

def mine(request):
    images = request.user.profile.posts.all()
    user_object = request.user
    user_images = user_object.profile.posts.all()
    user_saved = [save.photo for save in user_object.profile.saves.all()]
    user_liked = [like.photo for like in user_object.profile.mylikes.all()]
    print(user_liked)
    return render(request, 'myprofile.html', locals())\

