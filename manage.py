import click

from runner import WorkerRunner
from runner import LocalRunner



@click.group()
def cli():
    pass


@cli.command()
@click.option('--worker-id', required=True)
def run_local(worker_id):
    runner = LocalRunner()
    return runner(worker_id)


if __name__ == '__main__':
    cli()


