# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .renderers import UserRenderer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


def get_token_for_user(user):
		refresh = RefreshToken.for_user(user)

		return {
			'refresh': str(refresh),
			'access': str(refresh.access_token),
		}


# Define view for user registration
class UserRegistrationView(APIView):
	renderer_classes = [UserRenderer]

	def post(self, request, format=None):
		# create a user registration serializer instance
		serializer = UserRegistrationSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.save()
			token = get_token_for_user(user)
			return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define view for user login 
class UserLoginView(APIView):
	def post(self, request, format=None):
		# create a user login serializer instance
		serializer = UserLoginSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			email = serializer.data.get('email')
			password = serializer.data.get('password')
			user = authenticate(email=email, password=password)
			if user is not None:
				token = get_token_for_user(user)
				return Response({'token':token, 'msg':'Login Successful'}, status=status.HTTP_200_OK)
			return Response({'errors':{'non_field_errors':['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        refresh_token = request.data.get('token')

        if not refresh_token:
            return Response({'detail': 'Refresh token is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            RefreshToken(refresh_token).blacklist()
            return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		

# Define view for user profile
# class UserProfileView(APIView):
# 	renderer_classes = [UserRenderer]
# 	permission_classes = [IsAuthenticated]
# 	def get(self, request, format=None):
# 		# serialize the user profile and return the data
# 		serializer = UserLoginSerializer(request.user)
# 		return Response(serializer.data, status=status.HTTP_200_OK)


# Define a view for changing a user's password
# class UserChangePasswordView(APIView):
	# renderer_classes = [UserRenderer]
	# permission_classes = [IsAuthenticated]
	# def post(self, request, format=None):
	# 	# create serializer for changing user's password
	# 	serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
	# 	context = {'user':request.user}
	# 	if serializer.is_valid(raise_exception=True):
	# 		return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define view for sending a password reset email
# class SendPasswordResetEmailView(APIView):
	# renderer_classes = [UserRenderer]
	# def post(self, request, format=None):
	# 	# Create serializer for sending a password reset email
	# 	serializer = SendPasswordResetEmailSerializer(data=request.data)
	# 	if serializer.is_valid(raise_exception=True):
	# 		return Response({'msg':'Password Reset link send. Please check your Email.'}, status=status.HTTP_200_OK)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Define view for resetting a user's password 
# class UserPasswordResetView(APIView):
	# renderer_classes = [UserRenderer]
	# def post(self, request, user_id, token, format=None):
	# 	# create serializer for resetting user's password
	# 	serializer = UserPasswordResetSerializer(data=request.data, context={'user_id':user_id, 'token':token})
	# 	if serializer.is_valid(raise_exception=True):
	# 		return Response({'msg':'Password Reset Successfully.'}, status=status.HTTP_200_OK)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)