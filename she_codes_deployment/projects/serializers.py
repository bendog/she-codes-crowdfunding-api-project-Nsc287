from rest_framework import serializers
from django.apps import apps
from .models import Reward, Category, Idol
from django.contrib.auth import get_user_model
# from users.serializers import ProjectProfileSerializer, IdolSerializer

# class RewardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reward
#         fields = ['id', 'amount', 'description']

class PledgeSerializer(serializers.ModelSerializer):
    supporter=serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    category=serializers.ReadOnlyField(source='category.id')
    class Meta:
        model = Category
        fields='__all__'

class IdolSerializer(serializers.ModelSerializer):
    idol=serializers.ReadOnlyField(source='idol.id')

    class Meta:
        model = Idol        #apps.get_model('projects.Idol')
        fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = get_user_model()      
        fields =  ['username']
        

class ProjectSerializer(serializers.ModelSerializer):
    # owner=OwnerSerializer(many=False, read_only=True)
    
    class Meta:
        model = apps.get_model('projects.Project')
        fields = '__all__'
        # fields = ['title', 'description', 
        #     'goal', 'image', 'is_open', 'date_created', 
        #     'deadline', 'category', 'owner', 'pledges']
        

class ProjectDetailSerializer(ProjectSerializer):
    pledges=PledgeSerializer(many=True, read_only=True)
    idol=IdolSerializer(many=False, read_only=True)
    category=CategorySerializer(many=False, read_only=True)

# def update(self, instance, validated_data):
#     instance.title = validated_data.get('title', instance.title)
#     instance.description = validated_data.get('description',
#     instance.description)
#     instance.goal = validated_data.get('goal', instance.goal)
#     instance.image = validated_data.get('image', instance.image)
#     instance.is_open = validated_data.get('is_open', instance.is_open)
#     instance.save()
#     return instance