# List all Laptop Service

import os
from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient

# Instantiate App and mongodb
app = Flask(__name__)
api = Api(app)

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.timedb

@app.route('/')
def buttons():
    return render_template('buttons.html')


class All(Resource):
    def get(self, context='json'):
        getTop = reqparse.RequestParser()
        getTop.add_argument('top', type=int)
        stuff = getTop.parse_args()
        k = stuff['top']

        times = db.timedb.find()
        show = [time for time in times]
        
        if(context == 'csv'):
            show = '_id, OPEN, CLOSE\n'
            if(k):
                times = db.timedb.find(limit=k)
                for time in times:
                    dat = '{}, {}, {}\n'.format(time["_id"], time["OPEN"], time["CLOSE"])
                    show =+ dat
            else:
                times = db.timedb.find()
                for time in times:
                    dat = '{}, {}, {}\n'.format(time["_id"], time["OPEN"], time["CLOSE"])
                    show =+ dat
            result = show
        elif (context == 'json'):
            if(k):
                times = db.timedb.find(limit=k)
                show = [time for time in times]
                result = show 
            else:
                times = db.timedb.find()
                show = [time for time in times]
                result = show
        return result

class Open(Resource):
    def get(self, context='json'):
        getTop = reqparse.RequestParser()
        getTop.add_argument('top', type=int)
        stuff = getTop.parse_args()
        k = stuff['top']
        if(context == 'csv'):
            show = '_id, OPEN'
            if(k):
                times = db.timedb.find({}, {"CLOSE": 0}, limit=k)
                for time in times:
                    dat = '{}, {}\n'.format(time["_id"], time["OPEN"])
                    show =+ dat
            else:
                times = db.timedb.find({}, {"CLOSE": 0})
                for time in times:
                    dat = '{}, {}\n'.format(time["_id"], time["OPEN"])
                    show =+ dat
            result = show
        elif (context == 'json'):
            if(k):
                times = db.timedb.find({}, {"CLOSE": 0}, limit=k)
                show = [time for time in times]
            else:
                times = db.timedb.find({}, {"CLOSE": 0})
                show = [time for time in times]
            result = show
        return result


class Close(Resource):
    def get(self, context='json'):
        getTop = reqparse.RequestParser()
        getTop.add_argument('top', type=int)
        stuff = getTop.parse_args()
        k = stuff['top']
        if(context == 'csv'):
            show = '_id, CLOSE\n'
            if(k):
                times = db.timedb.find({}, {"OPEN":0}, limit=k)
                for time in times:
                    dat = '{}, {}\n'.format(time['_id'], time['CLOSE'])
                    show =+ dat
            else:
                times = db.timedb.find({}, {"OPEN":0})
                for time in times:
                    dat = '{}, {}\n'.format(time['_id'], time['CLOSE'])
                    show =+ dat
            result = show
        elif (context == 'json'):
            if(k):
                times = db.timedb.find({}, {"OPEN": 0}, limit=k)
                show = [time for time in times]
            else:
                times = db.timedb.find({}, {"OPEN": 0})
                show = [time for time in times]
            result = show
        return result

api.add_resource(All, '/listAll', '/listAll/<string:context>')
api.add_resource(Open, '/listOpenOnly', '/listOpenOnly/<string:context>')
api.add_resource(Close, '/listCloseOnly', '/listCloseOnly/<string:context>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
