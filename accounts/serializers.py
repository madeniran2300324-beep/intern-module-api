from rest_framework import serializers
from .models import InternshipRole, Application

class InternshipRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipRole
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        # We want the applicant field to be read-only so the system automatically assigns 
        # whoever is logged in as the applicant, rather than letting anyone spoof it.
        read_only_fields = ('applicant', 'status', 'submitted_at')