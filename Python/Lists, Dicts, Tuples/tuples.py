import sys

def main():
    coordinate_tuple = (42.376, -71.115)
    latitude, longitude = coordinate_tuple
    coordinate_list = [42.376, -71.115]

    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")
    print(f"Latitude: {latitude}, Longitude: {longitude}")
    print(f"Latitude: {coordinate_tuple[0]}, Longitude: {coordinate_list[1]}")

main()