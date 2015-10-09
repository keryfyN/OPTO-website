from application import app, db
from application.blueprints.tfts.models import Tft, TftSize, TftResolution

tft1 = TftSize(5)
db.session.add(tft1)
db.session.commit()
