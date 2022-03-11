
from dataclasses import fields
from rest_framework import serializers, validators
#model serializer kullancagımız için
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer


class RegisterSerializer(serializers.ModelSerializer):

#emaili zorunlu halegetirdik normalde değildi
    email = serializers.EmailField(
        required = True,
#email fieldeme uniq (tek) yaptık.aynı emailile kayıt olmasınlar die
        validators = [validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
#Sadece yaılsın geri dönmesin alttaki extra_kwards ile aynı sey iki farklı yöntem
        write_only = True,
#zorunlu girilsin
        required = True,
# hazır validate metodu ile valdate ettik
        validators = [validate_password],
#yazarken password * seklinde gözüksün 
         style = {"input_type" : "password"}

    )
    password2 = serializers.CharField(
        write_only = True,
        required = True, 
        style = {"input_type" : "password"}
    )
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password2"
        ]
#User register olduğunda passwordunu response olarak dönmemek için write only yaptık diğerleridöncek
        extra_kwargs = {
            "password": {"write_only" : True},
            "password2": {"write_only" : True},
        }

#User tablomda pasword2 bulunmadığı için direkt olarak ekleyemiyor.
#Bu yuzden gelen datadan password2 yi ayırdık ve kalan veriyi create ettik
    def create(self, validated_data):
#validated_data dan passwordu passworda atadık
        password = validated_data.get("password")
#validated data(gelen data)dan password2 yi cıkardık
        validated_data.pop("password2")
#validate_data yı user diye create ettik
        user = User.objects.create(**validated_data)
#database de hash lenmiş bir sekilde set ettik
        user.set_password(password)
        user.save()
        return user
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password" : "Password fields didn’t match."}
            )
        return data

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","first_name","last_name","email")


class CustomTokenSerializer(TokenSerializer):

#Token tablomun sadece key fieldsı var 
#Token tablomda user diye bir fieldsım olmadıgı için burada tanımladım
#Yukarıda bİR USERSERİALİZER TANIMLADIM VE user e ATADIM

    user = UserTokenSerializer(read_only = True)


    class Meta(TokenSerializer.Meta):
        fields = ("key","user")