def full_name():
    assemble = input("what is your name: ")
    desemble = input("what is your last name: ")
    name = f"{assemble} {desemble}"
    return name

sort_name = full_name()
print(sort_name)
