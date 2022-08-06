from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.contrib.auth.models import Group, User
from api import serializers
from helpdesk import models
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class UserTicketViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return models.Ticket.objects.filter(user=user).order_by('-update_time')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserTicketListSerializer
        else:
            return serializers.UserTicketDetailSerializer


class SupportTicketViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = serializers.SupportTicketDetailSerializer
    permission_classes = (IsAdminUser, )

    def list(self, request, *args, **kwargs):
        if 'status' in request.data:
            status = request.data['status']
            try:
                queryset = models.Ticket.objects.filter(status=status)
            except ValueError:
                return Response({'error': 'Status is incorrect'})
        else:
            queryset = models.Ticket.objects.all()

        serializer = serializers.UserTicketListSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return models.Ticket.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.UserTicketListSerializer
        else:
            return serializers.SupportTicketDetailSerializer


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MessageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        msg = models.Message.objects.filter(ticket__user=user).order_by('-update_time')
        return msg
