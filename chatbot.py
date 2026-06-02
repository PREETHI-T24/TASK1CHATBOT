from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chatbot():
    response = ""

    if request.method == "POST":
        user = request.form["message"].lower()

        if "price" in user:
            response = "The product costs ₹500."

        elif "time" in user:
            response = "Our service is available 24/7."

        elif "help" in user:
            response = "How can I assist you?"

        elif "hello" in user or "hi" in user:
            response = "Hello! Welcome to our chatbot."

        elif "name" in user:
            response = "I am a Rule-Based Chatbot."

        elif "thank" in user:
            response = "You're welcome!"

        elif "bye" in user:
            response = "Thank you! Have a great day."

        elif "chatbot" in user:
            response ="A software application designed to stimulate human conversation"
            
        else:
            response = "Sorry, I don't understand your question."

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)