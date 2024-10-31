from .models import Art

menu = [{'title': 'Главная', 'url_name': ''},
        {'title': 'Регистрация', 'url_name': 'register'},
        {'title': 'Вход', 'url_name': 'login'},
        {'title': 'О нас', 'url_name': 'about'},
        {'title': 'Мой аккаунт', 'url_name': 'my_account'}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        if 'art_selected' not in context:
            context['art_selected'] = 0
        return context