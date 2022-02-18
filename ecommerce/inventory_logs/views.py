import logging

from django.shortcuts import HttpResponse, render


def index(request):
    logger = logging.getLogger("loggers")
    message = {
    'message': "user visits index()"
    }
    logger.info(message)
    return HttpResponse("hello")
    