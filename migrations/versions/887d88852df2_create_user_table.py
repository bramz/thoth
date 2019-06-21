"""create user table

Revision ID: 887d88852df2
Revises: 
Create Date: 2019-06-21 15:31:43.737673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '887d88852df2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('password', sa.String, nullable=False),
    )


def downgrade():
    op.drop_table('user')
