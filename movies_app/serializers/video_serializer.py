from rest_framework import serializers
from movies_app.models import VideoModel

class VideoSerializer(serializers.ModelSerializer):
    class meta:
        model = VideoModel
        fields = [
            'id',
            'name',
            'key',
            'video_id',
            'site',
            'type',
        ]