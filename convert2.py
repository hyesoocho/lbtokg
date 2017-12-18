from flask import Flask, request
app = Flask(__name__)

html = """
<center>
<form action='/convert' method='POST'>
Pound:<input type='text' name='pound' value='{pound}'> = <span id='kilo'>{kilo}</span><br>
<input type='submit' value='Submit'>
</form>
"""

@app.route("/convert", methods=['post'])
def convert():
    try: 
        request.form["pound"]
        return html.format(pound=request.form["pound"],kilo=int(request.form["pound"])*0.453592)
    except ValueError:
	    return html.format(pound=request.form["pound"],kilo="Oops, please enter a number")
    except Exception:
        return html.format(pound=request.form["pound"],kilo="Sorry. Somrthing went wrong")	
	
@app.route("/")
def index():
    lb = int()
    kg = lb*0.453592
    return html.format(pound=lb,kilo=kg)
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
