'''
Created by -> Shivam Devaser
on - > 5-12-2024

created serializer TaskSerializer with fields->
titel(CharField)
description(TextField)
completed(BooleanField)
created_at(auto field of date and time)
'''

from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'completed',
            'created_at'
        )