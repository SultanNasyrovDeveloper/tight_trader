from tortoise import Tortoise, run_async
from tight_trader.settings import config


DSN = "postgres://{user}:{password}@{host}:{port}/{database}"


async def create_tables(url):
    await Tortoise.init(
        db_url=url, modules={'models': ['tight_trader.trading_bot.models',]}
    )
    await Tortoise.generate_schemas()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    run_async(create_tables(db_url))


