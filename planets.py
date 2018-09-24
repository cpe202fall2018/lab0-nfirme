def weight_on_planets():
    weight = input("What is your weight on earth? ")
    earthWeight = int(weight)
    marsWeight = earthWeight * 0.38
    jupWeight = earthWeight * 2.34

    print()
    print("On Mars you would weigh " + str(marsWeight) + " pounds.")
    print("On Jupiter you would weigh " + str(jupWeight) + " pounds.")





if __name__ == '__main__':
    weight_on_planets()
