"""Expose the current documentation version to templates.

`mike` sets the ``MIKE_DOCS_VERSION`` environment variable when building a
given version of the docs. This plugin reads that variable and:

- replaces ``{{ version }}`` placeholders in ``config['copyright']`` and
  ``config['site_description']``, and
- exposes ``version`` as a global in the template context, so it can be used
  in overridden templates (e.g. ``{{ version }}``).

The ``default`` config option is used when ``MIKE_DOCS_VERSION`` is not set
(e.g. when building locally with ``mkdocs build``).
"""

import os

from mkdocs.config import config_options as opts
from mkdocs.plugins import BasePlugin


class VersionPlugin(BasePlugin):
    """MkDocs plugin that exposes the current version to templates."""

    config_scheme = (
        ("default", opts.Type(str, default="dev")),
    )

    def _current_version(self):
        return os.environ.get("MIKE_DOCS_VERSION") or self.config["default"]

    def on_config(self, config):
        version = self._current_version()

        # Replace {{ version }} placeholders in string config values.
        for key in ("copyright", "site_description", "site_name"):
            value = config.get(key)
            if isinstance(value, str):
                config[key] = value.replace("{{ version }}", version)

        # Store the version so it can be read in on_env.
        self._version = version
        return config

    def on_env(self, env, config, files):
        env.globals["version"] = self._version
        return env

