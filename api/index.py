from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route('/greet',methods=['GET'])

def greet():
    
    name=request.args.get('name')

    if name:
        return jsonify({"message": f"Hi, {name} ! how you doing"})
    else:
        return jsonify({'error':"Please Specify name in  the 'name' query parametes."}), 400
    
if __name__=='__main__':
    app.run(debug=True)
