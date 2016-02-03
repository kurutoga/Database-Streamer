from app import db

class Packages(db.Model):
    __tablename__ = 'package'
    __bind_key__  = 'primary'
    
    package_id = db.Column('package_id', db.Integer, primary_key=True)
    serial = db.Column('serial', db.Text, nullable=False)
    tbname = db.Column('tbname', db.Text, nullable=False)
    type_id = db.Column('type_id', db.Integer)
    created_on = db.Column('created_on', db.DateTime, nullable=False)
   
class Sensor(db.Model):
    __tablename__ = 'sensor'
    __bind_key__  = 'primary'

    event_id = db.Column(db.Integer, primary_key=True)
    message  = db.Column(db.Text, nullable=False)
    sensor_id = db.Column(db.Integer, nullable=False)
    package_id = db.Column(db.Integer, nullable=False)
    stamp    = db.Column(db.DateTime, nullable=False)
    category = db.Column(db.Text)
    uuid     = db.Column(db.Text)
    channel_id = db.Column(db.Integer)
    key_id = db.Column(db.Integer)
    by_id  = db.Column(db.Integer, nullable=False)

    def __init__(self, e, m, s, s2, c, u, c2, k, b):
        self.event_id = e
        self.message = m
        self.sensor_id = s
        self.stamp = s2
        self.category = c
        self.uuid = u
        self.channel_id = c2
        self.key_id = k
        self.by_id = b

class ExperimentData(db.Model):
    
    __tablename__ = 'experiment_all_data'
    __bind_key__  = 'primary'

    uuid		= db.Column(db.String(32), primary_key=True)
    stamp		= db.Column(db.DateTime)
    stamp_utc   	= db.Column(db.DateTime)
    stamp_local 	= db.Column(db.DateTime)
    message		= db.Column(db.Text)
    by			= db.Column(db.Text)
    category		= db.Column(db.Text)
    serial		= db.Column(db.Text)
    target		= db.Column(db.Text)
    package_type	= db.Column(db.Text)
    sensor_type 	= db.Column(db.Text)
    channel		= db.Column(db.Text)
    tbname		= db.Column(db.Text)
    timezone		= db.Column(db.Text)
    label_name  	= db.Column(db.Text)
    value		= db.Column(db.Text)
    created_by  	= db.Column(db.Text)
    tag_inserted_when	= db.Column(db.DateTime)
    is_valid		= db.Column(db.Boolean)
    start_version	= db.Column(db.Integer)
    last_version	= db.Column(db.Integer)
    data_set_name	= db.Column(db.Text)
    experiment_name	= db.Column(db.Text)


    def __init__(self, a, b, c, d, e, f, g, h, i, \
                       j, k, l, m, n, o, p, q, r, \
                       s, t, u, v, w):
	self.uuid = a
	self.stamp = b
	self.stamp_utc = c
	self.stamp_local = d
	self.message = e
	self.by	= f
	self.category = g
	self.serial = h
	self.target = i
	self.package_type = j
	self.sensor_type = k
	self.channel = l
	self.tbname = m
	self.timezone = n		
	self.label_name = o
	self.value = p
	self.created_by = q
	self.tag_inserted_when = r
	self.is_valid = s
	self.start_version = t
	self.last_version = u
	self.data_set_name = v
	self.experiment_name = w
	
class Event(db.Model):

    __tablename__ = 'event'
    __bind_key__  = 'primary'

    event_id = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(64))
    sensor_id = db.Column(db.Integer, nullable=False)
    stamp = db.Column(db.DateTime)
    category = db.Column(db.String(64))
    uuid = db.Column(db.String(64), primary_key=True)
    channel_id = db.Column(db.Integer, nullable=False)
    key_id = db.Column(db.Integer, nullable=False)
    by_id = db.Column(db.Integer, nullable=False)
    
    def __init__(self, e, m, d, s, c, u, k, m2, n):
        self.eventid = e
        self.message = m
        self.sensor_id    = d
        self.stamp   = s
        self.by_id      = n
        self.category= c
        self.uuid    = u
        self.channel_id = k
        self.key_id = m2
        self.ct      = 7
  
    def __repr__ (self):
        return 'Event %r %r %r %r' % (self.eventid, self.message, self.dsid, self.stamp) #test

    def __iter__(self):
        self.ct = 7
        return self

#i know this is crazy. just for testing =D
    def __next__(self):
        if self.ct>0:
            if (self.ct==7):
                return '%r' % self.eventid
            elif (self.ct==6):
                return '%r' % self.message
            elif (self.ct==5):
                return '%r' % self.dsid
            elif (self.ct==4):
                return '%r' % self.stamp
            elif (self.ct==3):
                return '%r' % self.by
            elif (self.ct==2):
                return '%r' % self.category
            elif (self.ct==1):
                return '%r' % self.uuid
            self.ct -= 1
        else:
            raise StopIteration
    
