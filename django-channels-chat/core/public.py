from django.contrib.auth.models import User
from core.models import MessageModel, Domain
user = User.objects.all()
user_list = []
for item in user:
    user_list.append(item)
username = user_list[0]
rep = user_list[1]
tenant = MessageModel(schema_name='tenant1', user=username, recipient=rep, body='hello',)
tenant.save()
domain = Domain()
domain.domain = 't1.chatapp.com'
domain.tenant = tenant
domain.is_primary = True
domain.save()
