from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from users.models import CustomUser
from users.serializers import CustomUserSerializer, UserContactSerializer
from users.captcha import CaptchaValidator


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.none()
    serializer_class = CustomUserSerializer
    captcha_validator = CaptchaValidator()

    def create(self, request, *args, **kwargs):
        captcha_response = request.data.get('captcha_response')
        success, message = self.captcha_validator.validate_captcha(captcha_response)
        if not success:
            return Response({"error": message}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user 
    

class UserAddressView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = UserContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)