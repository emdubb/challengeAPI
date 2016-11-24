from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'fname', 'lname', 'profile_url')

    def create(self, validated_data):
        # Create and return a new 'User' instance, given the validated data
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update and return an existing 'User' instance, give the validated data.
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.fname = validated_data.get('fname', instance.fname)
        instance.lname = validated_data.get('lname', instance.lname)
        instance.profile_url = validated_data.get('profile_url', instance.profile_url)
        instance.save()
        return instance
