from typing import Optional
from src.database.database import get_db
from src.models.user_model import User

from sqlalchemy import select



class UserRepo:
    def __init__(self) -> None:
        self.session = next(get_db())

    def get(self, user_id: int) -> Optional[User]:
        query = select(User).where(User.id == user_id)
        user = self.session.execute(query)
        return user.scalar_one_or_none()

    def get_by_username(self, username: str) -> Optional[User]:
        query = select(User).where(User.username == username)
        user = self.session.execute(query)
        return user.scalar_one_or_none()

    def check_password(self, username: str, password: str) -> bool:
        query = select(User).where(User.username == username, User.password == password)
        user = self.session.execute(query)
        user = user.scalar_one_or_none()
        if user:
            return True
        return False

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user: User) -> User:
        user = self.session.merge(user)
        self.session.commit()
        return user

    def delete(self, user_id) -> None:
        user = self.get(user_id)
        self.session.delete(user)
        self.session.commit()


def user_repo_tests():
    repo = UserRepo()
    print(repo.get(1))

if __name__ == "__main__":
    user_repo_tests()
