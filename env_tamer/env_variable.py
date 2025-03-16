from sqlalchemy import UniqueConstraint
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class EnvVariable(Base):
    __tablename__ = "env_variable"

    directory: Mapped[str] = mapped_column(String, primary_key=True)
    key: Mapped[str] = mapped_column(String, primary_key=True)
    value: Mapped[str] = mapped_column(String, nullable=False)

    UniqueConstraint(directory, key, name="uix_dir_key")

    def __repr__(self) -> str:
       return f"EnvVariable(directory={self.directory!r}, key={self.key!r}, value={self.value!r})"