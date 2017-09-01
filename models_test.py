# -*- coding: utf-8 -*-
import arrow

from app import db, app
from app.models import *
from app.helper import *
from sqlalchemy import func


def test_scope_get():
    scope = Scope.query.all()
    for i in scope:
        print i.name

def test_user_get():
    user = Users.query.filter_by(username='admin', banned=0).first()
    print user.scope
    
def test_traffic_get():
    r = Traffic.query.first()
    #help(r)
    print type(r.pass_time)
    #print r.crossing_id

def test_traffic_add():
    t_list = []
    for i in range(3):
        t = Traffic(crossing_id='441302123', lane_no=1, direction_index='IN',
                    plate_no=u'粤L12345', plate_type='',
                    pass_time='2015-12-13 01:23:45', plate_color='0')
        db.session.add(t)
        t_list.append(t)
    db.session.commit()
    r = [{'pass_id': r.pass_id} for r in t_list]
    print r

def test_uci_add():
    t = UserCltxId(user_id=1, city='hcq', cltx_id=123)
    db.session.add(t)
    db.session.commit()

def test_uci_get():
    u = UserCltxId.query.filter_by(user_id=22, city='hcq').first()
    u.cltx_id = 456
    db.session.commit()

def test_cltx():
    sql = ("select max(id) from cltx")
    query = db.get_engine(app, bind='kakou').execute(sql)
    r = query.fetchone()
    print r
    query.close()


def test_kkdd():
    k = Kkdd.query.filter_by(kkdd_id='441302001', banned=0).first()
    print k.kkdd_id

def test_kkdd2():
    k = Kkdd.query.filter_by().all()
    print k

def test_kkdd3():
    k = db.session.query(Kkdd).filter(Kkdd.kkdd_id.like('441302%')).all()
    print k

def test_stat():
    sql = "select count(*) from cltx where jgsj >= to_date('2016-06-19 00:00:00', 'yyyy-mm-dd hh24:mi:ss') and jgsj <= to_date('2016-06-19 00:05:00', 'yyyy-mm-dd hh24:mi:ss') and wzdd='\xe4\xba\xa4\xe8\xad\xa6\xe6\x94\xaf\xe9\x98\x9f\xe5\x8d\xa1\xe5\x8f\xa3'"
    sql2 = "select * from cltx where jgsj >= to_date('2016-06-19 00:00:00', 'yyyy-mm-dd hh24:mi:ss') and jgsj <= to_date('2016-06-19 00:05:00', 'yyyy-mm-dd hh24:mi:ss')"
    query = db.get_engine(app, bind='kakou').execute(sql2)
    r = query.fetchone()
    print (r[3].decode('gbk'),r[0])

def test_maxid():
    q = db.session.query(func.max(Cltx.id)).first()
    print(q)

def test_cltx2():
    #c = db.session.query(Cltx).filter(Cltx.id>=1103178024,Cltx.id<=1103178034).all()
    st = arrow.get('2017-07-17 15:00:00').datetime.replace(tzinfo=None)
    et = arrow.get('2017-07-17 15:00:01').datetime.replace(tzinfo=None)
    c = db.session.query(Cltx).filter(Cltx.jgsj>=st)
    c = c.filter(Cltx.jgsj<=et).limit(10).offset(0).all()
    for i in c:
	print (i.hphm, i.jgsj)
    #print (c.fxbh, c.hphm, c.jgsj)

if __name__ == '__main__':
    test_maxid()
    test_cltx2()


