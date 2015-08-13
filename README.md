# flask-habitat

Selectively load Flask configuration values from environment variables at
runtime; never store secrets in configuration files again.

## Usage

Initialize **Flask-Habitat** before any other middleware that requires
configuration from a *habitat source* (e.g. environment, filesystem, or some
other user-defined source) in order for Flask config values to be replaced.

```python
from flask import Flask
from flask_habitat import Habitat
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# DATABASE is an environment variable expected to contain the dburi
app.config["SQLALCHEMY_DATABASE_URI"] = "$DATABASE"
app.config.from_envvar("APP_SETTINGS")
habitat = Habitat(app)
db = SQLAlchemy(app)
```

Bear in mind that **Flask-Habitat** only looks for configuration values which
are strings, which makes it compatible with any configuration format used,
which is particularly beneficial when using YAML. Below is an example
YAML-formatted config file using [Flask-Environments][environments]:

```yaml
COMMON: &common
  SQLALCHEMY_URI: $DATABASE_URI
  SECRET_KEY: $SECRET_KEY
  TOKEN_SALT: $TOKEN_SALT

DEVELOPMENT:
  <<: *common
  DEBUG: True

PRODUCTION:
  <<: *common
  SERVER_NAME: $SERVER_NAME
```

[environments]: https://github.com/mattupstate/flask-environments

## Configuration

- **HABITAT_SOURCE** defines where configuration values will be pulled from,
  e.g. the environment, a file, or in the future, some user-defined source.
  _Currently, the only supported value is ``environment``._
- **HABITAT_QUALIFIER** defaults to ``$``, and is the prefix that will be
  expected when looking for placeholders in configuration values.
