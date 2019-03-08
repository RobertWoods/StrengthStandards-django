from django.contrib.auth.models import User, Group
from rest_framework import serializers
from strength_standards.personal_records.models import PersonalRecord

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class PersonalRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalRecord
        fields = ('url', 'exercise', 'weight', 'reps', 'date', 'user')
