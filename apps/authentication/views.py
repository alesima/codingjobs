from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignupForm
from apps.models.UserProfile import UserProfile


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'jobseeker')

            userprofile = UserProfile.objects.create(
                user=user, is_employer=True if account_type == 'employer' else False)
            userprofile.save()

            login(request, user)

            return redirect('index')
        else:
            msg = 'Form is not valid'
    else:
        form = SignupForm()
    return render(request, 'accounts/register.html', {'form': form, 'msg': msg, 'success': success})
