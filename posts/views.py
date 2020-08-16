"""Posts views"""

# Django
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %T hrs'),
        'photo': 'https://picsum.photos/800/600/?image=1036',
    },
    {
        'title': 'Vía Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %T hrs'),
        'photo': 'https://picsum.photos/800/600/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %T hrs'),
        'photo': 'https://picsum.photos/800/600/?image=1076',
    },

]

# Create your views here.
def list_posts(request):
    """List existing posts."""
    return render(request, 'feed.html', {'posts': posts})