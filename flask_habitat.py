"""
    Flask-Habitat
    ~~~~~~~~~~~~~

    Selectively load Flask configuration values from environment variables at
    runtime.
"""
import os

from flask import current_app


HABITAT_ENVIRONMENT = "environment"
HABITAT_FILE = "file"


class Habitat(object):
    """Flask middleware for supporting config variable placeholders, and
    replacing them at runtime with values from the environment, filesystem,
    or other custom source.
    """

    def __init__(self, app=None, source=None, qualifier=None, exclude=None):
        self.app = app
        self.qualifier = qualifier
        self.source = source
        self.exclude = exclude or ()
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize default Flask-Habitat configuration values."""
        app.config.setdefault("HABITAT_SOURCE", self.source or "environment")
        app.config.setdefault("HABITAT_QUALIFIER", self.qualifier or "$")
        self.update_config()

    def load_source(self):  # pylint: disable=no-self-use
        """Load variables from the environment, file, or some other source."""
        source = self.app.config["HABITAT_SOURCE"]
        if source.lower() not in (HABITAT_ENVIRONMENT, HABITAT_FILE):
            raise ValueError("invalid HABITAT_SOURCE: %r" % source.lower())
        if source == HABITAT_ENVIRONMENT:
            return os.environ
        elif source == HABITAT_FILE:
            # TODO: support JSON, YAML, and Python files as Habitat sources
            raise NotImplementedError("File-based habitats not supported yet")

    def update_config(self):
        """Load the currently configured Habitat source and import all
        variables referenced in the application config from said source."""
        source = self.load_source()
        qualifier = self.app.config["HABITAT_QUALIFIER"]
        for key, value in self.app.config.items():
            if (key.startswith("HABITAT_") or
                    not isinstance(value, str) or
                    key in self.exclude or
                    not value.startswith(qualifier)):
                continue
            external_key = value[len(qualifier):]
            if external_key in source:
                self.app.config[key] = source[external_key]
