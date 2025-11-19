from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def whisper_home(request):
    return render(request, 'whisper/whisper.html')
