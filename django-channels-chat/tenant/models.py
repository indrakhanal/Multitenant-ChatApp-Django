from django.contrib.auth.models import User
from django.db.models import (Model, TextField, DateTimeField, ForeignKey, CASCADE)
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
# from tenants.models import TenantAwareModel


class SaveMessageModel(models.Model):
    user = ForeignKey(User, on_delete=CASCADE, verbose_name='user', related_name='user', db_index=True)
    recipient = ForeignKey(User, on_delete=CASCADE, verbose_name='recipient', related_name='receipt', db_index=True)
    timestamp = DateTimeField(auto_now_add=True, editable=False, db_index=True)
    body = TextField('body')

    def __str__(self):
        return str(self.id)

    def characters(self):
        return len(self.body)

    def notify_ws_clients(self):
        notification = {
            'type': 'recieve_group_message',
            'message': '{}'.format(self.id)
        }
        channel_layer = get_channel_layer()
        print("user.id {}".format(self.user.id))
        print("user.id {}".format(self.recipient.id))
        async_to_sync(channel_layer.group_send)("{}".format(self.user.id), notification)
        async_to_sync(channel_layer.group_send)("{}".format(self.recipient.id), notification)

    def save(self, *args, **kwargs):
        new = self.id
        self.body = self.body.strip()  # Trimming whitespaces from the body
        super(SaveMessageModel, self).save(*args, **kwargs)
        if new is None:
            self.notify_ws_clients()

    class Meta:
        app_label = 'tenant'
        verbose_name = 'SaveMessage'
        verbose_name_plural = 'messages'
        ordering = ('-timestamp',)

    auto_create_schema = True
