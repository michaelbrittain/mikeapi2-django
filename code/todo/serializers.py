from rest_framework import serializers
from django.contrib.auth.models import User, Group
from todo.models import TodoItem

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.ReadOnlyField()
    class Meta:
        model = Group
        fields = ('url', 'name')

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.ReadOnlyField()
    class Meta:
        model = TodoItem
        fields = ('url', 'id', 'title', 'completed', 'order')

