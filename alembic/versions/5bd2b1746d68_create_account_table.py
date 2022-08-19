"""create account table

Revision ID: 5bd2b1746d68
Revises: 
Create Date: 2022-08-19 22:57:29.820992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bd2b1746d68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('shortener', sa.Column('createdAt', sa.DateTime))


def downgrade() -> None:
    op.drop_column('shortener', 'createdAt')
