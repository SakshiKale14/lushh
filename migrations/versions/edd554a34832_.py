"""empty message

Revision ID: edd554a34832
Revises: 0c914959f059
Create Date: 2021-06-06 16:45:24.990982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edd554a34832'
down_revision = '0c914959f059'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_details_e_password_key', 'user_details', type_='unique')
    op.drop_constraint('user_details_e_username_key', 'user_details', type_='unique')
    op.drop_constraint('user_details_password_key', 'user_details', type_='unique')
    op.drop_constraint('user_details_secret_key_key', 'user_details', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_details_secret_key_key', 'user_details', ['secret_key'])
    op.create_unique_constraint('user_details_password_key', 'user_details', ['password'])
    op.create_unique_constraint('user_details_e_username_key', 'user_details', ['e_username'])
    op.create_unique_constraint('user_details_e_password_key', 'user_details', ['e_password'])
    # ### end Alembic commands ###
