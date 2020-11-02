from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from player.models import Song, Author, Statistic


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    test_field = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Author.objects.filter(pk=instance.id).update(**validated_data)
        return Author.objects.get(pk=instance.pk)


class AuthorSerialzierGet(serializers.Serializer):
    pk = serializers.IntegerField()

    def validate(self, attrs):
        if Author.objects.filter(pk=attrs.get('pk')).exists():
            return attrs
        else:
            raise ValidationError(detail="Object not found")


class StatisticSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    result = serializers.JSONField(required=True)
    email = serializers.EmailField(required=True)
    datetime_create = serializers.DateTimeField(required=False, read_only=True)
    datetime_update = serializers.DateTimeField(required=False, read_only=True)

    def create(self, validated_data):
        return Statistic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.result = validated_data.get('result')
        instance.email = validated_data.get('email')
        instance.save()
        return instance


class StatisticSerializerGet(serializers.Serializer):
    pk = serializers.IntegerField(required=True)

    def validate(self, attrs):
        if Statistic.objects.filter(pk=attrs.get('pk')).exists():
            return attrs
        else:
            raise ValidationError('Statistic not found')

