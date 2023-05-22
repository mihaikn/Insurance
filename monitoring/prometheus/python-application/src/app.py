from flask import Flask,request,make_response,jsonify,Response
from flask_sqlalchemy import SQLAlchemy
from config_ import *
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time

app=Flask(__name__)
app.config.from_object(Production)
_INF = float("inf")
graphs={}
graphs['c']=Counter('python_request_operations_total','The total number of processed requests')
graphs['h']= Histogram('python_request_duration_seconds','Histogram for the duration in seconds',buckets=(1,2,5,6,10,_INF))

db=SQLAlchemy(app)
class Programm(db.Model):
    __tablename__='programms'
    id=db.Column(db.Integer,primary_key=True)
    prog_name=db.Column(db.String(40))
    direction=db.Column(db.String(100))
    cost=db.Column(db.Integer)

    def __init__(self,prog_name,direction,cost):
        self.prog_name=prog_name
        self.direction=direction
        self.cost=cost

@app.route('/addProgram',methods=['POST'])
def addProgram():
    prog_name=request.form['prog_name']
    direction=request.form['direction']
    cost=request.form['cost']
    program=Programm(prog_name,direction,cost)
    db.session.add(program)
    db.session.commit()
    res="OK"
    return make_response(jsonify(res),200)
@app.route('/allprogs',methods=['GET'])
def allprogs():
    start=time.time()
    graphs['c'].inc()
    progs=db.session.query(Programm)
    res=[]
    for a in progs:
        tmp=[]
        tmp.append(a.prog_name)
        tmp.append(a.direction)
        tmp.append(a.cost)
        res.append(tmp)
    end=time.time()
    graphs['h'].observe(end-start)
    return make_response(jsonify(res),200)
@app.route('/electiveprogs/<dir>',methods=['GET'])
def electiveprogs(dir):
    progs=db.session.query(Programm).filter(Programm.direction==dir)
    res=[]
    for a in progs:
        tmp=[]
        tmp.append(a.prog_name)
        tmp.append(a.direction)
        tmp.append(a.cost)
        res.append(tmp)
    return make_response(jsonify(res),200)
@app.route('/creditcalc/<prog>',methods=['GET'])
def creditcalc(prog):
    progs=db.session.query(Programm).filter(Programm.prog_name==prog).first()
    return make_response(jsonify(progs.cost/12),200)
@app.route('/metrics')
def metrics():
    res=[]
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))

    return Response(res,mimetype="text/plain")
# if __name__=='__main__':
#     app.run()



