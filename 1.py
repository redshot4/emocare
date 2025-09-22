from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple HTML template
html = """
<!doctype html>
<html>
  <head>
    <title>User Greeting</title>
  </head>
  <body>
    <h2>Enter your name:</h2>
    <form method="post">
      <input type="text" name="username" required>
      <button type="submit">Submit</button>
    </form>

    {% if name %}
      <h3>Hello, {{ name }}! 👋</h3>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    if request.method == "POST":
        name = request.form.get("username")
    return render_template_string(html, name=name)

if __name__ == "__main__":
    app.run(debug=True)
