from rest_framework import serializers

from training_system_app.models import Product, UserGroup


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    user_groups = UserGroupSerializer(many=True, read_only=True, source='product')

    class Meta:
        model = Product
        fields = ('pk', 'name', 'creator', 'start_date_time', 'price', 'user_groups')
