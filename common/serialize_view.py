#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.db import models
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers


def get_model(app_name, model_name):
	cur_model = None
	try:
		cur_model = models.get_model(app_name, model_name)
	except Exception, e:
		raise
	return cur_model
	
def get_serializermodel(cur_model):
	model_fields = tuple([f.name for f in cur_model._meta.fields])
	meta_class = type("Meta", (), {"model":cur_model, "fields":model_fields})
	serialize_model = type("%sSerializer"%cur_model.__name__, (serializers.ModelSerializer,), {"Meta":meta_class}) 
	return serialize_model


class ModelsViewList(APIView):

	def get(self, request, app_name, model_name, format=None):
		cur_model = get_model(app_name, model_name)
		objs = cur_model.objects.all()
		serializer_cls = get_serializermodel(cur_model)
		serializer = serializer_cls(objs, many=True)
		return Response(serializer.data)

	def post(self, request, app_name, model_name, format=None):
		cur_model = get_model(app_name, model_name)
		serializer_cls = get_serializermodel(cur_model)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
