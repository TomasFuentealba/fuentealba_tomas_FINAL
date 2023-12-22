from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404
from .models import Inscrito, Institucion
from .serializers import InscritoSerial, InstitucionSerial
from fuentealba_tomas_app.forms import FormInscrito, FormInstitucion
from django.http import JsonResponse

def main(request):
    return render(request, 'main.html')

def datospersonalesview(request):
    alumno = {
        'id' : 1,
        'nombre' : 'Tomas Fuentealba',
        'email' : 'tomas.fuentealba03@inacapmail.cl',
        'asignatura' : 'Backend'
    }
    return JsonResponse(alumno)

class InscritoListClass(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerial(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscritoSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InscritoDetailClass(APIView):
    def get_object(self, pk):
        try:
            return Inscrito.objects.get(pk=pk)
        except Inscrito.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        inscrito = self.get_object(pk)
        serializer = InscritoSerial(inscrito)
        return Response(serializer.data)

    def put(self, request, pk):
        inscrito = self.get_object(pk)
        serializer = InscritoSerial(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inscrito = self.get_object(pk)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Function Based Views
@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerial(instituciones, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = InstitucionSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detail(request, pk):
    try:
        institucion = Institucion.objects.get(pk=pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InstitucionSerial(institucion)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = InstitucionSerial(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def listadoInscritos(request):
    inscritos = Inscrito.objects.all()
    data = {'inscrito': inscritos}
    return render(request, 'inscritos.html', data)

def agregarInscrito(request):
    form = FormInscrito()

    if (request.method == 'POST'):
        form = FormInscrito(request.POST)
        if (form.is_valid()):
            form.save()
            return main(request)
  
    data = {'form': form,'ins':'inscrito'}
    return render (request, 'agregar.html', data)


def agregarInstitucion(request):
    form = FormInstitucion()

    if (request.method == 'POST'):
        form = FormInstitucion(request.POST)
        if (form.is_valid()):
            form.save()
            return main(request)
  
    data = {'form': form,'ins':'institucion'}
    return render (request, 'agregar.html', data)