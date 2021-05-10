from django.contrib.admin import ModelAdmin, site
from .models import MessageModel
from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
# from tenant.utils import tenant_from_request


# class MessageModelAdmin(ModelAdmin):
#     search_fields = ('id', 'body', 'user__username', 'recipient__username')
#     list_display = ('id', 'user', 'recipient', 'timestamp', 'characters')
#     list_display_links = ('id',)
#     list_filter = ('user', 'recipient')
#     date_hierarchy = 'timestamp'


admin.site.register(MessageModel)


# @admin.register(MessageModel)
# class MessageAdmin(admin.ModelAdmin):
#     fields = ["id", "body", "user__username", "recipient__username"]
#     # readonly_fields = ["pub_date"]
#
#     def get_queryset(self, request, *args, **kwargs):
#         queryset = super().get_queryset(request, *args, **kwargs)
#         tenant = tenant_from_request(request)
#         queryset = queryset.filter(tenant=tenant)
#         return queryset
#
#     def save_model(self, request, obj, form, change):
#         tenant = tenant_from_request(request)
#         obj.tenant = tenant
#         super().save_model(request, obj, form, change)


