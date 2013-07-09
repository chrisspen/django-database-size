from django.contrib import admin

import models

class DatabaseSizeTableAdmin(admin.ModelAdmin):
    
    list_display = (
        #'id',
        #'site',
        'table_name',
        'size_in_bytes',
    )
    search_fields = (
        'schema_name',
        'table_name',
    )
    readonly_fields = (
    )
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def get_actions(self, request):
        actions = super(DatabaseSizeTableAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(self.readonly_fields)
        return readonly_fields + [f.name for f in self.model._meta.fields]
    
admin.site.register(models.DatabaseSizeTable, DatabaseSizeTableAdmin)
