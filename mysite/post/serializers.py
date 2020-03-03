from rest_framework import serializers
from .models import Post


#
# class Post(models.Model):
#     author = models.ForeignKey('account.User', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)
#


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.IntegerField(required=False)
    title = serializers.CharField(required=True, allow_blank=False, max_length=200)
    text = serializers.CharField(required=False, allow_blank=True)
    published_date = serializers.DateTimeField(required=False, allow_null=True)

    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Post` instance, given the validated data.
        """
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('text', instance.text)
        instance.code = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance
