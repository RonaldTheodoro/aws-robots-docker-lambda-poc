import click

from runner import runner


def run_robot(event, context):
    return runner(event, context)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--robot-id', required=True, type=int)
def run(robot_id):
    return run_robot({'robot_id': robot_id}, {})


if __name__ == '__main__':
    cli()
