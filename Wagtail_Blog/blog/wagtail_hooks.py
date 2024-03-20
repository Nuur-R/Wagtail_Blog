from wagtail import hooks
from wagtail.admin.userbar import AccessibilityItem
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler

from Wagtail_Blog.blog.models import BlogWriter

"""
N.B. To see what icons are available for use in Wagtail menus and StreamField block types,
enable the styleguide in settings:

INSTALLED_APPS = (
   ...
   'wagtail.contrib.styleguide',
   ...
)

or see https://thegrouchy.dev/general/2015/12/06/wagtail-streamfield-icons.html

This demo project also includes the wagtail-font-awesome-svg package, allowing further icons to be
installed as detailed here: https://github.com/allcaps/wagtail-font-awesome-svg#usage
"""


@hooks.register("register_icons")
def register_icons(icons):
    return icons + [
        "wagtailfontawesomesvg/solid/gears.svg",
    ]


class CustomAccessibilityItem(AccessibilityItem):
    axe_run_only = None


@hooks.register("construct_wagtail_userbar")
def replace_userbar_accessibility_item(request, items):
    items[:] = [
        CustomAccessibilityItem() if isinstance(item, AccessibilityItem) else item
        for item in items
    ]

class PersonViewSet(SnippetViewSet):
    model = BlogWriter
    menu_label = "Blog Writer"  # ditch this to use verbose_name_plural from model
    icon = "group"  # change as required
    list_display = ("first_name", "last_name", "job_title", "thumb_image")
    list_filter = {
        "job_title": ["icontains"],
    }
    list_export = ("first_name", "last_name", "job_title")

register_snippet(PersonViewSet)