"""Create question_answer table

Revision ID: 41bb32216d42
Revises: 
Create Date: 2024-07-15 13:53:05.537170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41bb32216d42'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Commands to add new table
    op.create_table(
        'question_answer',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('question', sa.String(), nullable=False),
        sa.Column('answer', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    # Commands to drop the table
    op.drop_table('question_answer')