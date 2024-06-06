from flask import render_template, request
from sqlalchemy import select

from db import Session
from app.models import Group, Student
from app import app


@app.route("/")
@app.route("/home")
def home():
    return render_template("base.html", title="MainPage")


@app.route('/groups', methods=["GET", "POST"])
def group_management():
    with Session() as session:
        if request.method == "POST":
            group = Group(name=request.form.get('name'), schedule=request.form.get('schedule'))
            session.add(group)
            session.commit()
        data = session.query(Group).all()
        print(data)

    return render_template('group/groups.html', iterable=data)


@app.route('/groups/<int:id>', methods=["GET"])
def group_get(id):
    with Session() as session:
        data = session.scalars(select(Group).where(Group.id == id)).first()
        print(data)

    return render_template('group/group_info.html', content=data)
