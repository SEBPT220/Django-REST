from rest_framework import serializers
from .models import Artist, Song

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
  songs = serializers.HyperlinkedRelatedField(
    view_name='song_detail',
    many=True,
    read_only=True
  )

  artist_url = serializers.ModelSerializer.serializer_url_field(
    view_name='artist_detail'
  )

  class Meta:
    model = Artist
    fields = ('id','artist_url', 'name', 'photo_url', 'nationality', 'songs')

class SongSerializer(serializers.HyperlinkedModelSerializer):
  artist = serializers.HyperlinkedRelatedField(
    read_only=True,
    view_name='artist_detail'
  )

  artist_id = serializers.PrimaryKeyRelatedField(
    queryset=Artist.objects.all(),
    source='artist'
  )

  class Meta:
    model = Song
    fields = (
      'id',
      'title',
      'album',
      'preview_url',
      'artist',
      'artist_id'
    )