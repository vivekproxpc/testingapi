from rest_framework import viewsets
from .models import Layout, Section, SectionDetail
from .serializers import LayoutSerializer, SectionSerializer, SectionDetailSerializer
from rest_framework.response import Response

class LayoutViewSet(viewsets.ModelViewSet):
    queryset = Layout.objects.all()
    serializer_class = LayoutSerializer

    def retrieve(self, request, *args, **kwargs):
        layout = self.get_object()
        serializer = self.get_serializer(layout)
        data = serializer.data
        data['slug'] = layout.slug
        data['layout_name'] = layout.layout_name

        return Response(data)

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionDetailViewSet(viewsets.ModelViewSet):
    queryset = SectionDetail.objects.all()
    serializer_class = SectionDetailSerializer
