from rest_framework import viewsets, permissions
from .models import InternshipRole, Application
from .serializers import InternshipRoleSerializer, ApplicationSerializer

class InternshipRoleViewSet(viewsets.ModelViewSet):
    queryset = InternshipRole.objects.all()
    serializer_class = InternshipRoleSerializer
    
    # Anyone can view open roles, but only HR (or admins) can create/modify them
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Automatically set the logged-in user as the applicant when creating an application
    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)