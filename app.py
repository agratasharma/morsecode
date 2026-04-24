from flask import Flask, render_template, request
from encoder_decoder import MorseCodeTranslator

app = Flask(__name__)
translator = MorseCodeTranslator()


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    user_input = ""
    mode = "encode"

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        mode = request.form.get("mode", "encode")

        if mode == "encode":
            result = translator.encode(user_input)
        elif mode == "decode":
            result = translator.decode(user_input)
        else:
            result = "Error: Invalid option selected."

    return render_template(
        "index.html",
        result=result,
        user_input=user_input,
        mode=mode
    )


if __name__ == "__main__":
    app.run(debug=True)