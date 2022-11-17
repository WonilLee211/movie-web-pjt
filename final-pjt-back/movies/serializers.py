from .models import Movie, Genre, WorldcupRecommend
from rest_framework import serializers
        

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

# MovieSerializer에 역참조될 serializer
class NestedGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre_id', 'name',)

class MovieSerializer(serializers.ModelSerializer):
    genres = NestedGenreSerializer(many=True, read_only=True) # 조회될 때 장르 보내기

    class Meta:
        model = Movie
        fields = '__all__'

# 영화별 장르를 movie-genre테이블에 저장하는 시리얼라이저
class GenreMoviegenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = 'movies'


# 월드컵 결과에 따른 추천 시리얼라이져
class WorldcupRecommendSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = WorldcupRecommend
        # fields = "__all__"
        exclude = ('user',)