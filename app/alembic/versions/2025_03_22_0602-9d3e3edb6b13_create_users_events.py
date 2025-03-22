"""create_users_events

Revision ID: 9d3e3edb6b13
Revises:
Create Date: 2025-03-22 06:02:54.014011

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "9d3e3edb6b13"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("telegram_id", sa.String(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("height", sa.String(), nullable=False),
        sa.Column("weight", sa.String(), nullable=False),
        sa.Column("dob", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("telegram_id"),
    )
    op.create_table(
        "events",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("creator_id", sa.Integer(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("format", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["creator_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_to_event",
        sa.Column("event_id", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["event_id"],
            ["events.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
    )


def downgrade() -> None:
    op.drop_table("user_to_event")
    op.drop_table("events")
    op.drop_table("users")
