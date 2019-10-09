"""empty message

Revision ID: e5b4175be075
Revises: 02be4c8fbd69
Create Date: 2019-10-09 15:34:06.312258

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e5b4175be075'
down_revision = '02be4c8fbd69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('room_languages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('iso', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('game_rooms', 'language')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_rooms', sa.Column('language', postgresql.ENUM(name='languages'), autoincrement=False, nullable=False))
    op.drop_table('room_languages')
    # ### end Alembic commands ###