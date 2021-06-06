"""empty message

Revision ID: a02b4ae6ef6b
Revises: 30c324ff5e4a
Create Date: 2021-06-05 23:21:50.841052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a02b4ae6ef6b'
down_revision = '30c324ff5e4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card_details', sa.Column('e_cardNo', sa.String(length=500), nullable=True))
    op.add_column('card_details', sa.Column('iv', sa.String(length=256), nullable=True))
    op.add_column('card_details', sa.Column('secret_key', sa.String(length=500), nullable=True))
    op.drop_constraint('user_details_secret_key_key', 'user_details', type_='unique')
    op.drop_column('user_details', 'secret_key')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_details', sa.Column('secret_key', sa.VARCHAR(length=300), autoincrement=False, nullable=True))
    op.create_unique_constraint('user_details_secret_key_key', 'user_details', ['secret_key'])
    op.drop_column('card_details', 'secret_key')
    op.drop_column('card_details', 'iv')
    op.drop_column('card_details', 'e_cardNo')
    # ### end Alembic commands ###
