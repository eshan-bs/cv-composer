from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from cv_app.models import CurriculumVitae
from cv_app.serializers import CustomTokenObtainPairSerializer, CurriculumVitaeSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CurriculumVitaeViewSet(ModelViewSet):
    queryset = CurriculumVitae.objects.all()
    serializer_class = CurriculumVitaeSerializer
