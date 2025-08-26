from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Task, Person, Date
from .serializers import TaskSerializer, PersonSerializer, DateSerializer
from django.http import JsonResponse


def api(request) :
    return JsonResponse(
        {'message' : 'Hold on'}
    )


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [ SearchFilter]
    filterset_fields = ['type', 'is_completed' , 'task_time' , 'task_name']
    search_fields = ['type']

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class PersonListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'email']

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class DateListCreate(generics.ListCreateAPIView):
    queryset = Date.objects.all()
    serializer_class = DateSerializer

class DateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Date.objects.all()
    serializer_class = DateSerializer

class AllDateView(generics.ListAPIView):
    queryset = Date.objects.all()
    serializer_class = DateSerializer
