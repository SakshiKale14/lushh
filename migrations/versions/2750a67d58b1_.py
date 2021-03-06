"""empty message

Revision ID: 2750a67d58b1
Revises: 53e3a410ee70
Create Date: 2021-06-05 16:41:33.337656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2750a67d58b1'
down_revision = '53e3a410ee70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_details_username_key', 'user_details', type_='unique')
    op.drop_column('user_details', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_details', sa.Column('username', sa.VARCHAR(length=300), autoincrement=False, nullable=True))
    op.create_unique_constraint('user_details_username_key', 'user_details', ['username'])
    # ### end Alembic commands ###
