"""empty message

Revision ID: f82c06cf3a14
Revises: 274fe4e4c4d2
Create Date: 2018-06-26 19:43:24.593844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f82c06cf3a14'
down_revision = '274fe4e4c4d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'deleted_at')
    # ### end Alembic commands ###
