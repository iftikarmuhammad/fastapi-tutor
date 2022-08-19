"""alter column

Revision ID: c159497a5915
Revises: 5bd2b1746d68
Create Date: 2022-08-19 23:07:00.687941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c159497a5915'
down_revision = '5bd2b1746d68'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('shortener', 'short_id', new_column_name='shortId')


def downgrade() -> None:
    pass
