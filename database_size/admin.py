from __future__ import print_function

from django.contrib import admin
from django.db import connections
from django.contrib.admin import SimpleListFilter

from database_size import models
from database_size import utils

class SelectDatabaseListFilter(SimpleListFilter):

    title = 'database'

    parameter_name = 'database'

    default_value = 'default'

    def __init__(self, request, params, model, model_admin):
        self.parameter_val = None
        try:
            self.parameter_val = request.GET.get(self.parameter_name, self.default_value)
        except Exception as e:
            pass
        super(SelectDatabaseListFilter, self).__init__(request, params, model, model_admin)

    def lookups(self, request, model_admin):
        """
        Must be overriden to return a list of tuples (value, verbose value)
        """
        return [(conn, conn) for conn in connections]

    def choices(self, cl):
        for lookup, title in self.lookups(None, None):
            yield {
                'selected': self.parameter_val == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset.
        """
        queryset._db = self.parameter_val
        return queryset

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
        SelectDatabaseListFilter,
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
