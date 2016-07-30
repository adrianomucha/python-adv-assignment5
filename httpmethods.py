from flask import Flask, request
from json import dumps, loads
from assignment import find_object, update_object

app = Flask(__name__)

@app.route('/<oid>', methods=['GET'])
def findObject(oid):
    #DB lookup code goes here
    my_object = find_object(oid)
    if my_object is None:
        return "",404
    return dumps(my_object)

@app.route('/<oid>', methods=['POST', 'PUT'])
def updateObject(oid):
    #DB Update/Upsert code goes here
    my_update = loads(request.get_data())
    my_update['a'] = oid
    update_object(my_update)
    print 'I got a post request!'
    return ""

if __name__ == '__main__':
    # with app.test_client() as c:
    #     get_resp = c.get('/blah')
    #     print 'get status: %s' % get_resp.status
    #     print 'get response: %s' % get_resp.get_data()
    #     post_resp = c.post('/blah')

    app.testing = True
    with app.test_client() as c:
        post_resp = c.post('/adrian', data ='{"some": "random datas"}')
        print 'post status: %s' % post_resp.status
        get_resp = c.get('/adrian')
        print 'get status: %s' % get_resp.status
        print 'get response: %s' % get_resp.get_data()

