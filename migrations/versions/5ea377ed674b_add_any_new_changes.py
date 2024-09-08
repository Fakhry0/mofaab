"""Add any new changes

Revision ID: 5ea377ed674b
Revises: 720ff5ad2478
Create Date: 2024-09-08 20:05:45.372097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ea377ed674b'
down_revision = '720ff5ad2478'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('comment') as batch_op:
        # Drop the 'date_created' column if it exists
        batch_op.drop_column('date_created')
        # Add the 'date_posted' column
        batch_op.add_column(sa.Column('date_posted', sa.DateTime(), nullable=False, server_default=sa.func.now()))
        # Ensure the 'author_id' column exists
        batch_op.add_column(sa.Column('author_id', sa.Integer(), nullable=False))
        # Add a foreign key constraint with a name
        batch_op.create_foreign_key('fk_comment_author_id', 'user', ['author_id'], ['id'])


def downgrade():
    with op.batch_alter_table('comment', schema=None) as batch_op:
        # Add the 'date_created' column back
        batch_op.add_column(sa.Column('date_created', sa.DATETIME(), nullable=True))
        # Drop the 'date_posted' column
        batch_op.drop_column('date_posted')
        # Drop the 'author_id' column
        batch_op.drop_column('author_id')
        # Drop the foreign key constraint
        batch_op.drop_constraint('fk_comment_author_id', type_='foreignkey')
