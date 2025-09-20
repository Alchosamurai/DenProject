from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from src.models.base_model import Base


class User(Base):
     __tablename__ = "user_account"

     id: Mapped[int] = mapped_column(primary_key=True)
     username: Mapped[str] = mapped_column(String(30))
     password: Mapped[str] = mapped_column(String(30))

     def __repr__(self) -> str:
         return f"User(id={self.id!r}, name={self.username!r}, password={self.password!r}"


def test(a, b, c):
    pass

test(15, 28, c=32)
