from django.shortcuts import render, redirect
from .forms import FormContacto
from django.core.mail import EmailMessage

# Create your views here.


def contacto(request):
    if request.method == 'POST':
        form = FormContacto(data=request.POST)
        if form.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')

            email = EmailMessage(
                "Mensaje desde Django",
                f"El usuario con nombre {nombre}, y direccion {email} escribe lo siguiente {contenido}",
                "", ["jaavier808@gmail.com"], reply_to=[email]
            )
            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')
    else:
        form = FormContacto()
        return render(request, "contacto/contacto.html", {
            'form': form
            })