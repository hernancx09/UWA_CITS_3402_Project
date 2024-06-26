"""amodified message table

Revision ID: 2d46578f721f
Revises: f11cae8807e3
Create Date: 2024-05-01 15:18:26.449336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d46578f721f'
down_revision = 'f11cae8807e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('job_id', sa.Integer(), nullable=False))
        batch_op.create_index(batch_op.f('ix_messages_applicant_id'), ['applicant_id'], unique=False)
        batch_op.create_foreign_key(None, 'users', ['applicant_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_index(batch_op.f('ix_messages_applicant_id'))
        batch_op.drop_column('job_id')

    # ### end Alembic commands ###
