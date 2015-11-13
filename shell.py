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

            ts_1 = TftSize(size_inch=5.7)
            ts_2 = TftSize(size_inch=7.0)
            ts_3 = TftSize(size_inch=8.0)
            ts_6 = TftSize(size_inch=5.0)


            db.session.add(ts_1)
            db.session.add(ts_2)
            db.session.add(ts_3)
            db.session.add(ts_6)
            db.session.commit()

            tr_1 = TftResolution(resolution_x='640', resolution_y='480', resolution_text='VGA')
            tr_2 = TftResolution(resolution_x='800', resolution_y='600', resolution_text='VGA')
            tr_3 = TftResolution(resolution_x='1024', resolution_y='768', resolution_text='VGA')
            tr_4 = TftResolution(resolution_x='1280', resolution_y='1024', resolution_text='VGA')
            tr_5 = TftResolution(resolution_x='1680', resolution_y='1050', resolution_text='VGA')
            tr_6 = TftResolution(resolution_x='800', resolution_y='480', resolution_text='VGA')

            db.session.add(tr_1)
            db.session.add(tr_2)
            db.session.add(tr_3)
            db.session.add(tr_4)
            db.session.add(tr_5)
            db.session.add(tr_6)
            db.session.commit()

            tb_1 = TftBrand(brand_name='Data Image')
            tb_2 = TftBrand(brand_name='Data Vision')
            tb_3 = TftBrand(brand_name='DigiWise')
            tb_4 = TftBrand(brand_name='Anshan Yes')
            tb_5 = TftBrand(brand_name='Truly')
            tb_6 = TftBrand(brand_name='EInk')

            db.session.add(tb_1)
            db.session.add(tb_2)
            db.session.add(tb_3)
            db.session.add(tb_4)
            db.session.add(tb_5)
            db.session.add(tb_6)
            db.session.commit()


            t_1 = Tft(article_number_opto='00.00.00001', article_number_supplier='FX000000001', tft_brightness='400',
                      tft_contrast='1000:1', tft_color_amount='10', tft_viewing_angle_u=35, tft_viewing_angle_d=45,
                      tft_viewing_angle_l=33, tft_viewing_angle_r=39, tft_operating_temperature_min=5.0,
                      tft_operating_temperature_max=70.0, tft_in_production=False, tft_touch_panel=True,
                      tft_size_id=ts_1.id, tft_resolution_id=tr_1.id,tft_brand_id=tb_1.id, tft_storage_temperature_min=-40,
                      tft_storage_temperature_max=50, tft_outline_h_mm=118.5,tft_outline_v_mm=77.55,tft_outline_d_mm=3.4,
                      tft_active_area_h_mm=108.0,tft_active_area_v_mm=64.8)

            t_2 = Tft(article_number_opto='00.00.00002', article_number_supplier='FX000000002', tft_brightness='250',
                      tft_contrast='1500:1', tft_color_amount='10', tft_viewing_angle_u=35, tft_viewing_angle_d=45,
                      tft_viewing_angle_l=33, tft_viewing_angle_r=39, tft_operating_temperature_min=5.0,
                      tft_operating_temperature_max=70.0, tft_in_production=True, tft_touch_panel=True,
                      tft_size_id=ts_2.id, tft_resolution_id=tr_2.id, tft_brand_id=tb_2.id, tft_storage_temperature_min=-40,
                      tft_storage_temperature_max=50, tft_outline_h_mm=118.5,tft_outline_v_mm=77.55,tft_outline_d_mm=3.4,
                      tft_active_area_h_mm=108.0,tft_active_area_v_mm=64.8)

            t_3 = Tft(article_number_opto='00.00.00003', article_number_supplier='FX000000003', tft_brightness='300',
                      tft_contrast='1800:1', tft_color_amount='10', tft_viewing_angle_u=35, tft_viewing_angle_d=45,
                      tft_viewing_angle_l=33, tft_viewing_angle_r=39, tft_operating_temperature_min=5.0,
                      tft_operating_temperature_max=70.0, tft_in_production=True, tft_touch_panel=False,
                      tft_size_id=ts_3.id, tft_resolution_id=tr_3.id, tft_brand_id=tb_3.id, tft_storage_temperature_min=-40,
                      tft_storage_temperature_max=50, tft_outline_h_mm=118.5,tft_outline_v_mm=77.55,tft_outline_d_mm=3.4,
                      tft_active_area_h_mm=108.0,tft_active_area_v_mm=64.8)

            t_4 = Tft(article_number_opto='00.00.00004', article_number_supplier='FX000000004', tft_brightness='200',
                      tft_contrast='1200:1', tft_color_amount='10', tft_viewing_angle_u=35, tft_viewing_angle_d=45,
                      tft_viewing_angle_l=33, tft_viewing_angle_r=39, tft_operating_temperature_min=5.0,
                      tft_operating_temperature_max=70.0, tft_in_production=False, tft_touch_panel=False,
                      tft_size_id=ts_1.id, tft_resolution_id=tr_4.id, tft_brand_id=tb_4.id, tft_storage_temperature_min=-40,
                      tft_storage_temperature_max=50, tft_outline_h_mm=118.5,tft_outline_v_mm=77.55,tft_outline_d_mm=3.4,
                      tft_active_area_h_mm=108.0,tft_active_area_v_mm=64.8)

            t_5 = Tft(article_number_opto='00.00.00005', article_number_supplier='FX000000005', tft_brightness='400',
                      tft_contrast='1000:1', tft_color_amount='10', tft_viewing_angle_u=35, tft_viewing_angle_d=45,
                      tft_viewing_angle_l=33, tft_viewing_angle_r=39, tft_operating_temperature_min=5.0,
                      tft_operating_temperature_max=70.0, tft_in_production=False, tft_touch_panel=True,
                      tft_size_id=ts_3.id, tft_resolution_id=tr_5.id, tft_brand_id=tb_5.id, tft_storage_temperature_min=-40,
                      tft_storage_temperature_max=50, tft_outline_h_mm=118.5,tft_outline_v_mm=77.55,tft_outline_d_mm=3.4,
                      tft_active_area_h_mm=108.0,tft_active_area_v_mm=64.8)

            t_6 = Tft(article_number_opto='00.00.00006', article_number_supplier='31-050WMTB00A3-S', tft_brightness='500',
                      tft_contrast='1000:1', tft_color_amount='10', tft_viewing_angle_u=35,tft_viewing_angle_d=45,
                      tft_viewing_angle_l=33, tft_viewing_angle_r=39, tft_operating_temperature_min=5.0,
                      tft_operating_temperature_max=70.0, tft_in_production=False, tft_touch_panel=True,
                      tft_size_id=ts_3.id, tft_resolution_id=tr_5.id, tft_brand_id=tb_5.id, tft_storage_temperature_min=-40,
                      tft_storage_temperature_max=50, tft_outline_h_mm=118.5,tft_outline_v_mm=77.55,tft_outline_d_mm=3.4,
                      tft_active_area_h_mm=108.0,tft_active_area_v_mm=64.8)

            db.session.add(t_1)
            db.session.add(t_2)
            db.session.add(t_3)
            db.session.add(t_4)
            db.session.add(t_5)
            db.session.add(t_6)
            db.session.commit()

            tp_1 = TftPort(port_type='LVDS', tfts=[t_1, t_2])
            tp_2 = TftPort(port_type='RGB', tfts=[t_3])
            tp_3 = TftPort(port_type='Serial', tfts=[t_4])
            tp_4 = TftPort(port_type='TTL', tfts=[t_5])
            tp_5 = TftPort(port_type='SPI', tfts=[t_1, t_2, t_6])

            db.session.add(tp_1)
            db.session.add(tp_2)
            db.session.add(tp_3)
            db.session.add(tp_4)
            db.session.add(tp_5)
            db.session.commit()
