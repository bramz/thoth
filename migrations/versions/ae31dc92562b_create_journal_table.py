"""create journal table

Revision ID: ae31dc92562b
Revises: 887d88852df2
Create Date: 2019-06-21 15:31:54.244709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae31dc92562b'
down_revision = '887d88852df2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'journal',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date', sa.Date),
        sa.Column('user', sa.String(50), nullable=False, default='anonymous'),
        sa.Column('title', sa.Text),
        sa.Column('name', sa.Text),
    )

def downgrade():
    op.drop_table('journal')
