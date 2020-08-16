"""Platzigram views"""

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %T hrs')
    return HttpResponse(f'Oh, hi! Current server time is {str(now)}')


def sorted_numbers(request):
    """Return a json with Sorted numbers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    # import pdb; pdb.set_trace()
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4,),
        content_type='application/json'
    )


def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hello, {name}! Welcome to Platzigram'
    return HttpResponse(message)
