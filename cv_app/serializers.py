# serializers.py
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from cv_app.models import CurriculumVitae


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        token['user_type'] = user.user_type

        return token

class CurriculumVitaeSerializer(ModelSerializer):
    class Meta:
        model = CurriculumVitae
        fields = '__all__'
