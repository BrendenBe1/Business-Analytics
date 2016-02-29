__author__ = 'Brenden'
import random
import sqlite3

conn = sqlite3.connect('Test.db')
c = conn.cursor()

# Pick what to run
GENERATE_DATA = True
printCustomer = True
printItems = True
printCounters = False
printEmployees = True

# Per category, do not go above 1000
numOfItems = 1000

#numOfCustomers = 10000
numOfCustomers = 10
numOfEmployees = 50

# Generate a list of random product IDs
def generateProducts(numOfItems):

    # Holds all product IDs
    IDList = []

    # Creates X number of items in each category
    for i in range(numOfItems):

        while True:
            temp = random.randint(10000, 20000)  # Random ID makes it more realistic if the store changed stock frequently, but not necessary
            if temp in IDList:  # Item already created
                continue
            else:
                IDList.append(temp)  # Add item
                break

        while True:
            temp = random.randint(20000, 30000)
            if temp in IDList:
                continue
            else:
                IDList.append(temp)
                break

        while True:
            temp = random.randint(30000, 40000)
            if temp in IDList:
                continue
            else:
                IDList.append(temp)
                break

        while True:
            temp = random.randint(40000, 50000)
            if temp in IDList:
                continue
            else:
                IDList.append(temp)
                break

        while True:
            temp = random.randint(50000, 60000)
            if temp in IDList:
                continue
            else:
                IDList.append(temp)
                break

        while True:
            temp = random.randint(60000, 70000)
            if temp in IDList:
                continue
            else:
                IDList.append(temp)
                break

    # Sort for easy selection
    IDList.sort()

    if printItems:
        print("\nAll items in store:")
        print(IDList)
        print()


        for i in range(len(IDList)):
            c.execute("INSERT INTO Products (ProductID) VALUES (?)", (IDList[i],))
            conn.commit()

    return IDList


def generatePurchases(IDList, numOfPurchases, numOfItems, food, medical, electronics, outdoors, clothing, beauty, customer):
    customerPurchases = []

    # Customer is *likely* to buy from some categories, but anything can happen
    weighted_categories = [('Food', food), ('Medical', medical), ('Electronics', electronics), ('Outdoors', outdoors), ('Clothing', clothing), ('Beauty', beauty)]
    randomCategory = [val for val, cnt in weighted_categories for i in range(cnt)]

    for i in range(numOfPurchases):

        choice = random.choice(randomCategory)

        if choice == 'Food':

            tempIndex = random.randint(0, numOfItems-1)
            while str(IDList[tempIndex])[0] != '1':
                tempIndex = random.randint(0, numOfItems-1)
            customerPurchases.append(IDList[tempIndex])

        elif choice == 'Medical':
            tempIndex = random.randint(numOfItems, 2*numOfItems-1)
            while str(IDList[tempIndex])[0] != '2':
                tempIndex = random.randint(numOfItems, 2*numOfItems-1)
            customerPurchases.append(IDList[tempIndex])

        elif choice == 'Electronics':
            tempIndex = random.randint(2*numOfItems, 3*numOfItems-1)
            while str(IDList[tempIndex])[0] != '3':
                tempIndex = random.randint(2*numOfItems, 3*numOfItems-1)
            customerPurchases.append(IDList[tempIndex])

        elif choice == 'Outdoors':
            tempIndex = random.randint(3*numOfItems, 4*numOfItems-1)
            while str(IDList[tempIndex])[0] != '4':
                tempIndex = random.randint(3*numOfItems, 4*numOfItems-1)
            customerPurchases.append(IDList[tempIndex])

        elif choice == 'Clothing':
            tempIndex = random.randint(4*numOfItems, 5*numOfItems-1)
            while str(IDList[tempIndex])[0] != '5':
                tempIndex = random.randint(4*numOfItems, 5*numOfItems-1)
            customerPurchases.append(IDList[tempIndex])

        elif choice == 'Beauty':
            tempIndex = random.randint(5*numOfItems, 6*numOfItems-1)
            while str(IDList[tempIndex])[0] != '6':
                tempIndex = random.randint(5*numOfItems, 6*numOfItems-1)
            customerPurchases.append(IDList[tempIndex])

    #if printCustomer:
     #   print(customerPurchases)
    return customerPurchases

def generateEmployees(numOfEmployees):
    # Name
    maleNames = ['Perry Lovan', 'Horacio Arvidson', 'Gale Skipworth', 'Joshua Lodge', 'Noble Shutter', 'Kristopher Talor', 'Jarod Harrop', 'Joan Henrichs', 'Wilber Vitiello', 'Clayton Brannum', 'Joel Sennett', 'Wiley Maffei', 'Clemente Flore', 'Cliff Saari', 'Miquel Plamondon', 'Erwin Broadus', 'Elvin Defibaugh', 'Ramon Vaquera', 'Roberto Koval', 'Micah Sumter', 'Wyatt Cambareri', 'Jamal Delarosa', 'Franklyn Hayles', 'Riley Haslett', 'Robt Fincher', 'Abraham Denzer', 'Darius Jude', 'Phillip Sunderman', 'August Kindel', 'Jospeh Mawson', 'Damion Postma', 'Gregorio Pasco', 'Rosendo Downing', 'Chance Plascencia', 'Jewell Pankratz', 'Jerrell Tarrance', 'Michal Bliss', 'Josue Larocque', 'Aaron Harpster', 'Zack Hildebrant', 'Frank Souders', 'Lindsay Bechard', 'Agustin Marks', 'Mathew Fredericksen', 'Ivan Hanline', 'Michael Otto', 'Max Oberlander', 'Ricky Mckellar', 'Bernard Friedt', 'King Lorentzen']
    femaleNames = ['Lorretta Vansickle', 'Loura Steimle', 'Neomi Fritz', 'Vernie Vanderveen', 'Dede Poehler', 'Margarete Espinoza', 'Leda Leonardo', 'Fae Strand', 'Nichol Winford', 'Danika Ridgeway', 'Elvira Balentine', 'Sharell Xie', 'Sheree Booker', 'Emely Conine', 'Justina Kleve', 'Pia Maxton', 'Sophia Lark', 'Nilsa Albee', 'Felipa Seman', 'Jeraldine Watkins', 'Susann Sowards', 'Asha Irion', 'Shay Koran', 'Rosio Jahn', 'Rachal Slaven', 'Beryl Byron', 'Jona Lira', 'Margert Strite', 'Talia Beauregard', 'Jacqueline Vella', 'Rolande Mccready', 'Margret Hickerson', 'Precious Confer', 'Evita Nicolai', 'Fredda Groner', 'Laquanda Bracken', 'Alana Saddler', 'Melania Harring', 'Shae Everette', 'Marlyn Mcfalls', 'Madeline Nicols', 'Fonda Webster', 'Fumiko Steffy', 'Virginia Sprinkle', 'Lula Frisch', 'Mari Mulherin', 'Alecia Remillard', 'Jeanna Halderman', 'Ocie Waldrep', 'Theresa Knouse']

    for i in range(numOfEmployees):
        # Clock in an hour before opening, 6 hours after, or 12 hours after
        clockIn = random.choice([7, 13, 19])

        # Clock out after 5 hours, 10 hours, or 15 hours
        clockOut = random.choice([13, 19, 23])
        while clockOut <= clockIn:
            clockOut = random.choice([13, 19, 23])

        # Hourly wage
        wage = random.choice([8, 9, 10, 12, 20])

        gender = random.choice(['M', 'F'])
        if gender == 'M':
            name = random.choice(maleNames)
        else:
            name = random.choice(femaleNames)

        if printEmployees:
            print("\nName:", name)
            print("Clock in:", clockIn)
            print("Clock out:", clockOut)
            print("Wage:", wage)
            c.execute("INSERT INTO Employee (Name, ClockIn, ClockOut, Wage) VALUES (?, ?, ?, ?)",
                      (name, clockIn, clockOut, wage))

            conn.commit()
        # Database.update clock in
        # Database.update clock out
        # Database.update wage
        # Database.update name

# Customer data generation (weighted randoms = define our own trends without being obvious)
def generateCustomers(numOfCustomers):

    # Counters
    shoppers = 0
    models = 0
    oldl = 0
    oldf = 0
    doctor = 0
    nudist = 0
    hippie = 0
    nerd = 0

    allCustomers = {}
    customerAttributes = []

    for i in range(numOfCustomers):

        # With these weights, our store has plenty of youngs and olds, but few mids
            # Most grocery shoppers come in the evening
            # Young people have equal distribution between morning and evening
            # etc
        age1 = random.randint(18, 28)
        age2 = random.randint(28, 50)
        age3 = random.randint(50, 85)
        weighted_ages = [(age1, 10), (age2, 2), (age3, 15)]
        randomAge = [val for val, cnt in weighted_ages for a in range(cnt)]

        hour1 = random.randint(8, 13)
        hour2 = random.randint(13, 18)
        hour3 = random.randint(18, 22)
        weighted_hours = [(hour1, 10), (hour2, 3), (hour3, 20)]
        randomHour = [val for val, cnt in weighted_hours for b in range(cnt)]

        age = random.choice(randomAge)
        hour = random.choice(randomHour)
        gender = random.choice(['M', 'M', 'M', 'M', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'])

        # Base chances, 100 total
        gs, sm, hp, ol, nrd, of, sd, nud = 20, 5, 5, 5, 5, 5, 10, 10

        customerID = random.randint(0, numOfCustomers*2)
        while customerID in allCustomers:
            customerID = random.randint(0, numOfCustomers*2)

        # Weights
        if 18 < age < 22:
            if gender == 'M':
                if 8 <= hour <= 12:
                    ol, sm, nrd, hp = 2, 2, 35, 20
                elif 13 <= hour <= 17:
                    ol, sm, nrd, hp, gs = 2, 2, 15, 30, 5
                elif 18 <= hour <= 22:
                    ol, sm, gs = 2, 2, 50

            elif gender == 'F':
                if 8 <= hour <= 12:
                    ol, sm, nrd = 5, 35, 15
                elif 13 <= hour <= 17:
                    ol, sm, hp = 5, 30, 30
                elif 18 <= hour <= 22:
                    ol, sm, gs, = 5, 25, 50

        elif gender == 'M' and 22 < age < 29:
            if 8 <= hour <= 12:
                ol, sm, nrd, hp = 5, 5, 35, 25
            elif 13 <= hour <= 17:
                ol, sm, nrd, hp = 5, 5, 35, 40
            elif 18 <= hour <= 22:
                ol, sm, nrd, hp, gs = 5, 5, 20, 20, 50

        elif gender == 'M' and 29 < age < 50:
            if 8 <= hour <= 12:
                ol, sm, nrd, gs = 5, 5, 40, 30
            elif 13 <= hour <= 17:
                ol, sm, nrd = 5, 5, 30
            elif 18 <= hour <= 22:
                ol, sm, gs = 5, 5, 70

        elif gender == 'M' and age > 50:
            if 8 <= hour <= 12:
                ol, sm, gs, of, hp = 5, 5, 30, 60, 20
            elif 13 <= hour <= 17:
                ol, sm, gs, of, hp = 5, 5, 15, 70, 20
            elif 18 <= hour <= 22:
                ol, sm, gs, of, hp = 5, 5, 50, 25, 20

        elif gender == 'F' and 22 < age < 35:
            if 8 <= hour <= 12:
                ol, sm, hp, gs = 5, 30, 30, 30
            elif 13 <= hour <= 17:
                ol, sm, hp, gs = 5, 30, 30, 15
            elif 18 <= hour <= 22:
                ol, sm, hp, gs = 5, 15, 25, 60

        elif gender == 'F' and 35 < age < 55:
            if 8 <= hour <= 12:
                ol, sm, hp, gs = 5, 5, 5, 40
            elif 13 <= hour <= 17:
                ol, sm, hp, gs = 25, 5, 5, 25
            elif 18 <= hour <= 22:
                ol, sm, hp, gs = 30, 5, 5, 40

        elif gender == 'F' and age > 55:
            if 8 <= hour <= 12:
                ol, sm, of, gs = 20, 5, 15, 30
            elif 13 <= hour <= 17:
                ol, sm, of, gs = 60, 5, 30, 15
            elif 18 <= hour <= 22:
                ol, sm, of, gs = 40, 5, 20, 40

        weighted_choices = [('Grocery Shopper', gs), ('Supermodel', sm), ('Hippie', hp), ('Old Lady', ol), ('Nerd', nrd), ('Self Doctor', sd), ('Nudist', nud), ('Old Fart', of)]
        randomType = [val for val, cnt in weighted_choices for n in range(cnt)]

        customer = random.choice(randomType)

        if customer == 'Grocery Shopper':
            shoppers += 1
            numOfPurchases = random.randint(0, 50)
            foodChance = 18
            medicalChance = 3
            electronicsChance = 1
            outdoorsChance = 1
            clothingChance = 1
            beautyChance = 2
            allCustomers[customerID] = [age, gender, hour, customer, generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)]
            temp = generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)


        elif customer == 'Supermodel':
            models += 1
            numOfPurchases = random.randint(0, 50)
            foodChance = 0
            medicalChance = 5
            electronicsChance = 0
            outdoorsChance = 0
            clothingChance = 10
            beautyChance = 13
            allCustomers[customerID] = [age, gender, hour, customer, generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)]
            temp = generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)


        elif customer == 'Hippie':
            hippie += 1
            numOfPurchases = random.randint(0, 50)
            foodChance = 6
            medicalChance = 2
            electronicsChance = 1
            outdoorsChance = 14
            clothingChance = 7
            beautyChance = 1
            allCustomers[customerID] = [age, gender, hour, customer, generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)]
            temp = generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)
            #print(temp)

        elif customer == 'Old Lady':
            oldl += 1
            numOfPurchases = random.randint(0, 50)
            foodChance = 6
            medicalChance = 8
            electronicsChance = 0
            outdoorsChance = 0
            clothingChance = 3
            beautyChance = 10
            allCustomers[customerID] = [age, gender, hour, customer, generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)]
            temp = generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)
            #print(temp)

        elif customer == 'Nerd':
            nerd += 1
            numOfPurchases = random.randint(0, 50)
            foodChance = 4
            medicalChance = 3
            electronicsChance = 14
            outdoorsChance = 0
            clothingChance = 2
            beautyChance = 1
            allCustomers[customerID] = [age, gender, hour, customer, generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)]
            temp = generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)
            #print(temp)

        elif customer == 'Self Doctor':
            doctor += 1
            numOfPurchases = random.randint(0, 50)
            foodChance = 5
            medicalChance = 32
            electronicsChance = 4
            outdoorsChance = 1
            clothingChance = 2
            beautyChance = 1
            allCustomers[customerID] = [age, gender, hour, customer, generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)]
            temp = generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)
            #print(temp)

        elif customer == 'Nudist':
            nudist += 1
            numOfPurchases = random.randint(0, 50)
            foodChance = 10
            medicalChance = 5
            electronicsChance = 0
            outdoorsChance = 14
            clothingChance = 0
            beautyChance = 0
            allCustomers[customerID] = [age, gender, hour, customer, generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)]
            temp = generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)
            #print(temp)

        elif customer == 'Old Fart':
            oldf += 1
            numOfPurchases = random.randint(0, 50)
            foodChance = 10
            medicalChance = 18
            electronicsChance = 5
            outdoorsChance = 3
            clothingChance = 3
            beautyChance = 0
            allCustomers[customerID] = [age, gender, hour, customer, generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)]
            temp = generatePurchases(completeIDList, numOfPurchases, numOfItems, foodChance, medicalChance, electronicsChance, outdoorsChance, clothingChance, beautyChance, customer)
            #print(temp)

        if printCustomer:
            itemsBought = (", ".join(repr(e) for e in temp))

            #print(itemsBought)

            c.execute("INSERT INTO Customer (CustomerID, Hour, Age, Gender, Items) VALUES (?, ?, ?, ?, ?)",
                      (customerID, hour, age, gender, itemsBought))

            conn.commit()
    if printCounters:
        print("\nShoppers:", shoppers)
        print("Models:", models)
        print("Old Ladies:", oldl)
        print("Old Farts:", oldf)
        print("Self doctors:", doctor)
        print("Nerds:", nerd)
        print("Hippies:", hippie)
        print("Nudists:", nudist)

    if printCustomer:
        print("\nRaw Customer Data: ")
        print(allCustomers)
        itemsBought = (", ".join(repr(e) for e in temp))

        #print(itemsBought)

        c.execute("INSERT INTO Customer (CustomerID, Hour, Age, Gender, Items) VALUES (?, ?, ?, ?, ?)",
                  (customerID, hour, age, gender, itemsBought))

        conn.commit()


    return allCustomers

# Run app
if GENERATE_DATA:
    completeIDList = generateProducts(numOfItems)
    generateEmployees(numOfEmployees)
    generateCustomers(numOfCustomers)

c.close()
conn.close()

