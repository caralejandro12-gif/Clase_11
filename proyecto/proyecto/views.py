from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime

def saludar(request):
    return HttpResponse("¡Hola, bienvenido a mi sitio web!")


def bienvenido(request, nombre, apellido):
    return HttpResponse(f"¡Bienvenido a mi sitio web {nombre} {apellido}!")


def bienvenido_html(request, nombre, apellido):
    hoy = datetime.datetime.now()
    html_content = f"""
    <html>
        <head>
            <title>Bienvenida</title>
        </head>
        <body>
            <h1>¡Bienvenido a mi sitio web {nombre} {apellido}!</h1>
            <h2>Nos alegra verte aquí.</h2>
            <h3>Esperamos que disfrutes tu visita.</h3>
            <h4>Siéntete como en casa.</h4>
            <p>Estamos encantados de tenerte aquí.</p>
            <p>Fecha y hora de la visita: {hoy}</p>
        </body>
    </html>
    """
    return HttpResponse(html_content)


def bienvenido_tpl(request, nombre, apellido):
    hoy = datetime.datetime.now()
    
    with open("C:/00.Coderhouse/Clase_11/proyecto/proyecto/plantilla/bienvenida.html", "r", encoding="utf-8") as archivo:
        template = Template(archivo.read())
        contexto = Context({"nombre": nombre, "apellido": apellido, "hoy": hoy})
        html_content = template.render(contexto)
        
    return HttpResponse(html_content)

# Lo que acabamos de hacer, es necesario un ajuste en el settings.py
def bienvenido_tpl2(request, nombre, apellido):
    hoy = datetime.datetime.now()
    notas = [4, 3, 6, 7, 8, 9, 10]
    contexto = ({"nombre": nombre, "apellido": apellido, "hoy": hoy, "notas": notas})
    plantilla = loader.get_template("bienvenida2.html")
    respuesta = plantilla.render(contexto)
        
    return HttpResponse(respuesta)