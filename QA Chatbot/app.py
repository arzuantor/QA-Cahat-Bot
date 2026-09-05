from flask import Flask, render_template, request, session
from chatbot import get_faq_answer


app = Flask(__name__, template_folder="template")

app.secret_key = "a8F#k29@Lm7!xP4"
@app.route("/")
def home():

    chats = session.get("chats", [])

    return render_template(
        "index.html",
        chats=chats
    )

@app.route("/predict", methods=["POST"])
def predict():
    question = request.form.get("question", "").strip()

    if not question:

        chats = session.get("chats", [])

        return render_template(
            "index.html",
            chats=chats
        )

    chats = session.get("chats", [])

    if len(chats) == 0:

        answer = "Hello! How can I help you?"
    else:

        answer = get_faq_answer(question)

    chats.append({
        "question": question,
        "answer": answer
    })


    session["chats"] = chats

    print("QUESTION:", repr(question))
    print("ANSWER:", repr(answer))


    return render_template(
        "index.html",
        chats=chats
    )
if __name__ == "__main__":

    app.run(debug=True)