from django.contrib.auth.models import User, Group
from strength_standards.quickstart.models import PersonalRecord
from rest_framework import viewsets
from strength_standards.quickstart.serializers import UserSerializer, GroupSerializer, PersonalRecordSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PersonalRecordViewSet(viewsets.ModelViewSet):
    queryset = PersonalRecord.objects.all()
    serializer_class = PersonalRecordSerializer
