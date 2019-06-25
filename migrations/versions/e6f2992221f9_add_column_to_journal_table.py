"""Add column to journal table

Revision ID: e6f2992221f9
Revises: ae31dc92562b
Create Date: 2019-06-27 08:27:44.049751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6f2992221f9'
down_revision = 'ae31dc92562b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('journal', sa.Column('content', sa.Text))


def downgrade():
    op.drop_column('journal', 'content')