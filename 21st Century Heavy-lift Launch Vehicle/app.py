#docstring - 21st Century Heavy-lift Launch Vehicle Database Application
#import database
import sqlite3
DATABASE = 'rockets.db'


#functions
def print_all_rockets():
    #print all the rockets with their organizations and nationality
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = """
    SELECT Rockets.rocket_name, Organizations.org_name, Organizations.nationality 
    FROM Rockets 
    JOIN Organizations ON Rockets.org_id = Organizations.org_id;
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"rocket_name              organization        nationality")
    for rocket in results:
        print(f"{rocket[0]:<25}{rocket[1]:<20}{rocket[2]:<15}")
    #loop finish here
    db.close()