from typing import List

from db import Base
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(50))
    schedule: Mapped[str] = mapped_column()

    students: Mapped[List["Student"]] = relationship(back_populates='group')

    def __str__(self):
        return f"<Group name:{self.name}>"


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(50), nullable=False)
    email: Mapped[str] = mapped_column(sa.String(25), unique=True, )
    age: Mapped[int] = mapped_column(nullable=True)

    group_id = mapped_column(sa.ForeignKey("groups.id"))
    group: Mapped["Group"] = relationship(back_populates='students')
    # projects:

    def __str__(self):
        return f"<Student name:{self.name}, age: {self.age}>"


# student_group_assoc_table = sa.Table(
#     "student_group_assoc_table",
#     Base.metadata,
#     sa.Column("group_id", sa.ForeignKey("groups.id"), primary_key=True),
#     sa.Column("student_id", sa.ForeignKey("students.id"), primary_key=True, ),
# )




#
# class Project(Base):
#     __tablename__ = "projects"
#
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     title: Mapped[str] = mapped_column(sa.String(250), nullable=False)
#     score: Mapped[int] = mapped_column()
#
#     def __str__(self):
#         return f"<Project title:{self.title}>"

