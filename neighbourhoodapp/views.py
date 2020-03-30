from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm,ProfileUpdateForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from . models import Profile,Post,Neighbourhood,Business
from .forms import postForm,neighbourhoodform,businessform


from django.contrib.auth.decorators import login_required

@login_required
def posted(request):
    nei=Neighbourhood.allimages()
    return  render(request,'index.html',{"nei":nei})

@login_required
def home(request):
    if request.user.is_authenticated:
        nei = Neighbourhood.allimages()
        return render(request,'index.html',{"nei":nei})
    else:
        return  redirect('/auth/login')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Neighbourhood account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request,'confirm.html')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request,'confirmed.html')
    else:
        return HttpResponse('Activation link is invalid!')



@login_required
def updatemyprofile(request):
    current_user = request.user
    try:
        myprofile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST,request.FILES)

            if form.is_valid():
                myprofile.profile_photo = form.cleaned_data['profile_photo']
                myprofile.bio = form.cleaned_data['bio']
                myprofile.username = form.cleaned_data['username']
                myprofile.save_profile()
                return redirect(home)
        else:
            form = ProfileUpdateForm()
    except:
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST,request.FILES)

            if form.is_valid():
                createprofile= Profile(profile_photo= form.cleaned_data['profile_photo'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'],user = current_user)
                createprofile.save_profile()
                return redirect(home)





        else:
            form = ProfileUpdateForm()


    return render(request,'createprofile.html',{"current_user":current_user,"form":form})



@login_required
def comment(request, image_id):
    comments = Post.objects.filter(neighbourhood=image_id)
    current_image = Neighbourhood.objects.get(id=image_id)
    current_user = request.user


    if request.method == 'POST':

        form = postForm(request.POST,request.FILES)


        if form.is_valid():
            comment = form.save(commit=False)
            comment.user=current_user
            comment.neighbourhood = current_image


            current_image.save_image()
            comment.save()
            return redirect('updates',image_id)
    else:
        form = postForm()
    return render(request, 'posted.html', {"form": form, "comments": comments})

@login_required
def myprofile(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(user_id=current_user)

    except:
        profile = Profile.objects.filter(user_id=current_user)

    return render(request, 'profile.html',{"profile": profile, "current_user": current_user})

@login_required
def neighbourhhod(request):

    if request.method == 'POST':
        form=neighbourhoodform(request.POST , request.FILES)
        if form.is_valid():
            createprofile = Neighbourhood(name=form.cleaned_data['name'], location=form.cleaned_data['location'],occupants=form.cleaned_data['occupants'],)
            createprofile.save_image()
        return redirect(home)
    else:
        form=neighbourhoodform()
    return  render(request,'createneighbourhood.html',{"form":form})



def business(request, image_id):
    business = Business.objects.filter(neighbourhood=image_id)
    current_image = Neighbourhood.objects.get(id=image_id)
    current_user = request.user
    if request.method == 'POST':
        form = businessform(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.neighbourhood = current_image

            current_image.save_image()
            comment.save_business()
            return redirect(home)
    else:
        form = businessform()
    return render(request, 'createbusiness.html', {"form": form,"business":business})

@login_required
def updates(request, image_id):
    updates = Post.objects.filter(neighbourhood=image_id)
    business= Business.objects.filter(neighbourhood=image_id)
    hood = Neighbourhood.objects.get(id=image_id)
    return  render(request,'updates.html',{'updates':updates,'hood':hood,"business":business})

@login_required
def get_business(request, image_id):

    business= Business.objects.filter(neighbourhood=image_id)
    return  render(request,'business.html',{"business":business})


def search_business(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term=request.GET.get("name")
        searchednames=Business.findbusiness(search_term)
        message=f"{search_term}"
        return render(request,"search.html",{"message":message,"searched":searchednames})

    else:
        message="you haven't searched"
    return render(request,"search.html",{"message":message})









# Create your views here.
