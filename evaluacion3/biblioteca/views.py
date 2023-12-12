from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro, Usuario
from .forms import LibroForm, LoginForm


def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/listar_libros.html', {'libros': libros})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.usuario_registo ="admin"            
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/agregar_libro.html', {'form': form})

def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'biblioteca/editar_libro.html', {'form': form, 'libro': libro})

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    libro.delete()
    return redirect('listar_libros')


#Inicio de sesión
def login(request):
    
    form = LoginForm(request.POST)
    if not form.is_valid():
        print(form.errors)
    
    if request.method == 'POST' and form.is_valid():
        txt_usuario = form.cleaned_data.get('txt_usuario')
        txt_contrasena = form.cleaned_data.get('txt_contrasena')
        try:
            user = Usuario.objects.get(usuario=txt_usuario)
            if user.contrasena == txt_contrasena:
                request.session['autenticado'] = True
                request.session['usuario'] = user.usuario
                return redirect('listar_libros')
            else:
                form.add_error(None, 'Contraseña incorrecta')
        except Usuario.DoesNotExist:
            form.add_error(None, 'Usuario no existe')
    return render(request, 'biblioteca/login.html', {'form': form})
    

#Cerrar sesión
def logout(request):
    request.session.pop('autenticado', None)
    return redirect('/login')