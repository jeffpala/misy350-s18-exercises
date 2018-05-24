import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


class Console(db.Model):
    __tablename__ = 'consoles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    games = db.relationship('Game', backref='console', cascade="delete")

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    console_id = db.Column(db.Integer, db.ForeignKey('consoles.id'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/consoles')
def show_all_console():
    consoles = Console.query.all()
    return render_template('console-all.html', consoles=consoles)


@app.route('/console/add', methods=['GET', 'POST'])
def add_consoles():
    if request.method == 'GET':
        return render_template('console-add.html')
    if request.method == 'POST':
        name = request.form['name']
        about = request.form['about']

        console = Console(name=name, about=about)
        db.session.add(console)
        db.session.commit()
        return redirect(url_for('show_all_console'))


@app.route('/api/console/add', methods=['POST'])
def add_ajax_consoles():
    name = request.form['name']
    about = request.form['about']

    console = Console(name=name, about=about)
    db.session.add(console)
    db.session.commit()

    flash('Console Inserted', 'success')
    return jsonify({"id": str(console.id), "name": console.name})


@app.route('/console/edit/<int:id>', methods=['GET', 'POST'])
def edit_console(id):
    console = Console.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('console-edit.html', console=console)
    if request.method == 'POST':

        console.name = request.form['name']
        console.about = request.form['about']

        db.session.commit()
        return redirect(url_for('show_all_console'))


@app.route('/console/delete/<int:id>', methods=['GET', 'POST'])
def delete_console(id):
    console = Console.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('console-delete.html', console=console)
    if request.method == 'POST':

        db.session.delete(console)
        db.session.commit()
        return redirect(url_for('show_all_console'))


@app.route('/api/console/<int:id>', methods=['DELETE'])
def delete_ajax_console(id):
    console = Console.query.get_or_404(id)
    db.session.delete(console)
    db.session.commit()
    return jsonify({"id": str(console.id), "name": console.name})

@app.route('/games')
def show_all_games():
    games = Game.query.all()
    return render_template('game-all.html', games=games)


@app.route('/game/add', methods=['GET', 'POST'])
def add_games():
    if request.method == 'GET':
        consoles = Console.query.all()
        return render_template('game-add.html', consoles=consoles)
    if request.method == 'POST':
        name = request.form['name']
        year = request.form['year']
        description = request.form['description']
        console_name = request.form['console']
        console = Console.query.filter_by(name=console_name).first()
        game = Game(name=name, year=year, description=description, console=console)

        db.session.add(game)
        db.session.commit()
        return redirect(url_for('show_all_games'))


@app.route('/game/edit/<int:id>', methods=['GET', 'POST'])
def edit_game(id):
    game = Game.query.filter_by(id=id).first()
    consoles = Console.query.all()
    if request.method == 'GET':
        return render_template('game-edit.html', game=game, consoles=consoles)
    if request.method == 'POST':

        game.name = request.form['name']
        game.year = request.form['year']
        game.description = request.form['description']
        console_name = request.form['console']
        console = Console.query.filter_by(name=console_name).first()
        game.console = console
        db.session.commit()
        return redirect(url_for('show_all_games'))


@app.route('/game/delete/<int:id>', methods=['GET', 'POST'])
def delete_game(id):
    game = Game.query.filter_by(id=id).first()
    consoles = Console.query.all()
    if request.method == 'GET':
        return render_template('game-delete.html', game=game, consoles=consoles)
    if request.method == 'POST':
        db.session.delete(game)
        db.session.commit()
        return redirect(url_for('show_all_games'))


@app.route('/api/game/<int:id>', methods=['DELETE'])
def delete_ajax_game(id):
    game = Game.query.get_or_404(id)
    db.session.delete(game)
    db.session.commit()
    return jsonify({"id": str(game.id), "name": game.name})


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':

    app.run()
