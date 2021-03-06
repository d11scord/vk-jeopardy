"""add session_scores table

Revision ID: 2f75d03d163e
Revises: 0d767a2196aa
Create Date: 2021-02-20 21:13:06.063729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f75d03d163e'
down_revision = '0d767a2196aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session_scores',
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['session_id'], ['game_sessions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('session_scores')
    # ### end Alembic commands ###
