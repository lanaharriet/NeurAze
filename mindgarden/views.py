from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def mind_home(request):
    return render(request, 'mindgarden/mindgarden.html')
