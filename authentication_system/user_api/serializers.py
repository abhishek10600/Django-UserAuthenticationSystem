from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, data):
        user_obj = UserModel.objects.create_user(
            email=data["email"], password=data["password"])
        user_obj.username = data["username"]
        user_obj.save()
        return user_obj


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, data):
        user = authenticate(username=data["email"], password=data["password"])
        if not user:
            raise ValueError("user not found.")
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["email", "username"]
