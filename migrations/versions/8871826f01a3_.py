"""empty message

Revision ID: 8871826f01a3
Revises: f5272f1ca923
Create Date: 2021-06-05 15:45:17.708384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8871826f01a3'
down_revision = 'f5272f1ca923'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_details', sa.Column('e_password', sa.String(length=500), nullable=True))
    op.add_column('user_details', sa.Column('e_username', sa.String(length=500), nullable=True))
    op.add_column('user_details', sa.Column('secret_key', sa.String(length=100), nullable=True))
    op.add_column('user_details', sa.Column('username', sa.String(length=300), nullable=True))
    op.drop_constraint('user_details_email_key', 'user_details', type_='unique')
    op.create_unique_constraint(None, 'user_details', ['e_username'])
    op.create_unique_constraint(None, 'user_details', ['secret_key'])
    op.create_unique_constraint(None, 'user_details', ['username'])
    op.create_unique_constraint(None, 'user_details', ['e_password'])
    op.drop_column('user_details', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_details', sa.Column('email', sa.VARCHAR(length=300), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user_details', type_='unique')
    op.drop_constraint(None, 'user_details', type_='unique')
    op.drop_constraint(None, 'user_details', type_='unique')
    op.drop_constraint(None, 'user_details', type_='unique')
    op.create_unique_constraint('user_details_email_key', 'user_details', ['email'])
    op.drop_column('user_details', 'username')
    op.drop_column('user_details', 'secret_key')
    op.drop_column('user_details', 'e_username')
    op.drop_column('user_details', 'e_password')
    # ### end Alembic commands ###