print("""HELLO!!! WELCOME TO THE CST CINEMA HALL !!!
                         REGISTRATION  
      ----->  Please enter the deteils below!!!! """)
name_ =str(input("Enter your name: "))
print ("WELCOME",name_)
std_ = int(input("""Are you a student ??
                # If Yes Enter--> (1)
                # If No Enter-->  (2)
                 ------->>>"""))
x = name_
if std_==1:
    age_= int(input("How old are you??"))
    y =age_
    if age_ <=12 :
        print("""Registration done!!
              --> You are a student age below (12) so,
              we offer you a discount of 50%
              (Your Ticket!!) """)
        print(f"""-----------------------------------------------
                 |----------CST CINEMA HALL-------(50%) |
                 |       Name:Mr./Mrs {x}                      |
                 |       Age:{y}                               |
                 |       Special offer: STUDENT DISCOUNT!!              |
                 -----------------------------------------------""")
    elif age_>13<18:
      print("""Registration done!!
              --> You are a student age below (18) so,
              we offer you a discount of 30%
              (Your Ticket!!) """)
      print(f"""-----------------------------------------------
                 |----------CST CINEMA HALL-------(30%)   |
                 |       Name:Mr./Mrs {x}                    |
                 |       Age: {y}                               |
                 |  Special offer: STUDENT DISCOUNT!!                   |
                 -----------------------------------------------""")
    else:
        print("""Registration succesfull!!
              --> You are a student age above (19) so,
              we offer you a discount of 10%
              (Your Ticket!!) """)
        print(f"""-----------------------------------------------
                 |----------CSTerian CINEMA HALL-------(10%)   |
                 |       Name:Mr./Mrs  {x}                     |
                 |       Age: {y}                              |
                 |  Special offer: STUDENT DISCOUNT!!                   |
                 -----------------------------------------------""")
else:
    print(f"""|-----------------------------------|
              |    Mr./Mrs:-   {x}                |
              |         ACCESS DENIED!!           |      |
              |THIS IS ESPECIALLY FOR STUDENTS!!! |
              -------------------------------------""")