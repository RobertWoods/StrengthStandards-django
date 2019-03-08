from django.contrib.auth.models import User, Group
from strength_standards.personal_records.models import PersonalRecord
from rest_framework import viewsets, permissions
from strength_standards.personal_records.serializers import UserSerializer, PersonalRecordSerializer
from strength_standards.personal_records.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class PersonalRecordViewSet(viewsets.ModelViewSet):
    queryset = PersonalRecord.objects.all()
    serializer_class = PersonalRecordSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
