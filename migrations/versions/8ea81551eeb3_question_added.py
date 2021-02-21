"""question added

Revision ID: 8ea81551eeb3
Revises: 7b7a8dd12ed0
Create Date: 2021-02-19 23:02:23.075089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ea81551eeb3'
down_revision = '7b7a8dd12ed0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=45), nullable=False),
    sa.Column('is_right', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answers')
    # ### end Alembic commands ###