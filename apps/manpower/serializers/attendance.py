from apps.vendor.models.vendor import AttendanceMethodChoices, VendorTypeChoices
from base.serializers import BaseModelSerializer, ExcludeFields, serializers

from ..models import (
    AttendanceLog,
)


class AttendanceLogCreateSerializer(BaseModelSerializer):
    def validate(self, attrs):
        worker = attrs.get("worker")
        group_of_worker = attrs.get("group_of_worker", False)
        total_workers = attrs.get("total_workers")
        vendor = attrs.get("vendor")

        # exactly one mode must be used
        if worker and group_of_worker:
            raise serializers.ValidationError(
                "Provide either 'worker' or set 'group_of_worker' to True, not both."
            )

        if not worker and not group_of_worker:
            raise serializers.ValidationError(
                "Either 'worker' must be provided or 'group_of_worker' must be True."
            )

        # --- Individual worker mode ---
        if worker:
            if vendor:
                raise serializers.ValidationError(
                    "vendor should not be provided when worker is given. It will be derived automatically."
                )  # worker have FK with vendor, independent worker will have vendor as None

            if worker.vendor is None:
                # independent worker — no vendor checks needed
                pass

            else:
                # vendor-assigned worker
                if worker.vendor.type != VendorTypeChoices.LABOUR:
                    raise serializers.ValidationError(
                        "Worker's vendor must be of type 'Labour'."
                    )
                if (
                    worker.vendor.attendance_method
                    != AttendanceMethodChoices.EACH_WORKER_SEPARATELY
                ):
                    raise serializers.ValidationError(
                        "This vendor tracks attendance by 'Count of Workers'. Use group_of_worker instead."
                    )
                # auto-derive vendor from worker
                attrs["vendor"] = worker.vendor

        # --- Group of workers mode ---
        if group_of_worker:
            if not vendor:
                raise serializers.ValidationError(
                    "vendor must be provided when group_of_worker is True."
                )
            # if vendor.type != VendorTypeChoices.LABOUR:
            #     raise serializers.ValidationError(
            #         "Vendor must be of type 'Labour' for group attendance."
            #     )
            if vendor.attendance_method != AttendanceMethodChoices.COUNT_OF_WORKERS:
                raise serializers.ValidationError(
                    "This vendor tracks attendance individually. Use worker instead of group_of_worker."
                )
            if total_workers is None or total_workers <= 0:
                raise serializers.ValidationError(
                    "total_workers must be provided and greater than 0 when group_of_worker is True."
                )

        # total_workers must not be provided for individual mode
        if not group_of_worker and total_workers is not None:
            raise serializers.ValidationError(
                "total_workers should not be provided when group_of_worker is False."
            )

        return attrs

    class Meta:
        model = AttendanceLog
        exclude = ExcludeFields.exclude


class AttendanceLogListSerializer(BaseModelSerializer):
    class Meta:
        model = AttendanceLog
        exclude = ExcludeFields.exclude


class AttendanceLogRetrieveSerializer(BaseModelSerializer):
    class Meta:
        model = AttendanceLog
        exclude = ExcludeFields.exclude


class AttendanceLogUpdateSerializer(BaseModelSerializer):
    class Meta:
        model = AttendanceLog
        exclude = ExcludeFields.exclude
