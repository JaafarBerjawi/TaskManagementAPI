"""Adding_Indexes

Revision ID: edfc20d489a9
Revises: f564b09eb9ad
Create Date: 2023-08-06 02:16:57.616115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edfc20d489a9'
down_revision = 'f564b09eb9ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_tasks_user_id'), ['user_id'], unique=False)

    with op.batch_alter_table('user_tokens', schema=None) as batch_op:
        batch_op.drop_constraint('user_tokens_token_key', type_='unique')
        batch_op.create_index(batch_op.f('ix_user_tokens_token'), ['token'], unique=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('users_username_key', type_='unique')
        batch_op.create_index(batch_op.f('ix_users_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_username'))
        batch_op.create_unique_constraint('users_username_key', ['username'])

    with op.batch_alter_table('user_tokens', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_tokens_token'))
        batch_op.create_unique_constraint('user_tokens_token_key', ['token'])

    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tasks_user_id'))

    # ### end Alembic commands ###
