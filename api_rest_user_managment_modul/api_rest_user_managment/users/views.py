from rest_framework import viewsets
from users.models import CustomUser
from users.serializers import CustomUserSerializer, CreateUserSerializer, UserContactsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CreateUserViewSet(viewsets.ModelViewSet):
    
    serializer_class = CreateUserSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return CustomUser.objects.filter(id=user_id)
        
    basename = 'customuser'


class UserDetailView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserContactsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)