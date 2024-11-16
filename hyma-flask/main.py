from flask import Flask,render_template,request,redirect,url_for
import sqlite3
app=Flask(__name__)

@app.route('/')
def front_page():
    return render_template('front_page.html')

def get_placement_data():
    with sqlite3.connect("placements.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM placements ORDER BY year DESC")
        placement_data = cur.fetchall()
    return placement_data

@app.route('/student')
def student_page():
    placement_data = get_placement_data()
    return render_template('student.html', placements=placement_data)

@app.route('/student-login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        rollno = request.form.get("rollno")
        pwd = request.form.get("password")

        # Connect to the database and fetch the password for the provided roll number
        with sqlite3.connect("student1.db") as con:
            cur = con.cursor()
            cur.execute("SELECT password FROM student1 WHERE rollno = ?", (rollno,))
            row = cur.fetchone()
            if row is None:
                # Invalid user
                return render_template('studentlogin.html', info='Invalid user')
            elif row[0] != pwd:
                # Invalid password
                return render_template('studentlogin.html', info='Invalid password')
            else:
                # Valid login, fetch student info
                cur.execute("SELECT * FROM student1 WHERE rollno = ?", (rollno,))
                student_info = cur.fetchone()

                if student_info:
                    # Convert the student info to a dictionary
                    student_info_dict = dict(zip([column[0] for column in cur.description], student_info))
                    return render_template("studentinfo.html", row=student_info_dict)
                else:
                    return render_template('studentlogin.html', info='No student record found')
    # For GET requests or if no form is submitted, just render the login page without info
    return render_template('studentlogin.html')

@app.route('/student-signup')
def student_signup():
    return render_template('studentsignup.html')

@app.route("/savedetails",methods=["POST","GET"])
def saveDetails():
    msg="msg"
    if request.method=="POST":
        try:
            username=request.form["username"]
            password=request.form["password"]
            rollno=request.form["rollno"]
            branch=request.form["branch"]
            gender=request.form["gender"]
            seattype=request.form["seattype"]
            laststudied=request.form["laststudied"]
            studentphone=request.form["studentphone"]
            email=request.form["email"]
            semester=request.form["semester"]
            dob=request.form["dob"]
            religion=request.form["religion"]
            rank=request.form["rank"]
            caste=request.form["caste"]
            joiningdate=request.form["joiningdate"]
            Aadhar=request.form["Aadhar"]
            address=request.form["address"]
            school=request.form["school"]
            board=request.form["board"]
            tenhall=request.form["tenhall"]
            tenyear=request.form["tenyear"]
            tenmarks=request.form["tenmarks"]
            tenaddress=request.form["tenaddress"]
            intercollege=request.form["intercollege"]
            student_group = request.form["student_group"]
            interhall = request.form["interhall"]
            interyear = request.form["interyear"]
            intermarks = request.form["intermarks"]
            interaddress = request.form["interaddress"]
            
            # Parent/Guardian details
            relationship = request.form["relationship"]
            # Check if Parent or Guardian
            if relationship == "parents":
                father = request.form["father"]
                fathermobile = request.form["fathermobile"]
                fatheroccupation = request.form["fatheroccupation"]
                fathereducation = request.form["fathereducation"]
                mother = request.form["mother"]
                mothermobile = request.form["mothermobile"]
                motheroccupation = request.form["Motheroccupation"]
                mothereducation = request.form["mothereducation"]
                income = request.form["income"]
                paraddress = request.form["paraddress"]
            else:
                guname = request.form["guname"]
                gumobile = request.form["gumobile"]
                guocc = request.form["guocc"]
                guedu = request.form["guedu"]
                guaddress = request.form["guaddress"]
            '''
            # Insert into database
            with sqlite3.connect("student1.db") as con:
                cur = con.cursor()
                cur.execute("""
                    INSERT into student1 (
                        username, password, rollno, branch, gender, seattype, laststudied, studentphone, email, semester, dob,
                        religion, rank, caste, joiningdate, Aadhar, address, school, board, tenhall, tenyear, tenmarks, tenaddress,
                        intercollege, group, interhall, interyear, intermarks, interaddress,
                        relationship, father, fathermobile, fatheroccupation, fathereducation, mother, mothermobile, motheroccupation, 
                        mothereducation, income, paraddress, guname, gumobile, guocc, guedu, guaddress
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    username, password, rollno, branch, gender, seattype, laststudied, studentphone, email, semester, dob,
                    religion, rank, caste, joiningdate, Aadhar, address, school, board, tenhall, tenyear, tenmarks, tenaddress,
                    intercollege, group, interhall, interyear, intermarks, interaddress,
                    relationship, father if relationship == "Parent" else None, fathermobile if relationship == "Parent" else None,
                    fatheroccupation if relationship == "parents" else None, fathereducation if relationship == "parents" else None,
                    mother if relationship == "parents" else None, mothermobile if relationship == "parents" else None,
                    motheroccupation if relationship == "parents" else None, mothereducation if relationship == "parents" else None,
                    income if relationship == "parents" else None, paraddress if relationship == "parents" else None,
                    guname if relationship == "Guardian" else None, gumobile if relationship == "Guardian" else None,
                    guocc if relationship == "Guardian" else None, guedu if relationship == "Guardian" else None,
                    guaddress if relationship == "Guardian" else None
                ))
                con.commit()'''
            with sqlite3.connect("student1.db") as con:
                cur=con.cursor()
                cur.execute("INSERT into student1(username,password,rollno,branch,gender,seattype,laststudied,studentphone,email,semester,dob,religion,rank,caste,joiningdate,Aadhar,address,school,board,tenhall,tenyear,tenmarks,tenaddress,intercollege,student_group,interhall,interyear,intermarks,interaddress,relationship, father, fathermobile, fatheroccupation, fathereducation, mother, mothermobile, motheroccupation, mothereducation, income, paraddress, guname, gumobile, guocc, guedu, guaddress) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(username,password,rollno,branch,gender,seattype,laststudied,studentphone,email,semester,dob,religion,rank,caste,joiningdate,Aadhar,address,school,board,tenhall,tenyear,tenmarks,tenaddress,intercollege,student_group,interhall,interyear,intermarks,interaddress,relationship,father if relationship == "parents" else None, fathermobile if relationship == "parents" else None,
                    fatheroccupation if relationship == "parents" else None, fathereducation if relationship == "parents" else None,
                    mother if relationship == "parents" else None, mothermobile if relationship == "parents" else None,
                    motheroccupation if relationship == "parents" else None, mothereducation if relationship == "parents" else None,
                    income if relationship == "parents" else None, paraddress if relationship == "parents" else None,
                    guname if relationship == "Guardian" else None, gumobile if relationship == "Guardian" else None,
                    guocc if relationship == "Guardian" else None, guedu if relationship == "Guardian" else None,
                    guaddress if relationship == "Guardian" else None))
                con.commit()
                msg="Student Successfully added"
        except:
            con.rollback()
            msg="we can not add the Student details to the list,Student details already exists"
        finally:
            con=sqlite3.connect("student1.db")
            con.row_factory=sqlite3.Row
            cur=con.cursor()
            cur.execute("SELECT * FROM student1 WHERE rollno = ?", (rollno,))
            row=cur.fetchone()
            return render_template("studentinfo.html",row=row)
            #return redirect(url_for('studentinfo'))

if __name__=='__main__':
    app.run(debug=True)