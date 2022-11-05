from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from apps.models.Notification import Notification


@login_required
def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        return redirect(goto, application_id=notification.extra_id)
    return render(request, 'notification/notifications.html')