distances = {
    "Voyager 1": "100",
    "Voyager 2": "200",
    "Voyager 3": "300 AU",
    "Voyager 4": "400",
    "Voyager 5": "500 AU",
}

def main():
    spacecraft = input("Enter a spacecraft: ")

    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"{spacecraft} is not a valid key")
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' into a float")
        return
    else:
        m = convert(au)
        print(f"{m}m away")

def convert(au):
    return au * 149597870700

main()