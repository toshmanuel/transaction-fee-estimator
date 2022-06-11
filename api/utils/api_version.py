import os


def api_version(route: str) -> str:
    """
    format routes according to route version number

    :param route: path to create
    :return:
    """
    version = os.environ.get("APP_API_VERSION", default="1")
    return f"/api/v{version}{route}"
    