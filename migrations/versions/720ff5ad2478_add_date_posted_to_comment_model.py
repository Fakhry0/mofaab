"""Add date_posted to Comment model

Revision ID: 720ff5ad2478
Revises: ac92a09ea3a4
Create Date: 2024-09-08 19:36:56.372097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '720ff5ad2478'
down_revision = 'ac92a09ea3a4'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('comment') as batch_op:
        # Drop the 'user_id' column if it exists
        batch_op.drop_column('user_id')
        # Add the 'date_posted' column
        batch_op.add_column(sa.Column('date_posted', sa.DateTime(), nullable=False, server_default=sa.func.now()))


def downgrade():
    with op.batch_alter_table('comment', schema=None) as batch_op:
        # Add the 'user_id' column back
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=False))
        # Add the 'date_created' column
        batch_op.add_column(sa.Column('date_created', sa.DATETIME(), nullable=True))
        # Drop the 'author_id' column if it exists
        batch_op.drop_column('author_id')
        # Create the foreign key constraint
        batch_op.create_foreign_key('actual_constraint_name', 'user', ['user_id'], ['id'])
