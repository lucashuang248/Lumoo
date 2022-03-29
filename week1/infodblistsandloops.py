InfoDb = []
InfoDb.append({
#list
 "Name": "Lucas Huang",
 "Birthday": "August 28",
 "Siblings": "Yes",
 "Hobbies":["Basketball”, “Eating”, “Listening to Music”, “Playing Video and Board Games"]
})
InfoDb.append({
 "Name": "Timmy Lin",
 "Birthday": "November 10",
 "Siblings": "Yes",
 "Hobbies":["Video Games”, “Pokemon GO”, “Math”,“Snowboard"]
})
def print_data(n):
    print(InfoDb[n]["Name"], InfoDb[n]["Birthday"], InfoDb[n]["Siblings"])
    print("\t", "Hobbies: ", end="")
    print(", ".join(InfoDb[n]["Hobbies"]))
    print()
#for loop
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
#while loopp
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
#recursive loop
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return
#prints the loops
def tester():
    print("For loop:")
    for_loop()
    print("While loop:")
    while_loop(0)
    print("Recursive loop:")
    recursive_loop(0)