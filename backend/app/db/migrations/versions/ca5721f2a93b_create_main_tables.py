"""create_main_tables
Revision ID: ca5721f2a93b
Revises: 
Create Date: 2022-03-25 16:29:23.607363
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = 'ca5721f2a93b'
down_revision = None
branch_labels = None
depends_on = None

def create_cleanings_table() -> None:
    op.create_table(
        "cleanings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False, server_default="spot_clean"),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )

def upgrade() -> None:
    create_cleanings_table()
    
def downgrade() -> None:
    op.drop_table("cleanings")
