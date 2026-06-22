from base.serializers import BaseModelSerializer, ExcludeFields

from ..models import PayType, Worker, WorkerCategory, WorkerDocument


# Worker
class WorkerCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Worker
        exclude = ExcludeFields.exclude


class WorkerListSerializer(BaseModelSerializer):
    class Meta:
        model = Worker
        exclude = ExcludeFields.exclude


class WorkerRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = Worker
        exclude = ExcludeFields.exclude


class WorkerUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = Worker
        exclude = ExcludeFields.exclude


# WorkerCategory
class WorkerCategoryCreateSerializer(BaseModelSerializer):
    class Meta:
        model = WorkerCategory
        exclude = ExcludeFields.exclude


class WorkerCategoryListSerializer(BaseModelSerializer):
    class Meta:
        model = WorkerCategory
        exclude = ExcludeFields.exclude


class WorkerCategoryRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = WorkerCategory
        exclude = ExcludeFields.exclude


class WorkerCategoryUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = WorkerCategory
        exclude = ExcludeFields.exclude


# WorkerDocument
class WorkerDocumentCreateSerializer(BaseModelSerializer):
    class Meta:
        model = WorkerDocument
        exclude = ExcludeFields.exclude


class WorkerDocumentListSerializer(BaseModelSerializer):
    class Meta:
        model = WorkerDocument
        exclude = ExcludeFields.exclude


class WorkerDocumentRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = WorkerDocument
        exclude = ExcludeFields.exclude


class WorkerDocumentUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = WorkerDocument
        exclude = ExcludeFields.exclude
