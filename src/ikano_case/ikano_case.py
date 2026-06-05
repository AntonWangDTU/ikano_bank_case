"""ikano_case."""

import argparse


# F(n) = F(n-1) + F(n-2), \quad F(0)=0,\ F(1)=1$
def fibo(n):

    # Erro handling
    if n < 0:
        raise ValueError("n must be non negative")
    if type(n) is not int:
        raise ValueError("n must be non negative integer")

    # Switch to loop version for higher n's
    if n > 30:
        x, y, z = 0, 1, 1
        for i in range(n):
            x = z
            y = z
            z = x + y
        return x
    # Recursive mode elegant but slower
    else:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return fibo(n - 1) + fibo(n - 2)


# n! = n \times (n-1)!, \quad 0! = 1


def fact(n):

    # Error handling
    if n < 0:
        raise ValueError("n must be non negative")
    if type(n) is not int:
        raise ValueError("n must be non negative integer")

    if n == 0:
        return 1

    return n * fact(n - 1)


def loan(P: float, r: float, n: int):

    # Error handling
    if r <= 0:
        raise ValueError("interest cannot be 0 or less in our equation")
    if P <= 0 or n <= 0:
        raise ValueError("We must have a principal and a number of months we will pay")

    M = P * (r * (1 + r) ** n / ((1 + r) ** n - 1))

    # More error handling
    if M < P * r:
        raise ValueError("Payment too small to cover monthly interest")

    return round(M, 2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="function")

    # Fibonacci subparser
    fibo_parser = subparsers.add_parser("fibo")
    fibo_parser.add_argument("--n", type=int, required=True)

    # Factorial subparser
    fact_parser = subparsers.add_parser("fact")
    fact_parser.add_argument("--n", type=int, required=True)

    # Loan interest subparser subparser
    loan_parser = subparsers.add_parser("loan")
    loan_parser.add_argument("--P", type=float, required=True)
    loan_parser.add_argument("--r", type=float, required=True)
    loan_parser.add_argument("--n", type=int, required=True)

    args = parser.parse_args()

    if args.function == "fibo":
        print(fibo(args.n))
    elif args.function == "fact":
        print(fact(args.n))
    elif args.function == "loan":
        print(loan(args.P, args.r, args.n))
