from django.http import JsonResponse
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer


def jobs(request):

    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return JsonResponse({'jobs': serializer.data})

def applications(request):

    applications = Application.objects.all()
    serializer = ApplicationSerializer(applications, many=True)
    return JsonResponse({'applications': serializer.data})