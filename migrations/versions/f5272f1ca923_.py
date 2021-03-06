"""empty message

Revision ID: f5272f1ca923
Revises: 57e8664f1d24
Create Date: 2021-05-23 14:39:11.993231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5272f1ca923'
down_revision = '57e8664f1d24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card_details', sa.Column('card_name', sa.String(length=300), nullable=True))
    op.add_column('card_details', sa.Column('card_no', sa.String(length=300), nullable=True))
    op.create_unique_constraint(None, 'card_details', ['card_no'])
    op.create_unique_constraint(None, 'card_details', ['card_name'])
    op.add_column('user_details', sa.Column('email', sa.String(length=300), nullable=True))
    op.add_column('user_details', sa.Column('password', sa.String(length=300), nullable=True))
    op.create_unique_constraint(None, 'user_details', ['password'])
    op.create_unique_constraint(None, 'user_details', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_details', type_='unique')
    op.drop_constraint(None, 'user_details', type_='unique')
    op.drop_column('user_details', 'password')
    op.drop_column('user_details', 'email')
    op.drop_constraint(None, 'card_details', type_='unique')
    op.drop_constraint(None, 'card_details', type_='unique')
    op.drop_column('card_details', 'card_no')
    op.drop_column('card_details', 'card_name')
    # ### end Alembic commands ###
