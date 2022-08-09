from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('articles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Korisničko ime ne postoji')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('articles')
        else:
            messages.error(request, 'Korisničko ime ILI šifra nisu tačno uneseni')
    
    return render(request, 'users/login.html')


def logoutUser(request):
    logout(request)
    messages.error(request, 'Uspješno ste se odjavili!')
    return redirect('login')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('articles')

    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Profil je napravljen!')

            login(request, user)
            return redirect('articles')
        
        else:
            messages.error(request, 'Pojavila se greška prilikom registracije')
    context = {'form': form}
    return render(request, 'users/register.html', context)

