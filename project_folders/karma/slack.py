import telepot

from slacker import Slacker
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from ..slack.models import Channel
from ..slack.utils import get_missed_member_telegram_handles

slack = Slacker('xoxb-865126114002-881145910964-YiQ1vJ7ClNONwXBlrDzAz50m')

class Service:
    @classmethod
    def get_bot(cls):
        return telepot.Bot(settings.BOT_TOKEN)
