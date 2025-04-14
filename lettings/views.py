"""
Views for handling lettings display.
"""

from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """Display a list of lettings.

    Retrieves all Letting objects and renders the 'lettings/index.html' template.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: Rendered template with the list of lettings.
    :rtype: HttpResponse
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Display details for a specific letting.

    Retrieves a Letting object by its ID and renders the 'lettings/letting.html' template with its details.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param letting_id: The unique identifier of the letting to display.
    :type letting_id: int
    :return: Rendered template with details for the specified letting.
    :rtype: HttpResponse
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)