"""Add date_posted to Comment model

Revision ID: dbcffb0e3aef
Revises: 7423cc084c40
Create Date: 2024-09-08 19:25:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbcffb0e3aef'
down_revision = '7423cc084c40'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('comment') as batch_op:
        batch_op.add_column(sa.Column('date_posted', sa.DateTime(), nullable=False, server_default=sa.func.now()))


def downgrade():
    with op.batch_alter_table('comment') as batch_op:
        batch_op.drop_column('date_posted')

