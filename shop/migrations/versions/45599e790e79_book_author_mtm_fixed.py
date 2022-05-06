"""book-author mtm fixed

Revision ID: 45599e790e79
Revises: bd90de543bbf
Create Date: 2022-05-01 20:10:03.304554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45599e790e79'
down_revision = 'bd90de543bbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('book_author_id_fkey', 'book', type_='foreignkey')
    op.drop_column('book', 'author_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('book_author_id_fkey', 'book', 'author', ['author_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
