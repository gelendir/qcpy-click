import click
import sqlite3
import os
import sys
import random
import datetime

DATABASE_FILE = 'db.sqlite'


db_file = click.Path(writable=True, resolve_path=True)
dice = click.Choice(['4', '6', '8', '12', '20'])


@click.group()
@click.option('--database', default='db.sqlite', envvar='DATABASE', type=db_file, help='database file')
def cli(database):
    global DATABASE_FILE
    DATABASE_FILE = database


@cli.command()
@click.option('--overwrite/--no-overwrite', default=False, help='delete previous database file')
def init(overwrite):
    """create a new database file"""
    if os.path.exists(DATABASE_FILE) and not overwrite:
        click.echo("database file already exists! exiting.")
        sys.exit(1)

    with open(DATABASE_FILE, 'w') as f:
        f.write('')

    click.echo("database {filename} created".format(filename=DATABASE_FILE))


@cli.command()
@click.option('--sides', default=6, type=dice, help='number of dice rolls')
def setup(sides):
    """populate database with default data"""
    sides = int(sides)

    conn = sqlite3.connect(DATABASE_FILE)
    conn.execute("CREATE TABLE dices(sides int)")
    conn.execute("CREATE TABLE rolls(name text, number int, rolled_at datetime)")
    conn.execute("INSERT INTO dices(sides) VALUES (?)", (sides,))
    conn.commit()
    conn.close()

    click.echo("database setup complete")


@cli.command()
@click.option('--name', prompt="Enter your name")
@click.option('--rolls', default=1, type=click.INT, help='number of rolls')
def roll(name, rolls):
    """roll a dice and save result"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    limit = cursor.execute("SELECT sides FROM dices").fetchone()[0]

    for i in range(rolls):
        number = random.randint(1, limit)

        announce = click.style('You rolled a ', fg='green') + click.style(str(number), fg='blue', bg='white')
        click.echo(announce)

        cursor.execute(
            "INSERT INTO rolls(name, number, rolled_at) VALUES (?,?,?)",
            (name, number, datetime.datetime.now())
        )

    conn.commit()


if __name__ == '__main__':
    cli()
