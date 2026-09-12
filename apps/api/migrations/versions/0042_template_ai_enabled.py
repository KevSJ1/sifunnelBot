"""Let portal templates be available to the AI agent.

Revision ID: 0042_template_ai_enabled
Revises: 0041_client_tz_portal_roles
"""

from alembic import op
import sqlalchemy as sa


revision = "0042_template_ai_enabled"
down_revision = "0041_client_tz_portal_roles"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "canned_responses",
        sa.Column("ai_enabled", sa.Boolean(), server_default=sa.false(), nullable=False),
    )


def downgrade() -> None:
    op.drop_column("canned_responses", "ai_enabled")