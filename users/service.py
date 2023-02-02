from datetime import datetime

import pytz
from django.conf import settings

from users.models import User


def set_verify_token_and_send_mail(new_user):
    """
        Деактивировать пользователя, установить токен и сроки жизни
        TODO: отправить письмо на почту со ссылкой
    """
    now = datetime.now(pytz.timezone(settings.TIME_ZONE))
    new_user.is_active = False
    new_user.verify_token = User.objects.make_random_password(length=20)
    new_user.verify_token_expired = now
    new_user.save()
