from rest_framework.renderers import BrowsableAPIRenderer

class CustomBrowsableAPIRendererWithoutForm(BrowsableAPIRenderer):
    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        context['display_edit_forms'] = False
        return context