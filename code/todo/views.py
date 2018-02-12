from django.contrib.auth.models import User, Group
from todo.models import TodoItem
from rest_framework import viewsets
from todo.serializers import UserSerializer, GroupSerializer, TodoItemSerializer
from rest_framework import status
from rest_framework.reverse import reverse
# from rest_framework.decorators import list_route
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows todo items to be viewed or edited.
	"""
	queryset = TodoItem.objects.all()
	serializer_class = TodoItemSerializer

	def perform_create(self, serializer):
		instance = serializer.save()  # to get primary key
		instance.url = reverse('todoitem-detail', args=[instance.pk], request=self.request)
		instance.save()

	def delete(self, request):
		TodoItem.objects.all().delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
