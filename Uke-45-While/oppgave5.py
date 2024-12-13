exit1 = False

def is_num(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def can_div(dividend, divisor):
    if dividend % divisor == 0:
        return True

while not exit1:
    år = input("År: ")
    if is_num(år):
        år = int(år)
        if can_div(år, 4) and not can_div(år, 100):
            print(f"{år} er et skudår.")
        elif can_div(år, 400):
            print(f"{år} er et skudår.")
        else:
            print(f"{år} er ikke et skudår.")
    elif år == "cmd":
        år = input("cmd/: ")
        match år:
            case "close":
                exit1 = True
    else:
        print("Ugyldig")