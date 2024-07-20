from rest_framework import serializers
from .models import Layout, Section, SectionDetail

class SectionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionDetail
        fields = ['id', 'heading', 'description']

class SectionSerializer(serializers.ModelSerializer):
    details = SectionDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'layout', 'banner_image', 'header', 'content', 'n_content', 'image', 'created_at', 'updated_at', 'deleted_at', 'details']

class LayoutSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True, source='layouts')

    class Meta:
        model = Layout
        fields = ['id', 'layout_name', 'slug', 'sections']
