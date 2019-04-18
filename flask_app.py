from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
  return render_template("index.html")

# For web requests called via http:
@app.route('/process_inputs', methods=['POST'])

def process_inputs():
    # Get the input data from the form into variables
    email = request.form.get('inputEmail', '')
    opinion = request.form.get('opinion','')
    g = open('email_list.txt', 'a')  # write to the end of the file so you don't lose data.
    g.write(email + "\n")
    g.write(opinion + "\n")

    g.close()
    return render_template("index.html")


if __name__ == '__main__':
    app.run()

    # import wordfilter
    # wordfilter.add_words(["dumb", "lol", "loser"])
    # wordfilter.blacklisted(['dumb'])