from wagtail.admin.edit_handlers import InlinePanel, FieldPanel
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from addendum.models import Snippet


class SnippetAdmin(ModelAdmin):
    model = Snippet
    menu_label = 'Snippets'
    menu_icon = 'doc-full'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('key', 'text')
    search_fields = ('text',)


Snippet.panels = [
    FieldPanel('key'),
    FieldPanel('text'),
    InlinePanel('translations', label='Translations')
]

modeladmin_register(SnippetAdmin)