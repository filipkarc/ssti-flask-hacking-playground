from flask import Flask, render_template_string, request


app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    user = request.args.get('user') or None

    template = '''
    <html><head><title>SSTI demo app</title><style>body {margin: 90px; background-image: url('{{url_for('static', filename='bg.jpg')}}');}</style></head><body>
    '''

    footer = '''
    <br><p style="margin-top: 30px;">
    Follow me: <a href="https://www.linkedin.com/in/filip-karczewski/" target="_blank" style="color: #C21010">LinkedIn</a>&nbsp;&nbsp;
    <a href="https://twitter.com/FilipKarc"  target="_blank" style="color: #C21010">Twitter</a>
    '''

    if user == None:
        template = template + '''
        <h1>Login Form</h1>
        <form>
        <input name="user" style="border: 2px solid #C21010; padding: 10px; border-radius: 10px; margin-bottom: 25px;" value="Username"><br>
        <input type="submit" value="Log In" style="border: 0px; padding: 5px 20px ; color: #C21010;">
        </form>
        '''.format(user) + footer
    else:
        template = template + '''
        <h1>Hi {}</h1>
        Welcome to the vulnerable app.<br>
        Have fun with Server-Side Template Injection (SSTI).
        '''.format(user) + footer
    
    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)

