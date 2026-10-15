from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.database import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"comment": "User information table"}

    username: Mapped[str] = mapped_column(String(50), comment="Account", nullable=False)
    password: Mapped[str] = mapped_column(String(255), comment="Password", nullable=False)
    name: Mapped[str] = mapped_column(String(50), comment="Name", nullable=False)
    role: Mapped[str] = mapped_column(
        String(50), comment="Role: student-Student, admin-Administrator", nullable=False
    )
    email: Mapped[str | None] = mapped_column(String(50), comment="Email")
    phone: Mapped[str | None] = mapped_column(String(50), comment="Mobile phone number")
    avatar: Mapped[str | None] = mapped_column(String(50), comment="Avatar")
    status: Mapped[int] = mapped_column(default=1, comment="Status: 0-Disabled, 1-Active")