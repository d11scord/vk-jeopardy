"""test mig

Revision ID: 46e2372472a3
Revises: a91e50f90b1c
Create Date: 2021-02-20 18:10:08.138229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46e2372472a3'
down_revision = 'a91e50f90b1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers', sa.Column('test', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answers', 'test')
    # ### end Alembic commands ###