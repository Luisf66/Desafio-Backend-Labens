from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    
    def validate_term(self, value):
        if value.year < 1900 or value.year > 2100:
            raise serializers.ValidationError("O ano deve estar entre 1900 e 2100.")
        return value
        
    def validate_conclusion(self, value):
        if value.year < 1900 or value.year > 2100:
            raise serializers.ValidationError("O ano deve estar entre 1900 e 2100.")
        return value