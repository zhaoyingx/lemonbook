from flask import Flask

# --create app--
app = Flask(__name__)
app.config.from_object('lemondiary.config')

import views
