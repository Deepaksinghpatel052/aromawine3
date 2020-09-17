from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# User Serializer
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username', 'email')



class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username","")
        password = data.get("password","")

        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data["user"] = user

                else:
                    mes = "User is not activate."
                    raise exceptions.ValidationError(mes)
            else:
                mes = "Username and pasword is incorrect & may be your account is not activate."
                raise exceptions.ValidationError(mes)
        else:
            mes = "Must provide username and password"
            raise exceptions.ValidationError(mes)
        return data





class RegistrationSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(style={"inpupt_type":"text"},write_only=True)
    last_name = serializers.CharField(style={"inpupt_type":"text"},write_only=True)
    email = serializers.CharField(style={"inpupt_type":"text"},write_only=True)
    class Meta:
        model  = User
        fields = ['first_name','last_name','username','email','password']
        eextra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        Userset  = User(
            username = self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email = self.validated_data['email'],
            is_active = True,
        )
        password = self.validated_data['password']
        Userset.set_password(password)
        Userset.save()
        return Userset





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user