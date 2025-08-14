from django import template
from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path_info

    items = list(MenuItem.objects.filter(menu_name=menu_name).select_related('parent'))

    item_dict = {item.id: item for item in items}
    for item in items:
        item.children = []
    for item in items:
        if item.parent_id and item.parent_id in item_dict:
            item_dict[item.parent_id].children.append(item)

    roots = [item for item in items if not item.parent_id]

    def sort_children(node):
        node.children.sort(key=lambda x: x.order)
        for child in node.children:
            sort_children(child)

    for root in roots:
        sort_children(root)

    active = None
    for item in items:
        if item.get_absolute_url() == current_path:
            active = item
            break

    expanded_ids = set()
    if active:
        current = active
        while current:
            expanded_ids.add(current.id)
            current = current.parent

    return {
        'roots': roots,
        'expanded_ids': expanded_ids,
        'active_id': active.id if active else None
    }