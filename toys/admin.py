from django.contrib import admin
from toys.models import Toy


from django.utils.timezone import now
from django.utils.html import format_html

@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "toy_category",
        "release_date",
        "was_included_icon",
        "days_since_release",
    )
    list_filter = ("toy_category", "release_date", "was_included_in_home")
    search_fields = ("name", "description", "toy_category")
    ordering = ("name", "release_date")
    fieldsets = (
        ("Informações Básicas", {
            "fields": ("name", "description", "toy_category")
        }),
        ("Detalhes de Lançamento", {
            "fields": ("release_date", "was_included_in_home")
        }),
    )

    def was_included_icon(self, obj):
        return "✅" if obj.was_included_in_home else "❌"
    was_included_icon.short_description = "Incluído em casa"
    was_included_icon.admin_order_field = "was_included_in_home"

    def days_since_release(self, obj):
        delta = (now() - obj.release_date).days
        if delta >= 0:
            return f"{delta} dias atrás"
        return format_html('<span style="color:red">no futuro</span>')
    days_since_release.short_description = "Lançado há"

