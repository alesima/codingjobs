def notifications(request):
    if request.user.is_authenticated:
        return {'notifications': request.user.notifications.filter(is_read=False)}
    return {'notifications': []}
