"""empty message

Revision ID: 9999434d3181
Revises: 95cb7c7e1112
Create Date: 2021-05-22 21:01:44.747119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9999434d3181'
down_revision = '95cb7c7e1112'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cloth_table', 'description')
    op.drop_column('jewellery_table', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jewellery_table', sa.Column('description', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('cloth_table', sa.Column('description', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
