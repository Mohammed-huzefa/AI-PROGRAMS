info={
"python":"Python is a high-level programming language.",
"ai":"Artificial Intelligence is the simulation of human intelligence by machines.",
"ml":"Machine Learning enables systems to learn from data.",
"java":"Java is an object-oriented programming language."
}

while True:
    q=input("Search: ").lower()

    if q=="exit":
        break

    if q in info:
        print(info[q])

    else:
        print("Information not found.")
