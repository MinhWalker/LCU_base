from LCU.serializers.serializers import ReleaseSerializer
from rest_framework.viewsets import ModelViewSet
from LCU.models.release import Release
from base import session

session = session()


class PartnerModelViewSet(ModelViewSet):
    serializer_class = ReleaseSerializer

    def get_queryset(self):
        return session.query(Release).all()