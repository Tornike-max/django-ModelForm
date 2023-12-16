from django.shortcuts import redirect, render
from .models import User
from .forms import userForm
# Create your views here.


def list_users(request):
    users = User.objects.all()
    
    return render(request, 'user_list.html',{'users':users})

def add_user(request):
    form = userForm()
    
    if request.method == 'POST':
        form = userForm(request.POST)
        
        if form.is_valid():
            # user = User(**form.cleaned_data)
            # user.save()
            form.save()
            
            return redirect('user-list')
        
            
    return render(request, 'add_user.html', {'form': form})