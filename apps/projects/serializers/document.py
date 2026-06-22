from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import Document


class DocumentCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Document
        exclude = ExcludeFields.exclude


class DocumentListSerializer(BaseModelSerializer):
    class Meta:
        model = Document
        exclude = ExcludeFields.exclude


class DocumentRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = Document
        exclude = ExcludeFields.exclude


class DocumentUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = Document
        exclude = ExcludeFields.exclude
