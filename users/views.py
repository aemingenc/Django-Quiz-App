from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

class RegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
#CreateAPIView clasının içindeki CreateModelMixin classının creat methodunu customize ettik.
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
#seriliazer save yaptığımızda user bilgilerinide bize döndürür bunları user e atadık
        user = serializer.save()
#Bu kullanıcıya göre bir token üret dedik
        token = Token.objects.create(user=user)
#serializer datayı bir değişkene atadık  bir dict şeklindeydi
        data = serializer.data
#data dictimize token isminte bir eleman daha ekledik bunu valueside token.key
        data['token']= token.key
        data['message']= "user successfully added"
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
        