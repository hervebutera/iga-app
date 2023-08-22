from rest_framework import serializers
from account.models import Account

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['firstname', 'lastname', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            firstname=self.validated_data['firstname'], 
            lastname=self.validated_data['lastname'],
            username=self.validated_data['username'], 
            email=self.validated_data['email'],

        ) 
        password = self.validated_data['password']

        account.set_password(password)
        account.save()
        return account
    
    