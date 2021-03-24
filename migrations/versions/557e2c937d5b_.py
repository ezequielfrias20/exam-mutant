"""empty message

Revision ID: 557e2c937d5b
Revises: 
Create Date: 2021-03-24 01:05:40.329107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '557e2c937d5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mutation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('no_mutation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('no_mutation')
    op.drop_table('mutation')
    # ### end Alembic commands ###
