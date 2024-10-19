from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Pelicula
from .forms import PeliculaForm  # Asegúrate de tener un formulario de Pelicula


def index(request):
    return render(request, 'cine/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('peliculas')  # Redirige al listado de películas
        else:
            return render(request, 'cine/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'cine/login.html')

def registro_view(request):
    return render(request, 'cine/registro.html')


def registro_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=email).exists():
                # Si el correo ya está registrado, mostrar error
                return render(request, 'cine/registro.html', {'error': 'El correo ya está registrado'})
            else:
                # Crear nuevo usuario
                user = User.objects.create_user(username=email, password=password)
                user.save()
                # Autenticar y redirigir al login
                login(request, user)
                return redirect('inicio')
        else:
            # Las contraseñas no coinciden, mostrar error
            return render(request, 'cine/registro.html', {'error': 'Las contraseñas no coinciden'})

    return render(request, 'cine/registro.html')

def listado_peliculas(request):
    # Suponiendo que tienes un modelo Pelicula
    peliculas = Pelicula.objects.all()  # Obtener todas las películas
    paginator = Paginator(peliculas, 4)  # 4 películas por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'cine/peliculas.html', {'page_obj': page_obj})

def agregar_editar_pelicula(request, pelicula_id=None):
    if pelicula_id:
        pelicula = get_object_or_404(Pelicula, id=pelicula_id)  # Editar película existente
    else:
        pelicula = None  # Nueva película

    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)  # request.FILES para imágenes
        if form.is_valid():
            form.save()
            return redirect('peliculas')  # Redirigir al listado de películas
    else:
        form = PeliculaForm(instance=pelicula)

    return render(request, 'cine/agregar_editar_pelicula.html', {'form': form})