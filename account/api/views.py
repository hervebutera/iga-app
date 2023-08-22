from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token


from account.api.serializers import RegistrationSerializer

@api_view(['POST',])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        account = serializer.save()
        # Response.status_code
        data['response'] = "Successfully registered a new user."
        data['firstname'] = account.firstname
        data['lastname'] = account.lastname
        data['username'] = account.username
        data['email'] = account.email
        token = Token.objects.get(user=account).key
        data['token'] = token

    else:
        data = serializer.errors

    return Response(data, status = status.HTTP_201_CREATED)

