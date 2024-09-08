"""Add date_posted to Comment model

Revision ID: 67d422151dbe
Revises: dbcffb0e3aef
Create Date: 2024-09-08 19:25:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67d422151dbe'
down_revision = 'dbcffb0e3aef'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('comment') as batch_op:
        batch_op.add_column(sa.Column('date_posted', sa.DateTime(), nullable=False, server_default=sa.func.now()))


def downgrade():
    with op.batch_alter_table('comment') as batch_op:
        batch_op.drop_column('date_posted')
