from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserRegisterSerializer,UserSerializer,UserUpdateSerializer
from users.models import User

class RegisterView(APIView):
    def post(self,request):
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# solo para los usuarios que esten logiados  podron ejecutar la petision
class UserView(APIView):
    permission_classes=[IsAuthenticated]

    # vamos hacer un overrasi del usuario
    def get(self,request):
        serializer=UserSerializer(request.user)
        return Response(serializer.data)
    # vamos a actualizar los datos del usaurio
    def put(self,request):
        # primero que hago es obtener le id del usuario
        # request.user.id
        user=User.objects.get(id=request.user.id)
        # con el serializador le vamos a decir al usuario que datos va poder actualizar
        serializer=UserUpdateSerializer(user,request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





