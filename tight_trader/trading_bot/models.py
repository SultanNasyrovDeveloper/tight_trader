from tortoise.models import Model
from tortoise import fields


class TradingBotBase(Model):
    """ Abstract trading bot model """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)

    def __str__(self):
        return 'Trading Bot {}'.format(self.id)

    def start_trading(self):
        pass
