from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from apps.job.models import Job
from apps.userprofile.models import UserProfile


def index(request):
    jobs = Job.objects.order_by('-created_at')[:3]
    return render(request, 'core/index.html', {'jobs': jobs})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'jobseeker')

            userprofile = UserProfile.objects.create(
                user=user, is_employer=True if account_type == 'employer' else False)
            userprofile.save()

            login(request, user)

            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})
