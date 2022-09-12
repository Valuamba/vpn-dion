from django import template

from apps.bot_feedback.models import Message

register = template.Library()


class MessageNode(template.Node):
    def __init__(self, limit, varname):
        self.limit, self.varname = limit, varname

    def render(self, context):
        entries = Message.objects.filter(status__isnull=True)
        context[self.varname] = entries[:int(self.limit)]
        return ""


@register.tag
def get_messages(parser, token):
    """
    Usage::
        {% get_messages [limit] as [varname] %}

    Examples::
        {% get_messages 10 as messages %}
    """
    tokens = token.contents.split()
    if len(tokens) < 4:
        raise template.TemplateSyntaxError(
            "'get_messages' statements require two arguments"
        )
    if not tokens[1].isdigit():
        raise template.TemplateSyntaxError(
            "First argument to 'get_messages' must be an integer"
        )
    if tokens[2] != "as":
        raise template.TemplateSyntaxError(
            "Second argument to 'get_messages' must be 'as'"
        )
    return MessageNode(
        limit=tokens[1],
        varname=tokens[3]
    )
