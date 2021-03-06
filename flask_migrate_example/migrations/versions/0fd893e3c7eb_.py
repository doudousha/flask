"""empty message

Revision ID: 0fd893e3c7eb
Revises: 12f9e436b3e6
Create Date: 2018-08-28 22:48:17.913158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fd893e3c7eb'
down_revision = '12f9e436b3e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('alias_name', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'alias_name')
    # ### end Alembic commands ###
