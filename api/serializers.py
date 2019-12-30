from rest_framework import serializers
from .models import Movie, Comment


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('movie', 'content')


class TopSerializer(serializers.ModelSerializer):

    order = serializers.SerializerMethodField()
    movie_id = serializers.SerializerMethodField()
    rank = 0
    last_comment_count = 0

    class Meta:
        model = Movie
        fields = ('movie_id', 'comments_count', 'order')

    def get_movie_id(self, obj):
        return obj.id

    def get_order(self, obj):
        # qs is ordered by comments count if == 0
        # it means all movies have 0 comments
        if obj.comments_count == 0:
            self.rank = 1
        if not self.last_comment_count == obj.comments_count:
            self.rank += 1
        self.last_comment_count = obj.comments_count
        return self.rank


class MovieInputSerializer(serializers.Serializer):

    title = serializers.CharField()
