from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    description = request.form.get('description')
    if title:
        todo = Todo(title=title, description=description)
        db.session.add(todo)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:id>')
def complete_todo(id):
    todo = Todo.query.get_or_404(id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    init_db()  # 確保資料庫表格被創建
    app.run(debug=True)
