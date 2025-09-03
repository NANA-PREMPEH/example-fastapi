"""add content column to posts table

Revision ID: 3c7ab5f0937f
Revises: 674a96e81d5a
Create Date: 2025-09-03 01:08:31.356242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c7ab5f0937f'
down_revision: Union[str, Sequence[str], None] = '674a96e81d5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
