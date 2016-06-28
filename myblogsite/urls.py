#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

#class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
        	model = User
        	fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    url(r'^', include('snippets.urls')),
    url(r'^common/', include('common.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]
