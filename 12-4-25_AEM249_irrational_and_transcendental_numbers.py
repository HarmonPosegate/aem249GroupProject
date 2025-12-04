# approximate e^x using n number of taylor series terms
def eul(x, n):
    user_num = x
    e_approx = 0
    for i in range(n):
        e_approx += (user_num**i) / factorial(i)
    return e_approx

# approximate x*pi using n number of taylor series terms
# this is a REALLY BAD approximation, but gets the point across
def xpi(x, n):
    user_num = x
    pi_approx = 0
    sign = 1.0
    for i in range(n):
        pi_approx += sign / (2*i + 1)
        sign = -sign
    return 4 * user_num * pi_approx

# calculate the factorial of a number n
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# find the nearest perfect square root of n
def nearest_square(n):
    found_min = float('inf')
    empirical = 0
    for i in range(51):   # search 0–50
        test_diff = abs(n - i*i)
        if test_diff < found_min:
            found_min = test_diff
            empirical = i
            if test_diff == 0:
                break
    return empirical

# compute (1/2 choose k)
def choose_half(k):
    num = 1.0
    for j in range(k):
        num *= (0.5 - j)
    return num / factorial(k)

# approximate sqrt(x) using n Taylor series terms
def sqt(x, n):
    user_num = x
    nearest_root = nearest_square(x)
    x_0 = nearest_root * nearest_root     # expansion point
    sr_approx = nearest_root              # f(x0)
    for i in range(1, n):
        binom = choose_half(i)
        term = binom * (x_0 ** (0.5 - i)) * ((user_num - x_0)**i)
        sr_approx += term
    return sr_approx


# main code

print("Choose function:")
print("Type 1 for e^x")
print("Type 2 for xpi")
print("Type 3 for sqrt(x)")

choice = int(input())

x_in = float(input("Type a number between 1 and 100 for x:"))
n_in = int(input("Type a number between 1 and 100 for the number of iterations:"))

if choice == 1:
    print(f"e^({x_in}) approximated with {n_in} Taylor expansion terms is {eul(x_in, n_in)}")
elif choice == 2:
    print(f"pi*({x_in}) approximated with {n_in} Taylor expansion terms is {xpi(x_in, n_in)}")
elif choice == 3:
    print(f"sqrt({x_in}) approximated with {n_in} Taylor expansion terms is {sqt(x_in, n_in)}")
else:
    print("Invalid choice")
