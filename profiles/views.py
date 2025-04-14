from django.shortcuts import render
from profiles.models import Profile


def index(request):
    """
    Display a list of profiles.

    Retrieves all Profile objects and renders the 'profiles/index.html' template.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered page with the list of profiles.
    :rtype: HttpResponse
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Display the details of a specific user profile.

    Retrieves the Profile object corresponding to the provided username and
    renders the 'profiles/profile.html' template with its details.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param username: The username of the profile to display.
    :type username: str
    :return: The rendered page with the profile details.
    :rtype: HttpResponse
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
