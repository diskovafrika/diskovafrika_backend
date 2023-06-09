"""initial migration

Revision ID: db2df78b7151
Revises: 
Create Date: 2023-04-02 07:09:06.825964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db2df78b7151'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('country', sa.Column('sub_region', sa.Enum('Northern', 'Central', 'Western', 'Southern', 'Eastern'), nullable=True))
    op.add_column('country', sa.Column('population', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('country', 'population')
    op.drop_column('country', 'sub_region')
    # ### end Alembic commands ###
