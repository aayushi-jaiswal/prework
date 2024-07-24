import sqlite3
import sys


def connect_to_database():
    try:
        conn = sqlite3.connect('assignment.db')
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Error not able to connect to the SQLite database: Try again! {e}")
        sys.exit(1)

def searchNames(searchString):
    conn, cursor = connect_to_database()
    cursor.execute("SELECT name, marks FROM students WHERE UPPER(name) LIKE ?", ('%' + searchString.upper() + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def main():
    while True:
        searchString = input("Enter a search string (or 'quit' to exit): ").strip()
        
        if searchString.lower() == 'quit':
            print("Quitting the program!")
            break
        
        if searchString == "":
            print("Please enter a search string")
            continue
        
        
        results = searchNames(searchString)
        
        if not results:
            print("No matching records found, Try another one!")
        else:
            total_marks = 0
            count = 0
            
            print("Matching records:")
            for name, marks in results:
                print(f"Name: {name}, Marks: {marks}")
                total_marks += marks
                count += 1
            
            if count > 0:
                average_marks = total_marks / count
                print(f"Total Marks: {total_marks}")
                print(f"Average Marks: {average_marks}")
    
    print("Program finished.")

if __name__ == "__main__":
    main()
