import aiopg.sa
import sqlalchemy as sa


async def init_pg(app):
    conf = app['config']['db']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        loop=app.loop)
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


meta = sa.MetaData()


note = sa.Table(
    'notes', meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('created_at', sa.Date, nullable=False),
    sa.Column('updated_at', sa.Date, nullable=False),
    sa.Column('content', sa.Text, nullable=False),

    sa.PrimaryKeyConstraint('id', name='question_id_pkey')
)
