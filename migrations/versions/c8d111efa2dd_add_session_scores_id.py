"""add session_scores id

Revision ID: c8d111efa2dd
Revises: 35d8d8ecf830
Create Date: 2021-02-23 18:36:01.477120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8d111efa2dd'
down_revision = '35d8d8ecf830'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('session_scores', sa.Column('id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('session_scores', 'id')
    # ### end Alembic commands ###
