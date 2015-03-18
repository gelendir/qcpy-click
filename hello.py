import click


@click.command()
@click.argument('name')
@click.option('--age', default=0, type=click.INT, help='Your age')
def hello(name, age):
    click.echo("Hello {name} !".format(name=name))

    if 0 < age < 42:
        click.echo("You're young !")
    elif age == 42:
        click.echo("You have the universal age")
    elif age > 42:
        click.echo("You're old !")

if __name__ == "__main__":
    hello()
