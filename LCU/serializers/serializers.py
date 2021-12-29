from rest_framework import serializers
from LCU.models.partner import Partner
from LCU.models.label import Label
from LCU.models.release import Release


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ("id", "name", "description")
        # fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ("id", "code")


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ("id", "version", "note")
