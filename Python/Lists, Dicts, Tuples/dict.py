def main():
    spacecraft = {"Name": "Voyager 1"}
    spacecraft.update({"Distance": 67, "Orbit": "Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ======== REPORT ========

    Name: {spacecraft.get("Name", "Unknown")}
    Distance: {spacecraft.get("Distance", "Unknown")}
    Orbit: {spacecraft.get("Orbit", "Unknown")}

    ========================
    """

main()