"""
Module for the oc_lettings_site views.

This module contains view functions for the oc_lettings_site project.
"""

from django.shortcuts import render


def index(request):
    """
    Render the homepage.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered homepage.
    :rtype: HttpResponse
    """
    return render(request, 'index.html')
