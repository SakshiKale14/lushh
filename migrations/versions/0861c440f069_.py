"""empty message

Revision ID: 0861c440f069
Revises: 7161c49d4ee2
Create Date: 2021-05-22 17:08:26.066951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0861c440f069'
down_revision = '7161c49d4ee2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cloth_table', sa.Column('prod_name', sa.String(length=50), nullable=True))
    op.add_column('jewellery_table', sa.Column('prod_name', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('jewellery_table', 'prod_name')
    op.drop_column('cloth_table', 'prod_name')
    # ### end Alembic commands ###
