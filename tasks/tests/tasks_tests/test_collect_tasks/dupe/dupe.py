from sema4ai.tasks import task


@task
def main():
    pass


@task  # type: ignore # noqa
def main():  # type: ignore # noqa
    pass
