from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest  # Import HttpRequest
from .models import CustomUser, UserProfile
class UserLog(APIView):
    def post(self, request: HttpRequest):  # Specify the request type
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)

        if user is not None:
            if user.is_superadmin():
                # Super Admin login logic here
                login(request, user)
                return Response({'message': 'Super Admin logged in'}, status=status.HTTP_200_OK)
            elif user.is_admin():
                # Admin login logic here
                login(request, user)
                return Response({'message': 'Admin logged in'}, status=status.HTTP_200_OK)
            elif user.is_user():
                # Regular User login logic here
                login(request, user)
                return Response({'message': 'User logged in'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Incorrect username or password'}, status=status.HTTP_401_UNAUTHORIZED)
#--------------------------------------------
@authentication_classes([])
@permission_classes([IsAuthenticated])
class SuperAdminLogout(APIView):
    def post(self, request):
        # Log out the Super Admin
        logout(request)
        return Response({'message': 'Super Admin logged out'}, status=status.HTTP_200_OK)
    
#--------------------------------------------
class DeleteAdmin(APIView):
    def delete(self, request, admin_id):
        # Delete an admin user
        admin = get_object_or_404(CustomUser, id=admin_id)
        admin.delete()
        return Response({'message': 'Admin deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        
#---------------------------------------------
class ListAdmins(APIView):
    def get(self, request):
        # Get a list of admin users
        admins = CustomUser.objects.filter(role='admin')
        serializer = CustomUserSerializer(admins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
#----------------------------------
class EditAdmin(APIView):
    def put(self, request, admin_id):
        # Edit admin user information
        admin = get_object_or_404(CustomUser, id=admin_id)
        serializer = CustomUserSerializer(admin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#-----------------------------------
class ShowAdmin(APIView):
    def get(self, request, admin_id):
        # Get information of a specific admin user
        admin = get_object_or_404(CustomUser, id=admin_id)
        serializer = CustomUserSerializer(admin)
        return Response(serializer.data, status=status.HTTP_200_OK)