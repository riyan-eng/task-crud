from flask import Flask, jsonify, request
import psycopg2
app = Flask(__name__)

@app.route("/create", methods=["POST"])
def create():
    nama = (request.json)["name"]
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="riyan"
    )
    curs = conn.cursor()
    query = f"insert into task(name) values('{nama}')"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    returnJson = {
        "message": f"berhasil memassukkan {nama}"
    }
    return jsonify(returnJson)

@app.route("/list", methods=["GET"])
def list():
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="riyan"
    )
    curs = conn.cursor()
    query = f"select * from task"
    curs.execute(query)
    data = curs.fetchall()
    array = []
    for d in data:
        array.append({
            "id": d[0],
            "name": d[1]
        })
    curs.close()
    conn.close()
    return jsonify(array)

@app.route("/detail/<id>", methods=["GET"])
def detail(id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="riyan"
    )
    curs = conn.cursor()
    query = f"select * from task where id= {id}"
    curs.execute(query)
    data = curs.fetchone()
    responseJson = {
        "id": data[0],
        "name": data[1]
    }
    
    curs.close()
    conn.close()
    return jsonify(responseJson)

@app.route("/update/<id>", methods=["PUT"])
def update(id):
    name = (request.json)["name"]
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="riyan"
    )
    curs = conn.cursor()
    query = f"update task set name = '{name}' where id = {id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    responseJson = {
        "message": "berhasil update"
    }
    return jsonify(responseJson)

@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="riyan"
    )
    curs = conn.cursor()
    query = f"delete from task where id= {id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    responseJson = {
        "message": "berhasil hapus"
    }
    return jsonify(responseJson)

if __name__ == "__main__":
    app.run()