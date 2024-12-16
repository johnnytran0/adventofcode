from jinja2 import Environment, FileSystemLoader, select_autoescape
import click
import datetime
import os

env = Environment(
    autoescape=select_autoescape(),
    loader=FileSystemLoader('aoc/templates')
)

@click.command()
@click.option('--year', default=datetime.datetime.now().strftime("%Y"))
@click.option('--day', default=datetime.datetime.now().strftime("%d"))
def new_puzzle(year, day):
    template = env.get_template("partN.py.jinja")

    for part in [1,2]:
        render = template.render(year=year, day=day, part=part)
        subdir = f'aoc/{year}/{day}'
        os.makedirs(subdir, exist_ok=True)
        with open(f'{subdir}/part{part}.py', 'w') as f:
            f.write(render)
        f.close()

if __name__ == '__main__':
    new_puzzle()
