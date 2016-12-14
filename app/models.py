import sqlalchemy as sa

meta = sa.MetaData()

note = sa.Table(
    'notes', meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('created_at', sa.Date, nullable=False),
    sa.Column('updated_at', sa.Date, nullable=False),
    sa.Column('content', sa.Text, nullable=False),

    sa.PrimaryKeyConstraint('id', name='question_id_pkey'))
)
