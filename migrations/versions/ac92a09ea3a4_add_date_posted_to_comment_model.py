"""Add date_posted to Comment model

Revision ID: ac92a09ea3a4
Revises: 67d422151dbe
Create Date: 2024-09-08 19:25:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac92a09ea3a4'
down_revision = '67d422151dbe'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('comment') as batch_op:
        batch_op.add_column(sa.Column('date_posted', sa.DateTime(), nullable=False, server_default=sa.func.now()))


def downgrade():
    with op.batch_alter_table('comment') as batch_op:
        batch_op.drop_column('date_posted')
