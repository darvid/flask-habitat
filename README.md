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
