from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def hub(request):
    # For now we deliver unlocked/locked flags from session or DB later
    rooms = [
        {'name': 'Whisper Hall', 'url': 'whisper:whisper_home', 'locked': False},
        {"name": "Mind Garden", "locked": False, "url": "mindgarden:mind_home"},
        {'name': 'Library Gate', 'url': 'library:library_home', 'locked': False},
        {'name': 'Crystal Notes', 'url': 'crystal:crystal_home', 'locked': False},
        {'name': 'Memory Vault', 'url': 'memory:memory_home', 'locked': False},
    ]
    return render(request, 'hub/hub.html', {'rooms': rooms})

