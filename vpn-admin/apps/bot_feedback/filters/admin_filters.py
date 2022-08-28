from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class StatusListFilter(admin.BooleanFieldListFilter):
    def choices(self, changelist):
        field_choices = dict(self.field.flatchoices)
        for lookup, title in (
                (None, _("All")),
                ("1", field_choices.get(True, _("Processed"))),
                ("0", field_choices.get(False, _("Ignored"))),
        ):
            yield {
                "selected": self.lookup_val == lookup and not self.lookup_val2,
                "query_string": changelist.get_query_string(
                    {self.lookup_kwarg: lookup}, [self.lookup_kwarg2]
                ),
                "display": title,
            }
        if self.field.null:
            yield {
                "selected": self.lookup_val2 == "True",
                "query_string": changelist.get_query_string(
                    {self.lookup_kwarg2: "True"}, [self.lookup_kwarg]
                ),
                "display": field_choices.get(None, _("Unchecked")),
            }