from rest_framework import serializers
from api.models import Person , Task , Date

class TaskSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Task
        fields = "__all__"

class DateSerializer(serializers.ModelSerializer) :
    task = TaskSerializer(many=True , read_only=True)
    class Meta :
        model = Date
        fields = "__all__"

class PersonSerializer(serializers.ModelSerializer) :
    date = DateSerializer(many=True , read_only=True)
    class Meta :
        model = Person
        fields = "__all__"