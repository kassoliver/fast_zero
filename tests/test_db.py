from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(username='kassia', password='secret', email='teste@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'kassia'))

    assert user.username == 'kassia'
