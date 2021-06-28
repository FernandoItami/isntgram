from rest_framework.response import Response
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view



class PostView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['POST',])
def register_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'new user successfully registered'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)