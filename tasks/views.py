from django.shortcuts import render
from django.http import JsonResponse 
from .models import Tasks
from .serializers import TasksSerializer
from rest_framework import viewsets

# Create your views here.
def hello(request):
    return JsonResponse({'hello': 'world'})


class TasksView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    def get_queryset(self):
        queryset = Tasks.objects.all()


        status = self.request.query_params.get('status',None)
        if status:
            queryset = queryset.filter(status=status)

        return queryset

     