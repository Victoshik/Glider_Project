from gl.models import Events

menu = [
        {'title': 'Создать событие', 'url_name': 'add_event'},
        {'title': 'Создать заметку', 'url_name': 'add_note'},
        {'title': 'Создать группу', 'url_name': 'add_group'},
        {'title': 'О сайте', 'url_name': 'about'},
        ]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
            user_menu.pop(0)
            user_menu.pop(0)
        context['menu'] = user_menu

        return context
