#docstring - 21st Century Heavy-lift Launch Vehicle Database Application
#Import database
import sqlite3
DATABASE = "rockets.db"

#Function 1
def print_all_rockets():
    #Print all the rockets with organizations and nationality
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Rockets.rocket_name, Organizations.org_name, Organizations.nationality FROM Rockets JOIN Organizations ON Rockets.org_id = Organizations.org_id;"
    cursor.execute(sql)
    cursor.execute(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"rocket_name              organization        nationality")
    for rocket in results:
        print(f"{rocket[0]:<25}{rocket[1]:<20}{rocket[2]:<15}")
    #loop finish
    db.close()

#Function 2
def print_rockets_by_year():
    #Print rockets sorted by first launch year (from newest to oldest)
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT rocket_name, first_launch_year FROM Rockets ORDER BY first_launch_year DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"rocket_name              first_launch_year")
    for rocket in results:
        print(f"{rocket[0]:<25}{rocket[1]:<10}")
    #loop finish
    db.close()

#Function 3
def print_rockets_by_payload():
    #Print rockets sorted by LEO payload (from largest to smallest)
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT rocket_name, leo_payload_kg FROM Rockets ORDER BY leo_payload_kg DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"rocket_name              leo_payload_kg")
    for rocket in results:
        print(f"{rocket[0]:<25}{rocket[1]:<10}")
    #loop finish
    db.close()

#Function 4
def filter_rockets_by_status():
    #Filter and print rockets by user defined status
    user_input = input("Enter status (Operational/Retired): ").strip()
    
    #input validation
    if user_input not in ["Operational", "Retired"]:
        print("Invalid status. Please enter 'Operational' or 'Retired'.\n")
        return

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT rocket_name, status FROM Rockets WHERE status = ?;"
    cursor.execute(sql, (user_input,))
    results = cursor.fetchall()
    
    #check if results exist
    if not results:
        print("No rockets found with this status.\n")
    else:
        #loop through all the results
        print(f"rocket_name              status")
        for rocket in results:
            print(f"{rocket[0]:<25}{rocket[1]:<15}")
        #loop finish
    db.close()

#Function 5
def search_rockets_by_country():
    #Filter and print rockets by user defined nationality
    user_input = input("Enter country name (e.g., USA, China): ").strip()
    
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT Rockets.rocket_name, Organizations.nationality FROM Rockets JOIN Organizations ON Rockets.org_id = Organizations.org_id WHERE Organizations.nationality = ?;"
    cursor.execute(sql, (user_input,))
    results = cursor.fetchall()
    
    #check if results exist
    if not results:
        print(f"No rockets found from {user_input}. \n")
    else:
        #loop through all the results
        print(f"rocket_name              nationality")
        for rocket in results:
            print(f"{rocket[0]:<25}{rocket[1]:<15}")
        #loop finish
    db.close()

#Function 6
def search_rockets_by_min_payload():
    #Print rockets above a user defined specific LEO payload
    user_input = input("Enter minimum LEO payload (in integer, unit: kilograms): ").strip()
    
    #input validation
    try:
        min_payload = int(user_input)
    except ValueError:
        print("That is not a valid number.\n")
        return

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT rocket_name, leo_payload_kg FROM Rockets WHERE leo_payload_kg >= ?;"
    cursor.execute(sql, (min_payload,))
    results = cursor.fetchall()
    
    # check if results exist
    if not results:
        print(f"No rockets found with payload >= {min_payload} kg.\n")
    else:
        #loop through all the results
        print(f"rocket_name              leo_payload_kg")
        for rocket in results:
            print(f"{rocket[0]:<25}{rocket[1]:<10}")
        #loop finish
    db.close()

#main code
while True:
    user_input = input("""
What would you like to do.
1.Print all rockets with their organizations
2.Print all rockets sorted by first launch year (Newest to Oldest)
3.Print all rockets sorted by LEO payload (Largest to Smallest)
4.Filter rockets by status (Operational / Retired)
5.Search rockets by country
6.Search rockets above specific LEO payload
7.Exit.
""")
    
    if user_input == "1":
        print_all_rockets()
    elif user_input == "2":
        print_rockets_by_year()
    elif user_input == "3":
        print_rockets_by_payload()
    elif user_input == "4":
        filter_rockets_by_status()
    elif user_input == "5":
        search_rockets_by_country()
    elif user_input == "6":
        search_rockets_by_min_payload()
    elif user_input == "7":
        break
    else:
        print("That is not an option!\n")