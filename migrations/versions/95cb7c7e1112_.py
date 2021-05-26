"""empty message

Revision ID: 95cb7c7e1112
Revises: 0861c440f069
Create Date: 2021-05-22 17:23:43.435265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95cb7c7e1112'
down_revision = '0861c440f069'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cloth_table', 'prod_name')
    op.drop_column('jewellery_table', 'prod_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jewellery_table', sa.Column('prod_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.add_column('cloth_table', sa.Column('prod_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
