from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def render_block(context, block_name):
    """
    تگی که یک بلاک خاص را پیدا کرده و نمایش می‌دهد
    """
    return context.get(block_name, f'{{ بلاک "{block_name}" یافت نشد }}')
