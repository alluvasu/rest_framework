from rest_framework import serializers
from a1.models import Snippet


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(required=False,max_length=100)
    linenos = serializers.BooleanField(required=False)

    # def create(self , validated_data) :
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Snippet.objects.create ( **validated_data )

    def update(self , instance , validated_data) :
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get ( 'title' , instance.title )
        instance.code = validated_data.get ( 'code' , instance.code )
        instance.linenos = validated_data.get ( 'linenos' , instance.linenos )
        instance.save()
        return instance


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    owner = serializers.ReadOnlyField ( source='owner.username' )

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets','owner']


class SnippetSerializer1(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer1(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']