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
from . models import Profile


from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
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
                return redirect("/profile/")
        else:
            form = ProfileUpdateForm()
    except:
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST,request.FILES)

            if form.is_valid():
                createprofile= Profile(profile_photo= form.cleaned_data['profile_photo'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'],user = current_user)
                createprofile.save_profile()





        else:
            form = ProfileUpdateForm()


    return render(request,'createprofile.html',{"current_user":current_user,"form":form})



@login_required
def myprofile(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(user_id=current_user)

    except:
        profile = Profile.objects.filter(user_id=current_user)

    return render(request, 'profile.html',{"profile": profile, "current_user": current_user})








# Create your views here.
