#!/usr/bin/env python
import click

@click.command()
def hello():
    click.echo('Hello all. My name is Kabita Paul')

if __name__ == '__main__':
    hello()
