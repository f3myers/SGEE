from django.shortcuts import render, get_object_or_404, redirect
from data_models.models import Estrategia

def estra_view(request):
    return render(request, 'estra.html')

def contact_view(request):
    return render(request, 'contactenos.html')

def estrategias_view(request):
    estrat=Estrategia.objects.all()
    return render(request, 'estrategias.html',{'estrategias':estrat})

def eventos_view(request):
    return render(request, 'eventos.html')

def reportes_view(request):
    return render(request, 'reportes.html')

def usuarios_view(request):
    return render(request, 'usuarios.html')

def informacion_profesoral_view(request):
    return render(request, 'informacion_profesoral.html')

def encuestas_view(request):
    return render(request, 'encuestas.html')

def sobrenos_view(request):
    return render(request, 'sobrenos.html')

def testimonials_view(request):
    return render(request, 'testimonials.html')

def formularios_encuestas_view(request):
    return render(request, 'formularios_encuestas.html')

def formulario_estrategia_view(request):
    if request.method == 'POST':
        # Recopilar datos del formulario utilizando los nombres originales
        titulo_estrategia = request.POST.get('titulo-estrategia')  # Nombre en el formulario
        curso = request.POST.get('curso')  # Curso
        anio_escolar = request.POST.get('ano-escolar')  # Año escolar
        grupo = request.POST.get('grupo')  # Grupo

        plan_estudios = request.POST.get('plan-estudios')  # Plan de estudios
        obj_estrategia = request.POST.get('objetivos-estrategia')  # Objetivos de la estrategia
        dir_brigada = request.POST.get('direccion-brigada')  # Dirección de la brigada
        caract_brigada = request.POST.get('caracteristicas-brigada')  # Características de la brigada
        colect_pedagogico = request.POST.get('colectivo-pedagogico')  # Colectivo pedagógico
        otros_aspectos = request.POST.get('otros-aspectos', 'otros_aspectos')  # Otros aspectos (valor por defecto)

        dim_curricular = request.POST.get('dimension-curricular')  # Dimensión curricular
        dim_extensionista = request.POST.get('dimension-extensionista')  # Dimensión extensionista
        dim_politica = request.POST.get('dimension-politico-ideologica')  # Dimensión político-ideológica
        conclusiones = request.POST.get('conclusiones')  # Conclusiones

        obj_general = request.POST.get('objetivo-general')  # Objetivo general
        obj_dc = request.POST.get('objetivos-especificos-curricular')  # Objetivos específicos (curricular)
        plan_dc = request.POST.get('plan-acciones-curricular')  # Plan de acciones (curricular)
        obj_de = request.POST.get('objetivos-especificos-extensionista')  # Objetivos específicos (extensionista)
        plan_de = request.POST.get('plan-acciones-extensionista')  # Plan de acciones (extensionista)
        obj_dp = request.POST.get('objetivos-especificos-politico-ideologica')  # Objetivos específicos (político-ideológica)
        plan_dp = request.POST.get('plan-acciones-politico-ideologica')  # Plan de acciones (político-ideológica)

        evaluacion = request.POST.get('evaluacion-integral')  # Evaluación integral
        autor = request.POST.get('autor')  # Nombre del autor

        # Crear una instancia del modelo Estrategia
        estrategia = Estrategia(
            nombre=titulo_estrategia,  # Mapeo con el modelo
            curso=curso,
            anio_escolar=anio_escolar,
            grupo=grupo,
            plan_estudios=plan_estudios,
            obj_estrategia=obj_estrategia,
            dir_brigada=dir_brigada,
            caract_brigada=caract_brigada,
            colect_pedagogico=colect_pedagogico,
            otros_aspectos=otros_aspectos,
            dim_curricular=dim_curricular,
            dim_extensionista=dim_extensionista,
            dim_politica=dim_politica,
            conclusiones=conclusiones,
            obj_general=obj_general,
            obj_dc=obj_dc,
            plan_dc=plan_dc,
            obj_de=obj_de,
            plan_de=plan_de,
            obj_dp=obj_dp,
            plan_dp=plan_dp,
            evaluacion=evaluacion,
            autor=autor,
        )

        # Guardar la estrategia en la base de datos
        estrategia.save()

        # Redirigir a una página de éxito
        return redirect('estrategias')  # Cambia 'success_page' por la URL de tu página de éxito

    # Renderizar el formulario en caso de que el método sea GET
    return render(request, 'formulario_estrategia.html')
def bien(request):
    return render(request, 'okk.html')
def formulario_eventos_view(request):
    return render(request, 'formulario_eventos.html')

def formulario_usuarios_view(request):
    return render(request, 'formulario_usuarios.html')

def formulario_reporte_view(request):
    return render(request, 'formulario_reporte.html')

def formulario_informacion_pro_view(request):
    return render(request, 'formulario_informacion_pro.html')

def eliminarEstrategia(request, estra_id):
    estra=get_object_or_404(Estrategia, id=estra_id)
    estra.delete()
    return redirect('estrategias')