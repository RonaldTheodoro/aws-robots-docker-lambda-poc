import click

from runner import runner


def run_worker(event, context):
    return runner(event, context)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--worker-id', required=True, type=int)
def run(worker_id):
    return run_worker({'worker_id': worker_id}, {})


if __name__ == '__main__':
    cli()
