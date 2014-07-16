from register.forms import PostForm

__author__ = 'kevin'


def post(request):
    if request.method == "POST":
        # Get the instance of the form filled with the submitted data
        form = PostForm(request.POST)
        # Django validity check
        if form.is_valid():
            input = form.save(commit=False)
            input.user = User.objects.get(id=request.user.pk)
            input.save()
            last_post = list(Post.objects.filter(user=request.user))[-1]
            # posts.append(last_post)
            # posts.reverse()
            # data = {'form' : form, 'posts': posts, 'last_post':last_post}
            return redirect("/home")


            # Else if the user is looking at the form page
    else:
        form = PostForm()
    return {'postform': form}