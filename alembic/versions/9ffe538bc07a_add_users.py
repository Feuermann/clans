"""Add users

Revision ID: 9ffe538bc07a
Revises: 0cbd012d8746
Create Date: 2017-03-24 11:57:19.104105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ffe538bc07a'
down_revision = '0cbd012d8746'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userprofile',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('battles_total', sa.Integer(), nullable=False),
    sa.Column('wins_total', sa.Integer(), nullable=False),
    sa.Column('vehicles_x', sa.Integer(), nullable=False),
    sa.Column('exp_total', sa.Integer(), nullable=False),
    sa.Column('is_hidden', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userprofile')
    # ### end Alembic commands ###