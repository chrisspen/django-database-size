from django.contrib import admin

import models
import utils

class TableAdmin(admin.ModelAdmin):
    
    list_display = (
        #'id',
        #'site',
        'table_name',
        'schema_name',
        'table_owner',
        'size_in_bytes',
        'pretty_size',
    )
    list_filter = (
        'schema_name',
        'table_owner',
    )
    search_fields = (
        'schema_name',
        'table_name',
        'table_owner',
    )
    readonly_fields = (
        'pretty_size',
    )
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def get_actions(self, request):
        actions = super(TableAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        return readonly_fields + [f.name for f in self.model._meta.fields]
    
    def pretty_size(self, obj=None):
        if obj is None:
            return ''
        return utils.humanize_bytes(obj.size_in_bytes)
    pretty_size.short_description = 'size'
    pretty_size.admin_order_field = 'size_in_bytes'
    
admin.site.register(models.Table, TableAdmin)
