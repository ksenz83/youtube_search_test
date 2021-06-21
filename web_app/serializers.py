from rest_framework import serializers
from .models import KeyWordsData, VideoData


class KeyWordsSerializer(serializers.Serializer):
    key_word = serializers.CharField(max_length=64)
    id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return KeyWordsData.objects.create(**validated_data)


class VideoDataSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256)
    id = serializers.IntegerField(required=False)
    url = serializers.CharField(max_length=64)
