from django.contrib.auth.models import User
from django.db.models import (TextField, ForeignKey, CASCADE)
from django_tenants.models import TenantMixin, DomainMixin


class MessageModel(TenantMixin):
    user = ForeignKey(User, on_delete=CASCADE, verbose_name='user', related_name='from_user', db_index=True)
    recipient = ForeignKey(User, on_delete=CASCADE, verbose_name='recipient', related_name='to_user', db_index=True)
    body = TextField('body')

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = 'core'
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    auto_create_schema = True


class Domain(DomainMixin):
    pass