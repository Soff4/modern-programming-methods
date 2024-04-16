import sys

def prime_checker(num):
    try:
        num = int(num)
        if num <= 1:
            sys.stdout.write("False")
            sys.exit(1)
        else:
            for i in range(2, num):
                if (num % i) == 0:
                    sys.stdout.write("False")
                    sys.exit(1)
            sys.stdout.write("True")
            sys.exit(0)
    except (ValueError, TypeError):
        sys.stderr.write(f"Error: Введене значення '{num}' не є цілим числом.\n")
        sys.exit(1)

...