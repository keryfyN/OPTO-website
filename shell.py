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
            ts_6 = TftSize(5.0)


            db.session.add(ts_1)
            db.session.add(ts_2)
            db.session.add(ts_3)
            db.session.add(ts_6)
            db.session.commit()

            tr_1 = TftResolution('640', '480', 'VGA')
            tr_2 = TftResolution('800', '600', 'SVGA')
            tr_3 = TftResolution('1024', '768', 'XGA')
            tr_4 = TftResolution('1280', '1024', 'SXGA')
            tr_5 = TftResolution('1680', '1050', 'UXGA')
            tr_6= TftResolution('800', '480', 'WVGA')

            db.session.add(tr_1)
            db.session.add(tr_2)
            db.session.add(tr_3)
            db.session.add(tr_4)
            db.session.add(tr_5)
            db.session.add(tr_6)
            db.session.commit()

            tb_1 = TftBrand('Data Image')
            tb_2 = TftBrand('Data Image')
            tb_3 = TftBrand('Data Image')
            tb_4 = TftBrand('Data Image')
            tb_5 = TftBrand('Data Image')
            tb_6 = TftBrand('Data Image')

            db.session.add(tb_1)
            db.session.add(tb_2)
            db.session.add(tb_3)
            db.session.add(tb_4)
            db.session.add(tb_5)
            db.session.add(tb_6)
            db.session.commit()


            t_1 = Tft('00.00.00001', 'FX000000001', '400', '1000:1', '10', 35, 45, 33, 39, 5.0, 70.0, False, True, ts_1.id, tr_1.id,tb_1.id, -40,50, 118.5,77.55,3.4,108.0,64.8)
            t_2 = Tft('00.00.00002', 'FX000000002', '250', '1500:1', '10', 35, 45, 33, 39, 5.0, 70.0, True, True, ts_2.id, tr_2.id, tb_2.id, -40,50, 118.5,77.55,3.4,108.0,64.8)
            t_3 = Tft('00.00.00003', 'FX000000003', '300', '1800:1', '10', 35, 45, 33, 39, 5.0, 70.0, True, False, ts_3.id, tr_3.id, tb_3.id, -40,50, 118.5,77.55,3.4,108.0,64.8)
            t_4 = Tft('00.00.00004', 'FX000000004', '200', '1200:1', '10', 35, 45, 33, 39, 5.0, 70.0, False, False, ts_1.id, tr_4.id, tb_4.id, -40,50, 118.5,77.55,3.4,108.0,64.8)
            t_5 = Tft('00.00.00005', 'FX000000005', '400', '1000:1', '10', 35, 45, 33, 39, 5.0, 70.0, False, True, ts_3.id, tr_5.id, tb_5.id, -40,50, 118.5,77.55,3.4,108.0,64.8)
            t_6 = Tft('00.00.00006', '31-050WMTB00A3-S', '500', 'TBD', '10', 35,45, 33, 39, 5.0, 70.0, False, True, ts_3.id, tr_5.id, tb_5.id, -40,50, 118.5,77.55,3.4,108.0,64.8)

            db.session.add(t_1)
            db.session.add(t_2)
            db.session.add(t_3)
            db.session.add(t_4)
            db.session.add(t_5)
            db.session.add(t_6)
            db.session.commit()

            tp_1 = TftPort('LVDS', [t_1, t_2])
            tp_2 = TftPort('RGB', [t_3])
            tp_3 = TftPort('Serial', [t_4])
            tp_4 = TftPort('TTL', [t_5])
            tp_5 = TftPort('SPI', [t_1, t_2])

            db.session.add(tp_1)
            db.session.add(tp_2)
            db.session.add(tp_3)
            db.session.add(tp_4)
            db.session.add(tp_5)
            db.session.commit()
