from django.shortcuts import render


# Mi functios
def user_login(request):
    """Login view."""
    return render(request, 'users/login.html')
