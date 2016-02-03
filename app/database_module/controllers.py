from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, Response, \
                  stream_with_context
from flask_login import login_required
from app import db
import datetime

from app.database_module.forms import DateForm
from app.database_module.models import *
from app.auth_module.controllers import login_required
from app.database_module.query import column_windows

database_module = Blueprint('database', __name__, url_prefix='/db')
sensors = db.session.query(Sensor.sensor_id, Sensor.target).all()
sense={}
for s,t in sensors:
    sense[s]=t
@database_module.route('/download', methods=['GET', 'POST'])
@login_required
def download():
    form = DateForm(request.form)
    if form.validate_on_submit():
        pid = db.session.query(Packages.package_id).filter(Packages.tbname==session['table']).all()
        pids = []
        for p in pid:
            pids.append(p[0])
        sids = db.session.query(Sensor.sensor_id).filter(Sensor.package_id.in_(pids)).all()
        start = datetime.datetime.strptime(str(form['startDate'].data), '%Y-%m-%d')
        end   = datetime.datetime.strptime(str(form['endDate'].data), '%Y-%m-%d')
        print(len(sids))
        def gen():
            res = db.session.query(Event.stamp, Event.sensor_id, Event.message).filter(db.and_(Event.stamp>=start, Event.stamp<=end, Event.sensor_id.in_(sids), Event.message.in_(['ON', 'OFF']))).order_by(Event.stamp)
            for row in res.yield_per(5):
                a = '\t'.join([str(str(row.stamp)[:-6]),str(sense[row.sensor_id]), str(row.message), '\n'])
                yield a
        return Response(stream_with_context(gen()), mimetype='text/csv', headers={"Content-disposition":"attachment; filename=data.txt", "Cache-Control":"no-cache"})
    return render_template('download2.html', form=form)
