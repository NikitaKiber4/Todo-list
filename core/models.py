from pydantic import BaseModel
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from core.database import Base

class CreateTask(BaseModel):
    title: str
    description: str | None = None

class TaskModel(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
