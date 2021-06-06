"""empty message

Revision ID: 30c324ff5e4a
Revises: c994b59dd640
Create Date: 2021-06-05 23:10:09.543374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30c324ff5e4a'
down_revision = 'c994b59dd640'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_details', sa.Column('secret_key', sa.String(length=300), nullable=True))
    op.create_unique_constraint(None, 'user_details', ['secret_key'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_details', type_='unique')
    op.drop_column('user_details', 'secret_key')
    # ### end Alembic commands ###