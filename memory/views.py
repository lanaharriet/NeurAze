from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def memory_home(request):
    return render(request, 'memory/memory.html')
