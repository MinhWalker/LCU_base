from LCU.serializers.serializers import LabelSerializer
from rest_framework.viewsets import ModelViewSet
from LCU.models.label import Label
from base import session

session = session()


class LabelModelViewSet(ModelViewSet):
    serializer_class = LabelSerializer

    def get_queryset(self):
        return session.query(Label).all()
