"""Version number."""

# from importlib.metadata import version

# __version__ = version(__package__)


# Currently the __package__ returns steam_web_api which is wrong. That is the
# dir name. Will make updates in the future. Don't know if this actually effects
# the py package

PACKAGE = "python-steam-api"

try:
    from importlib.metadata import version

    __version__ = version(PACKAGE)
except Exception:
    pass
