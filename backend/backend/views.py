from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

@permission_classes([IsAuthenticated])
class employesListView(APIView):
    def get(self, request):
        # Check if the user is a Super Admin or Admin to access the list of employee
        if request.user.role in [CustomUser.SUPER_ADMIN, CustomUser.ADMIN]:
            users = UserProfile.objects.all()
            serializer = UserProfileSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response({'detail': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)

#-------------------------------------
