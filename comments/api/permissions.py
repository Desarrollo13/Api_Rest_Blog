from rest_framework.permissions import BasePermission
from comments.models import Comment


class IsOwnerOrReadAndCreateOnly(BasePermission):
    # entro en el permiso
    def has_permission(self, request, view):
        if request.method=='GET' or request.method=='POST':
            return True
        else:
            # sino esta intentando actualizar o eliminar
            # primero ontengo el id que esta por eliminar o editar
            id_comment=view.kwargs['pk']
            # tengo que sacar la informacion a quien pertenece ese id
            # petision a la bd para obtener info de ese comentario
            commet=Comment.objects.get(pk=id_comment)

            # obetngo el usuario que esta ejecutando la petision
            id_user=request.user.pk

            # el id del usuario del creador del comentario
            id_user_comment=commet.user_id
            
            # el creador de este comentario
            if id_user==id_user_comment:
                return True
            return False
