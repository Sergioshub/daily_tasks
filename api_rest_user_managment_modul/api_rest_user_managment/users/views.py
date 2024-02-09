from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from users.models import CustomUser
from users.serializers import CustomUserSerializer, UserContactSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.none()  # Поставил заглушку чтобы список пользователей не был доступен всем.
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({"error": "User creation not allowed for authenticated users"}, status=status.HTTP_403_FORBIDDEN)
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