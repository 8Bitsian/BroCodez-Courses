# Exercise 14: Shipping Label - Print a shipping label using arbitrayr arguments within a function
# 21 Notes

# Positional arguments must be first
def ship_label(*args, **kwargs):
    # Output your full name
    for arg in args:
        print(arg, end = " ")
    print()

    # Output address on one line:
    # for value in kwargs.values():
    #     print(value, end = " ")

    if "apt" in kwargs:
        print(f"{kwargs.get("street")} {kwargs.get("apt")}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get("street")}")
        print(f"{kwargs.get("pobox")}")
    else:
        print(f"{kwargs.get("street")}")

    print(f"{kwargs.get("city")} {kwargs.get("state")}")
    print(f"{kwargs.get("zip")}")

# Pass in mix of arbitrary positional arguments (*args) and then keyword arguments (**kwargs)
ship_label("Ms.", "8Bit", "Software",
           street = "123 Fake St.",
           pobox = "PO Box #7890",
           city = "Atlanta",
           state = "GA",
           zip = "78901")