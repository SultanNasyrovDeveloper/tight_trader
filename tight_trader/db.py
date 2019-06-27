from tortoise import Tortoise


async def create_engine(app):
    pass


async def close_engine(app):
    await Tortoise.close_connections()
