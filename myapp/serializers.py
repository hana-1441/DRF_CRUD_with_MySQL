from rest_framework import serializers

from .models import ApiData


class Dataserializer(serializers.ModelSerializer):
    text=serializers.CharField(label="Enter any text",max_length=100, required=True)
    
    # def create(self, validated_data):
    #     return ApiData.objects.create(text=validated_data.get('text'))
    
    # def update(self, instance, validated_data):
    #     instance.text=validated_data.get('text',instance.text)
    #     instance.save()
    #     return instance
    
    class Meta:
        model=ApiData
        fields='__all__'