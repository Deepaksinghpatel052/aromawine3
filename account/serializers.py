from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# User Serializer
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id','first_name','last_name','username', 'email')
        fields = ('id','first_name','last_name', 'email')



class LoginSerializers(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email","")
        password = data.get("password","")
        data["status"] = "0"
        if email and password:
            user = authenticate(username=email,password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                    data["status"] = "1"
                else:
                    mes = "User is not activate."
                    raise exceptions.ValidationError(mes)
            else:
                mes = "Email and password is incorrect & may be your account is not activate."
                raise exceptions.ValidationError(mes)
        else:
            mes = "Must provide email and password"
            raise exceptions.ValidationError(mes)
        return data





class RegistrationSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(style={"inpupt_type":"text"},write_only=True)
    last_name = serializers.CharField(style={"inpupt_type":"text"},write_only=True)
    email = serializers.CharField(style={"inpupt_type":"text"},write_only=True)
    class Meta:
        model  = User
        fields = ['first_name','last_name','email','password']
        eextra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        Userset  = User(
            username = self.validated_data['email'],
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
        fields = ('id',  'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',  'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'])

        return user