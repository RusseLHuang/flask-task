"""create task table

Revision ID: f42dae0d6d89
Revises: 
Create Date: 2021-03-27 17:12:41.834848

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f42dae0d6d89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'task',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('status', sa.Boolean, nullable=False),
    )
    pass


def downgrade():
    op.drop_table('task')
    pass
