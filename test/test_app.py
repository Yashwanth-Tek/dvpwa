import pytest


def test_import_app():
    from sqli.app import app
    assert app is not None


def test_import_routes():
    from sqli import routes
    assert routes is not None


def test_import_views():
    from sqli import views
    assert views is not None
