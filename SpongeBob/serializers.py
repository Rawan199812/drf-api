  
from rest_framework import serializers
from .models import  SpongeBob

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpongeBob
        fields = ('id','title','body','author', 'created_at', 'updated_at')
