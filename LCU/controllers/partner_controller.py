from LCU.serializers.serializers import PartnerSerializer
from rest_framework.viewsets import ModelViewSet
from LCU.models.partner import Partner
from base import session

session = session()


class PartnerModelViewSet(ModelViewSet):
    serializer_class = PartnerSerializer

    class Meta:
        model = Partner
        fields = '__all__'

    def get_queryset(self):
        return session.query(Partner).all()