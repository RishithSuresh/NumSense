from flask import Flask, render_template, request

app = Flask(__name__)

# --- Number checking functions ---
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

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

def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    explanation = None
    if request.method == "POST":
        try:
            num = int(request.form["number"])
            choice = request.form["choice"]
            explanation = ""
            if choice == "Palindrome":
                s = str(num)
                is_pal = s == s[::-1]
                result = f"{num} is a Palindrome" if is_pal else f"{num} is not a Palindrome"
                explanation = f"Reverse of {s} is {s[::-1]}."
            elif choice == "Prime":
                if num < 2:
                    is_p = False
                    explanation = f"{num} is less than 2."
                else:
                    divisors = [i for i in range(2, int(num**0.5)+1) if num % i == 0]
                    is_p = len(divisors) == 0
                    if is_p:
                        explanation = f"No divisors found between 2 and {int(num**0.5)}."
                    else:
                        explanation = f"Divisible by {divisors[0]}."
                result = f"{num} is Prime" if is_p else f"{num} is not Prime"
            elif choice == "Armstrong":
                digits = [int(d) for d in str(num)]
                power = len(digits)
                parts = [f"{d}^{power}={d**power}" for d in digits]
                total = sum(d**power for d in digits)
                is_a = num == total
                explanation = f"{' + '.join(parts)} = {total}"
                result = f"{num} is an Armstrong number" if is_a else f"{num} is not an Armstrong number"
            elif choice == "Perfect":
                divisors = [i for i in range(1, num) if num % i == 0]
                total = sum(divisors)
                is_per = num == total
                explanation = f"Divisors: {divisors}. Sum = {total}"
                result = f"{num} is a Perfect number" if is_per else f"{num} is not a Perfect number"
            elif choice == "Fibonacci":
                a, b = 0, 1
                seq = [0, 1]
                while b < num:
                    a, b = b, a + b
                    seq.append(b)
                is_fibo = (a == num or b == num)
                explanation = f"Fibonacci sequence up to {num}: {seq if seq[-1] <= num else seq[:-1]}"
                result = f"{num} is a Fibonacci number" if is_fibo else f"{num} is not a Fibonacci number"
        except ValueError:
            result = "❌ Please enter a valid integer"
            explanation = ""

    return render_template("index.html", result=result, explanation=explanation)

if __name__ == "__main__":
    app.run(debug=True)
