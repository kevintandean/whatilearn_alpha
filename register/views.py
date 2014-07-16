from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from register.forms import *
# Create your views here.
from registration.forms import RegistrationForm

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#
#     else:
#         form = CustomUserCreationForm()
#
#     return render(request, "registration/registration_form.html", {
#         'form': form,
#     })
@login_required
def edit_profile(request):
    if hasattr(request.user,"profile"):
        return redirect("update_profile")

    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            if form.save():
                return redirect ("home")

    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = ProfileForm(initial={'user':request.user.pk})
    data = {"form": form}
    return render(request, "profile/edit_profile.html", data)

@login_required
def update_profile(request):
    # Similar to the the detail view, we have to find the existing genre we are editing
    profile = Profile.objects.get(user=request.user)

    # We still check to see if we are submitting the form
    if request.method == "POST":
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            if form.save():
                return redirect("/profile/{}".format(request.user.username))

    # Or just viewing the form
    else:
        # We prefill the form by passing 'instance', which is the specific
        # object we are editing
        form = ProfileForm(instance=profile)
    data = {"form": form}
    return render(request, "profile/edit_profile.html", data)

def view_profile(request, username):
    user_id = User.objects.get(username=username).id
    if request.user.username == username:
        print "Yeay"
        if hasattr(request.user,"profile")==False:
            print "Yeay"
            return redirect('edit_profile')


    profile = Profile.objects.get(user=user_id)
    first_name = profile.first_name
    last_name = profile.last_name
    posts=list(Post.objects.filter(user=user_id))
    # tags = Tag.objects.filter(post=1)

    # print tags
    bio = profile.bio
    # if not profile.avatar:
    #     avatar = "/media/avatar/default_avatar.jpg"
    #     #print avatar
    # else:
    #     avatar = profile.avatar.url
    #AVATAR IS SELECTED BY DEFAULT BY CALLING AVATAR_IMAGE_URL (from model)
    avatar = profile.avatar_image_url() #this is a string avatar/60818_10201083718174136_4635851443860706305_n_1.jpg
    cover = profile.cover_image_url()
    #print avatar
    data = {'first_name':first_name,'last_name':last_name, 'bio':bio, 'avatar':avatar, 'username':username, 'posts':posts, 'cover':cover}
    return render(request, "profile/view_profile.html", data)


@login_required
def home(request):
    if hasattr(request.user,"profile")==False:
        print "TESTHOME"
        return redirect("edit_profile")
    #for news feed
    posts = list(Post.objects.order_by('-created')[:20])
    # last_post = list(Post.objects.order_by('?')[:1])
    last_post=list(Post.objects.filter(user=request.user))

    #posting
    if request.method == "POST":
        # Get the instance of the form filled with the submitted data
        form = PostForm(request.POST)
        # Django validity check
        if form.is_valid():
            input = form.save(commit=False)
            input.user=User.objects.get(id=request.user.pk)
            input.save()
            last_post=list(Post.objects.filter(user=request.user))[-1]
            # posts.append(last_post)
            # posts.reverse()
            #data = {'form' : form, 'posts': posts, 'last_post':last_post}
            return redirect("/home")


    # Else if the user is looking at the form page
    else:
        form = PostForm()

    #endposting

    #feed

    data = {'posts': posts, 'last_post':last_post}
    return render(request, "home.html", data)

def landing(request):
    if request.user.is_authenticated():
        return redirect("home")
    else:
        return redirect("registration_register")
   # return render(request, "landing.html")

def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    posts=[post]
    data = {'posts': posts}
    return render(request, "include/view_post.html", data)

    # data = {'first_name':first_name,'last_name':last_name, 'bio':bio, 'avatar':avatar, 'username':username}
    # return render(request, "profile/view_profile.html", data)



