from rest_framework import serializers
from .models import Artist, Song

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
  songs = serializers.HyperlinkedRelatedField(
    view_name='song_detail',
    many=True,
    read_only=True
  )

  class Meta:
    model = Artist
    fields = ('id', 'name', 'photo_url', 'nationality', 'songs')

class SongSerializer(serializers.HyperlinkedModelSerializer):
  artist = serializers.HyperlinkedRelatedField(
    read_only=True,
    view_name='artist_detail'
  )

  class Meta:
    model = Song
    fields = (
      'title',
      'album',
      'preview_url',
      'artist',
    )