
from rest_framework import viewsets
from .models import User, Caregiver, Member, Address, Job, Job_Application, Appointment
from .serializers import (
	UserSerializer, CaregiverSerializer, MemberSerializer, AddressSerializer,
	JobSerializer, JobApplicationSerializer, AppointmentSerializer
)

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CaregiverViewSet(viewsets.ModelViewSet):
	queryset = Caregiver.objects.all()
	serializer_class = CaregiverSerializer

class MemberViewSet(viewsets.ModelViewSet):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer

class AddressViewSet(viewsets.ModelViewSet):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer

class JobViewSet(viewsets.ModelViewSet):
	queryset = Job.objects.all()
	serializer_class = JobSerializer

class JobApplicationViewSet(viewsets.ModelViewSet):
	queryset = Job_Application.objects.all()
	serializer_class = JobApplicationSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
	queryset = Appointment.objects.all()
	serializer_class = AppointmentSerializer
