from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework import status


@api_view(['POST'])
def registerUser(request):
	try:
		# Fetch input data
		username = request.data['username']
		password = request.data['password']
		email = request.data['email']
		
		user = User.objects.filter(username= username)
		
		# If any user is found, it means passed username already is in use
		if len(user) > 0:
			return Response({"message" : "user already exists"},status=status.HTTP_401_UNAUTHORIZED)
		
		try:
			# Create new user and its token
			user = User(username= username, email= email, password= password)
			User.full_clean(user)
			user.save()
			
			token = Token.objects.get_or_create(user=user)
					
			return Response({"message" : "success"}, status=status.HTTP_201_CREATED)
		
		except Token.DoesNotExist:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	
	except Exception as e:
		return Response({"message" : str(e)}, status=status.HTTP_400_BAD_REQUEST)
	


@api_view(['POST'])
def loginUser(request):	
	try:
		# Fetch input data
		username = request.data['username']
		password = request.data['password']
		
		user = authenticate(username= username, password= password)
		
		# If credentials are incorrect, return error
		if user is None:
			return Response(status=status.HTTP_401_UNAUTHORIZED)
		
		try:
			# Fetch token for user
			token = Token.objects.get(user=user)
			return Response({"token" : token.key})
		
		except Token.DoesNotExist:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	
	except:
		return Response(status=status.HTTP_400_BAD_REQUEST)