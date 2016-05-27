#coding:utf8

from rest_framework import serializers
from snippets.models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES

#class SnippetSerializer(serializers.Serializer):
class SnippetSerializer(serializers.ModelSerializer):
#	pk = serializers.IntegerField(read_only=True)
#	title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#	code = serializers.CharField(style={'base_template':'textarea.html'})
#	linenos = serializers.BooleanField(required=False)
#	language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,default='python')
#	style = serializers.ChoiceField(choices=STYLE_CHOICES,default='friendly')
	
	#def create(self, validated_date):
		#create and return a new snippet instance 
	#	return Snippet.objects.create(**validated_date)

	#def update(self, instance, validated_data):
		#update and return a existing 'snippet' instance
	#	instance.title = validated_data.get('title', instance.title)
	#	instance.code = validated_data.get('code', instance.code)
	#	instance.linenos = validated_data.get('linenos', instace.linenos)
	#	instance.language = validated_data.get('langeuage', instance.langeuage)
	#	instance.style = validate_data.get('style', instance.style)
	#	instance.save()
	#	return instance
	class Meta:
		model = Snippet
		fields = ('id','title','code','linenos','language','style')
