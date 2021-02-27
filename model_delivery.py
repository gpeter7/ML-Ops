 # load Flask 
import flask
import requests
import pickle

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def food():

    data = {"success": False}
    
    with open('model.pkl', 'rb') as handle:
        b = pickle.load(handle)

    m_1 = b["m_1"]
    m_2 = b["m_2"]
    c   = b["c"]
    
    if "msg" in flask.request.args:
        data['input'] = float(flask.request.args['msg'])
        try:
            x = data['input']
            result = (m_1*x + m_2*(x**2) + c)
            data["response"] = result
            data["success"] = True
        except:
            pass
    else:

        try:
            x = 10
            result = (m_1*x + m_2*(x**2) + c)
            data["response"] = result
            data["success"] = True
        except:
            pass

    if data['success']:
        img_str= f"""
                      <table>
                          <tr>
                              <td><b> X </b><td>
                              <td> {x} <td>
                          </tr>
                          <tr>
                              <td><b> M_1 </b><td>
                              <td> {m_1} <td>
                          </tr>
                          <tr>
                              <td><b> M_2 </b><td>
                              <td> {m_2} <td>
                          </tr>
                          <tr>
                              <td><b> Bias </b><td>
                              <td> {c} <td>
                          </tr>
                         <tr>
                              <td><b> Result </b><td>
                              <td> {data["response"]} <td>
                          </tr>
                      </table>
                      
                 """
    return f"""
                <!doctype html>
                <html>
                <head>
                <title>Estimated Y</title>

                </head>
                <body>
                    {img_str}
                </body>
                </html>
        """
    
# start the flask app, allow remote connections
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')