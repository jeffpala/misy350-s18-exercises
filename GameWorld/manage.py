from flask_script import Manager
from gameworld import app, db, Console, Game

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    xbox = Console(name='Xbox One', about='Xbox One was announced in May 2013, it is the successor to Xbox 360 and the third console in the Xbox line.')
    playstation4 = Console(name='Playstation 4', about='PS4 was announced as the successor to the PlayStation 3 on February 20, 2013, it was launched on November 15, 2013 in North America.')
    wii = Console(name='Wii', about='The Wii is a video game console released by Nintendo, on November 19, 2006.')
    game1 = Game(name='Fortnite', year=2017, description="Fortnite is a co-op sandbox survival game developed by Epic Games and People Can Fly and published by Epic Games.", console=xbox)
    game2 = Game(name='Uncharted: The Lost Legacy', year=2017, description="This is an action-adventure game developed by Naughty Dog and published by Sony Interactive Entertainment.", console=playstation4)
    game3 = Game(name='Wii Sports Resort', year=2009, description="Wii Sports Resort is a sports video game developed and published by Nintendo for the Wii video game console, and is a direct sequel to Wii Sports.", console=wii)
    db.session.add(xbox)
    db.session.add(playstation4)
    db.session.add(wii)
    db.session.add(game1)
    db.session.add(game2)
    db.session.add(game3)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
