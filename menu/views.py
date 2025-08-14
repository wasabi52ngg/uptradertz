from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import MenuItem

class MenuTemplateView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_name = kwargs.get('menu_name')

        if 'path' not in kwargs or not kwargs['path'].strip():
            context['menu_name'] = menu_name
            context['active_item'] = None
        else:
            slugs = kwargs['path'].strip('/').split('/')
            current = None
            for slug in slugs:
                if not slug:
                    continue
                if current is None:
                    current = get_object_or_404(MenuItem, menu_name=menu_name, parent=None, slug=slug)
                else:
                    current = get_object_or_404(MenuItem, parent=current, slug=slug)
            context['menu_name'] = menu_name
            context['active_item'] = current

        return context