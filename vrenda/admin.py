from django.contrib import admin
from vrenda.models import Entrada, Flow, FlowType, Classification
# Register your models here.


class EntradaAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'value', 'flow', 'observation')
    search_fields = ('user', 'date', 'value', 'flow', 'observation')


admin.site.register(Entrada, EntradaAdmin)


class FlowAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type_of', 'classification')
    search_fields = ('name', 'description', 'type_of', 'classification')


admin.site.register(Flow, FlowAdmin)


class FlowTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(FlowType, FlowTypeAdmin)


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Classification, ClassificationAdmin)
