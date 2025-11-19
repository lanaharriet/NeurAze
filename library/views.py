from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def library_home(request):
    return render(request, 'library/library.html')
