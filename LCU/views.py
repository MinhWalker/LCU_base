from LCU.serializers.serializers import PartnerSerializer, LabelSerializer, ReleaseSerializer
from rest_framework.viewsets import ModelViewSet
from LCU.models.partner import Partner
from LCU.models.label import Label
from LCU.models.release import Release
from base import session


class PartnerModelViewSet(ModelViewSet):
    serializer_class = PartnerSerializer

    def get_queryset(self):
        return session.query(Partner).all()


class LabelModelViewSet(ModelViewSet):
    serializer_class = LabelSerializer

    def get_queryset(self):
        return session.query(Label).all()


class ReleaseModelViewSet(ModelViewSet):
    serializer_class = ReleaseSerializer

    def get_queryset(self):
        return session.query(Release).all()
