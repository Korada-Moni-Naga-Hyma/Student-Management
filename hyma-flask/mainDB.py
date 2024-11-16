import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
con = sqlite3.connect("student1.db")
print("Database opened successfully")

# Create a new table called Student1 with the specified columns
con.execute("""
    CREATE TABLE IF NOT EXISTS Student1 (
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        rollno TEXT UNIQUE PRIMARY KEY,
        branch TEXT NOT NULL,
        gender TEXT,
        seattype TEXT,
        laststudied TEXT,
        studentphone TEXT,
        email TEXT,
        semester TEXT,
        dob TEXT,
        religion TEXT,
        rank TEXT,
        caste TEXT,
        joiningdate TEXT,
        Aadhar TEXT,
        address TEXT,
        school TEXT,
        board TEXT,
        tenhall TEXT,
        tenyear TEXT,
        tenmarks TEXT,
        tenaddress TEXT,
        intercollege TEXT,
        student_group TEXT,           
        interhall TEXT,
        interyear TEXT,
        intermarks TEXT,
        interaddress TEXT,
        relationship TEXT,
        father TEXT,
        fathermobile TEXT,
        fatheroccupation TEXT,
        fathereducation TEXT,
        mother TEXT,
        mothermobile TEXT,
        motheroccupation TEXT,
        mothereducation TEXT,
        income TEXT,
        paraddress TEXT,
        guname TEXT,
        gumobile TEXT,
        guocc TEXT,
        guedu TEXT,
        guaddress TEXT
    )
""")

print("Table created successfully")

# Close the database connection
con.close()


'''con.execute("create table Student1(username TEXT NOT NULL,password TEXT NOT NULL,rollno TEXT UNIQUE PRIMARY KEY,branch TEXT NOT NULL,gender TEXT,seattype TEXT,laststudied TEXT,studentphone TEXT,email TEXT,semester TEXT,dob TEXT,religion TEXT,rank TEXT,caste TEXT,joiningdate TEXT,Aadhar TEXT,address TEXT,school TEXT,board TEXT,tenhall TEXT,tenyear TEXT,tenmarks TEXT,tenaddress TEXT)")

print("TABLE created successfully")

con.close()
'''
# Creating the Placements database and table
con = sqlite3.connect("placements.db")
print("Placements database opened successfully")

con.execute("""
CREATE TABLE IF NOT EXISTS placements(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER,
    student_name TEXT,
    company TEXT,
    position TEXT,
    salary TEXT
)
""")
print("Placements table created successfully")

# Insert example data into the placements table
con.executescript("""
INSERT INTO placements (year, student_name, company, position, salary) VALUES 
(2022, 'Alice Johnson', 'TechCorp', 'Software Engineer', '$70,000'),
(2021, 'Bob Smith', 'DataWorks', 'Data Analyst', '$65,000'),
(2020, 'Charlie Davis', 'WebSolutions', 'Frontend Developer', '$60,000'),
(2019, 'Ravi', 'WebSolutions', 'Frontend Developer', '$60,000'),
(2018, 'Davis', 'WebSolutions', 'Frontend Developer', '$60,000'),
(2017, 'Charlie ', 'WebSolutions', 'Frontend Developer', '$60,000');
""")
print("Example data inserted into placements table")

# Commit changes and close the connection
con.commit()
con.close()
