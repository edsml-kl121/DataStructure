# a,b, ..., z
# distance a -> b = 5, z -> a = 15
# fuel 1
# dist. = 5, fuel =


def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    current_fuel = 0
    for i in range(len(fuel)):
        city_passed = 0
        # print(fuel[0])
        print(fuel)
        for j in range(len(fuel)):
            # print(current_fuel, mpg, fuel[j], distances[j])
            current_fuel = current_fuel + mpg * fuel[j] - distances[j]
            if i==6:
              print(current_fuel)
            if current_fuel < 0:
                pass
            else:
                city_passed += 1
        # print(city_passed, i)
        last = fuel.pop(0)
        fuel.append(last)
        last = distances.pop(0)
        distances.append(last)
        if city_passed == len(fuel):
            return i

distances = [1, 3, 10, 6, 7, 7, 2, 4]
fuel = [1, 1, 1, 1, 1, 1, 1, 1]
mpg = 5
print(validStartingCity(distances, fuel, mpg))

# 3
# 4
# 8
# 10
# 5
# 4
# 2