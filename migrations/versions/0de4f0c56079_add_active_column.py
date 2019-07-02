"""Add active column

Revision ID: 0de4f0c56079
Revises: e6f2992221f9
Create Date: 2019-06-28 09:51:53.304452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0de4f0c56079'
down_revision = 'e6f2992221f9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('active', sa.Integer, default=0))


def downgrade():
    op.drop_column('user', 'active')