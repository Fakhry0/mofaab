"""Add photo column to Project model

Revision ID: 48f13db7951f
Revises: a110bef24f5c
Create Date: 2024-09-11 21:28:03.980403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48f13db7951f'
down_revision = 'a110bef24f5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photo', sa.String(length=20), nullable=True))
        batch_op.alter_column('date_created',
               existing_type=sa.DATETIME(),
               nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('verification_token')
        batch_op.drop_column('is_verified')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_verified', sa.BOOLEAN(), nullable=True))
        batch_op.add_column(sa.Column('verification_token', sa.VARCHAR(length=100), nullable=True))

    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.alter_column('date_created',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.drop_column('photo')

    # ### end Alembic commands ###
