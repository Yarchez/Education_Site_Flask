from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from sqlalchemy import create_engine

import db.connect
from db.tables import tasks, levels, topics
from db.config import settings

app = Flask(__name__)
bootstrap = Bootstrap(app)

DATABASE_URL = settings.DATABASE_URL

engine = db.connect.SessionLocal().get_bind()


@app.route('/')
def page_home():
    template_dir = "homepage.html"
    return render_template(template_dir)


@app.route('/topics')
def page_topics():
    template_dir = "topics.html"

    with engine.connect() as connect:
        sql_script = topics.select().order_by("id")
        result_of_ex = connect.execute(sql_script).fetchall()

        lst = []
        for topic in result_of_ex:
            id, text, position_in_exam = topic
            count_of_tasks = len(connect.execute(tasks.select().where(tasks.c.topic_id == id)).fetchall())
            lst.append(
                {
                    "title_of_topic": text,
                    "number_of_topic": id,
                    "count_of_tasks": count_of_tasks,
                },
            )
    return render_template(template_dir, topics=lst)


@app.route('/topics/<int:topic_id>')
def page_topic(topic_id):
    template_dir = "topic.html"
    with engine.connect() as connect:
        sql_script = tasks.select().where(tasks.c.topic_id == topic_id).order_by(tasks.c.id)
        result_of_ex = connect.execute(sql_script).fetchall()

        lst = []
        for task in result_of_ex:
            id, topid_id, level_id, text, answer, is_image = task
            sql_script = levels.select().where(levels.c.id == level_id)
            level_id, level = connect.execute(sql_script).fetchone()
            lst.append(
                {
                    "id": id,
                    "level": level,
                    "text": text,
                    "is_image": is_image,
                    "answer": answer,
                },
            )
    return render_template(template_dir, tasks=lst)


# @app.route('/topics/<int:topic>/<int:id>')
# def page_task(topic, id):
#     template_dir = "task.html"
#     return render_template(template_dir, topic=topic, id=id)


@app.route('/about')
def page_about():
    template_dir = "about.html"
    return render_template(template_dir)


if __name__ == '__main__':
    app.run(port=3001, host='127.0.0.1')
