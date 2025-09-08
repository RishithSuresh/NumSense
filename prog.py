from flask import Flask, render_template, request

app = Flask(__name__)

# --- Number checking functions ---
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d**len(digits) for d in digits)

def is_perfect(n):
    if n < 2:
        return False
    return n == sum(i for i in range(1, n) if n % i == 0)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            num = int(request.form["number"])
            choice = request.form["choice"]

            if choice == "Palindrome":
                result = f"{num} is a Palindrome" if is_palindrome(num) else f"{num} is not a Palindrome"
            elif choice == "Prime":
                result = f"{num} is Prime" if is_prime(num) else f"{num} is not Prime"
            elif choice == "Armstrong":
                result = f"{num} is an Armstrong number" if is_armstrong(num) else f"{num} is not an Armstrong number"
            elif choice == "Perfect":
                result = f"{num} is a Perfect number" if is_perfect(num) else f"{num} is not a Perfect number"

        except ValueError:
            result = "❌ Please enter a valid integer"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
