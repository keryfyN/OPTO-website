import os
from application import *
from application.default_settings import _basedir

os.environ['PYTHONINSPECT'] = 'True'
# Create database directory if not exists.
create_db_dir = _basedir + '/db'

if not os.path.exists(create_db_dir):
    os.mkdir(create_db_dir, mode=0o755)


def init_db():
    app = create_app()
    from application.blueprints.tfts.models import TftSize, Tft, TftPort, TftResolution

    with app.app_context():
        if not os.path.exists(app.config['SQLALCHEMY_DATABASE_URI']):
            db.drop_all()
            db.create_all()

            ts_1 = TftSize(5.7)
            ts_2 = TftSize(7.0)
            ts_3 = TftSize(8.0)
            ts_4 = TftSize(12.0)
            ts_5 = TftSize(17.0)

            db.session.add(ts_1)
            db.session.add(ts_2)
            db.session.add(ts_3)
            db.session.add(ts_4)
            db.session.add(ts_5)
            db.session.commit()

            tr_1 = TftResolution('640', '480', 'VGA')
            tr_2 = TftResolution('800', '600', 'SVGA')
            tr_3 = TftResolution('1024', '768', 'XGA')
            tr_4 = TftResolution('1280', '1024', 'SXGA')
            tr_5 = TftResolution('1680', '1050', 'UXGA')

            db.session.add(tr_1)
            db.session.add(tr_2)
            db.session.add(tr_3)
            db.session.add(tr_4)
            db.session.add(tr_5)
            db.session.commit()

            tp_1 = TftPort('LVDS')
            tp_2 = TftPort('CPU RGB SPI')
            tp_3 = TftPort('Serial Parallel')
            tp_4 = TftPort('TTL')
            tp_5 = TftPort('SPI')

            db.session.add(tp_1)
            db.session.add(tp_2)
            db.session.add(tp_3)
            db.session.add(tp_4)
            db.session.add(tp_5)
            db.session.commit()

            t_1 = Tft('00.00.00001', 'FX000000001', '400', '1000:1', '10mpx', False, 35.0, 45.0, 33.0, 39.0, 5.0, 70.0, False, True, ts_1.id, tr_1.id, tp_1.id)
            t_2 = Tft('00.00.00002', 'FX000000002', '250', '1500:1', '10mpx', True, 35.0, 45.0, 33.0, 39.0, 5.0, 70.0, True, True, ts_2.id, tr_2.id, tp_2.id)
            t_3 = Tft('00.00.00003', 'FX000000003', '300', '1800:1', '10mpx', True, 35.0, 45.0, 33.0, 39.0, 5.0, 70.0, True, False, ts_3.id, tr_3.id, tp_3.id)
            t_4 = Tft('00.00.00004', 'FX000000004', '200', '1200:1', '10mpx', False, 35.0, 45.0, 33.0, 39.0, 5.0, 70.0, False, False, ts_4.id, tr_4.id, tp_4.id)
            t_5 = Tft('00.00.00005', 'FX000000005', '400', '1000:1', '10mpx', True, 35.0, 45.0, 33.0, 39.0, 5.0, 70.0, False, True, ts_5.id, tr_5.id, tp_5.id)

            db.session.add(t_1)
            db.session.add(t_2)
            db.session.add(t_3)
            db.session.add(t_4)
            db.session.add(t_5)
            db.session.commit()
