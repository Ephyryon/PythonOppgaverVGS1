import random

job = False
job_type = 0
exit1 = False

saturation = 10
hungry = False

fatigue = 0
exhausted = False

cashier = 150
barista = 250
office_worker = 200

hour = 7

pocket = 0
bank = 0

actions = ["/work", "/eat", "/sleep", "/deposit", "/withdraw", "/balance", "/apply-job", "/quit"]
jobs = ["cashier", "barista", "office worker"]
fail_check = [1, 2, 3, 4, 5]

def check_input(input_value, list_of_lists):
    for sublist in list_of_lists:
        if input_value in sublist:
            return True
    return False

def cashier1():
    global pocket
    global hour
    global job
    global job_type
    work = input("You need to restock. Do it propperly or quickly? : ").lower()
    match work:
        case "propperly":
            print(f"You finish restocking without any issues. +{cashier}kr, hour={hour}")
            pocket += cashier
            hour += 7
        case "quickly":
            check = random.choice(fail_check)
            match check:
                case 1:
                    print(f"You finished work quickly without fail. +{cashier}kr, hour={hour}")
                    pocket += cashier
                    hour += 4
                case 2:
                    print(f"You misplaced a few items causing your boss to make you restock again. +{cashier}kr, hour={hour}")
                    pocket += cashier
                    hour += 8
                case 3:
                    print(f"You dropped a few boxes. The boss deducted the damages from your pay. +{cashier - 50}kr, hour={hour}")
                    pocket += (cashier - 50)
                    hour += 6
                case 4:
                    print(f"You tried to pick up many items at once, but you failed. +{cashier}kr, hour={hour}")
                    pocket += cashier
                    hour += 6
                case 5:
                    print(f"You slipped while running. As you fell the box with tomatosauce you were carrying hit the boss in the back. He fired you. -job, +unemployed, hour={hour}")
                    hour += 4
                    job = False
                    job_type = 0
def cashier2():
    print("You stand at the register today.")
    work = random.choice(fail_check)
    match work:
        case 1:
            print("Someone comes over complaining that someone is stealing.")
            print("What do you do?")
            print("-Ignore")
            print("")
    

cashier_shifts = ["cashier1"]

def work_shift():
    if job_type == 1:
        work = random.choice(cashier_shifts)
        match work:
            case "cashier1":
                cashier1()

def sleep():
    global hour
    global fatigue
    global exhausted
    hours = [1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 10]
    if exhausted:
        print("You fell asleep immediately. You slept 10 hours.")
        hour += 10
        fatigue -= fatigue
        exhausted = False
    else:
        sleep = random.choice(hours)
        print(f"You slept for {sleep} hours.")
        hour += sleep
        fatigue -= 5
        if fatigue < 0:
            fatigue = 0

while not exit1:
    action1 = input(f"Time: {hour}  Satiation: {saturation}  Fatigue: {fatigue}  Action: ").lower()
    if check_input(action1, actions):
        match action1:
            case "/work":
                work_shift()
            case "/eat":
                if hungry:
                    saturation += 2
            case "/sleep":
                sleep()
            case "/deposit":
                deposit = int(input("How much do you want to deposit? : "))
                if deposit <= pocket:
                    pocket -= deposit
                    bank += deposit
                    print(f"{deposit}kr added to account. Balance: {bank}kr  Cash: {pocket}kr")
                else:
                    print("You dont have that much.")
            case "/withdraw":
                withdraw = int(input("How much do you want to withdraw? : "))
                if withdraw <= bank:
                    pocket += withdraw
                    bank -= withdraw
                    print(f"{withdraw}kr has been withdrawn from bank. Balance: {bank}kr  Cash: {pocket}kr")
                else:
                    print("You don't have that much in your bank.")
            case "/balance":
                print(f"Bank: {bank}kr  Cash: {pocket}kr")
            case "/apply-job":
                apply = input(f"Available jobs: {jobs} : ").lower()
                if check_input(apply, jobs):
                    match apply:
                        case "cashier":
                            job_type = 1
                            job = True
                            print("You're now a cashier. Income: 150kr")
                        case "barista":
                            job_type = 2
                            job = True
                        case "office worker":
                            job_type = 3
                            job = True
            case "/quit":
                exit1 = True