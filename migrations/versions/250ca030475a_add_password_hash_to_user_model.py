"""Add password_hash to User model

Revision ID: 250ca030475a
Revises: cc8d16918e9c
Create Date: 2024-09-07 23:59:53.593229

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision = '250ca030475a'
down_revision = 'cc8d16918e9c'
branch_labels = None
depends_on = None


def upgrade():
    # Check if the 'author' table exists
    bind = op.get_bind()
    inspector = Inspector.from_engine(bind)
    if 'author' not in inspector.get_table_names():
        op.create_table('author',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(length=50), nullable=True),
            sa.Column('profile_picture_url', sa.String(length=200), nullable=True),
            sa.PrimaryKeyConstraint('id')
        )

    with op.batch_alter_table('blog_post', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_blog_post_author_id', 'user', ['author_id'], ['id'])
        batch_op.drop_column('date_created')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=True))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=150), nullable=False))
        batch_op.drop_column('password_hash')

    with op.batch_alter_table('blog_post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_created', sa.DATETIME(), nullable=True))
        batch_op.drop_constraint('fk_blog_post_author_id', type_='foreignkey')

    op.drop_table('author')
    # ### end Alembic commands ###
