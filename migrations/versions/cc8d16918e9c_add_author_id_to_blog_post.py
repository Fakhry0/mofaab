"""Add author_id to blog_post

Revision ID: cc8d16918e9c
Revises: 11a7348884ee
Create Date: 2024-09-07 23:25:51.459391

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'cc8d16918e9c'
down_revision = '11a7348884ee'
branch_labels = None
depends_on = None

def column_exists(table_name, column_name):
    inspector = sa.inspect(op.get_bind())
    columns = [col['name'] for col in inspector.get_columns(table_name)]
    return column_name in columns

def upgrade():
    # Add the new column with a default value if it doesn't exist
    if not column_exists('blog_post', 'author_id'):
        op.add_column('blog_post', sa.Column('author_id', sa.Integer(), nullable=False, server_default='1'))
        # Remove the server default after the column has been populated
        op.alter_column('blog_post', 'author_id', server_default=None)
    
    # If you need to create a foreign key constraint, you can do it here
    # op.create_foreign_key('fk_blog_post_author', 'blog_post', 'user', ['author_id'], ['id'])

def downgrade():
    # Drop the foreign key constraint if it was created
    # op.drop_constraint('fk_blog_post_author', 'blog_post', type_='foreignkey')
    
    # Drop the column if it exists
    if column_exists('blog_post', 'author_id'):
        op.drop_column('blog_post', 'author_id')
