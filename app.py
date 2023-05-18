from flask import Flask,request,make_response,jsonify
from flask_sqlalchemy import SQLAlchemy
from config_ import *

app=Flask(__name__)
app.config.from_object(Production)

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
    progs=db.session.query(Programm)
    res=[]
    for a in progs:
        tmp=[]
        tmp.append(a.prog_name)
        tmp.append(a.direction)
        tmp.append(a.cost)
        res.append(tmp)
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
if __name__=='__main__':
    app.run()



