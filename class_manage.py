def admin():
    print('''-----admin panel----------
            a.add class
               1. add total info 
               2.add students to class
               3.remove students from class
                
            b.manage class    
               4.delete class
               5.show all classes
               6.show student classes(by class ID)
               7.back to login menu\n\n''')
    
    op = (input(">>>> "))
    if op == '1':
        add_class()
    elif op == '2':
        add_class_students()
    elif op == '3':
        remove_students_class()
    elif op == '4':
        delete_class()
    elif op == '5':
        showAll_class()
    elif op == '6':
        class_students()
    elif op == '7':
        login()
    else:
        print('please enter a valid number!')
        admin()





def add_class():
    class_name = input('please enter class name: ')
    class_teacher = input('enter class teacher name: ')
    
    class_id = input('enter class id: ')
    while len(class_id) != 3:
        print('class ID must be 3 digits!')
        class_id = input('enter class id: ')
    while True:
        with open('class.txt' , 'r') as info:
            count = 0
            for line in info:
                if line == '\n':
                    continue
                else:
                  cs = []
                  cs = line.rstrip().split('|')
                  if cs[2] == class_id:
                    count += 1
        if count > 0:
            print('class_id already exist!')
            class_id = input('enter class id: ')
        elif count == 0:
            flag = 0
            with open('class.txt' , 'a') as c:
                c.write(f'{class_name}|{class_teacher}|{class_id}\n')
                print('add class was successful!')
                flag +=1
                break
    if flag == 1:
        admin()



def delete_class():
    class_id = input('delete class by class id: ')
    info = open('class.txt' , 'r')
    temp = open('temp.txt' , 'w')
    flag = 0   
    for line in info:
            if line == '\n':
                continue
            else:
               
               cs = line.rstrip().split('|')
            
               if cs[2] == class_id:
                   flag +=1
                   pass
               elif cs[2] != class_id:
                   temp.write(line)
    info.close()
    temp.close()

    if flag == 1 :
      
        with open('temp.txt' , 'r') as temp:
         with open('class.txt' , 'w') as info:
            
            for item in temp:
                
                info.write(item+'\n')
            print('delete was successful!') 
            admin()
                
    elif flag == 0:
             print('class not found!')
             delete_class()
     
    

def showAll_class():
    count = 0
    with open('class.txt' , 'r') as c:
        for line in c:
            print(line)
            count+=1
    if count > 0:
        admin()


    

def add_class_students():
    class_id = input('enter class id to add students: ')
    with open('class.txt' , 'r') as c:
        for line in c:
            cs = []
            cs = line.rstrip().split('|')
            if cs[2] == class_id:
                student_id = input('enter student id to add to class: ')
            
                with open('students.txt' , 'r') as student:
                    count = 0
                    for item in student:
                        cs2 = []
                        cs2 = item.rstrip().split('|')
                        if  cs2[1] == student_id:
                            with open('class_students.txt' , 'a') as id:
                                id.write(f'{item}|{class_id}')
                                count +=1
                if count > 0:
                    print('sudent add was succesful')
                    admin()
                else:
                    print('student not found!')

def remove_students_class():
    pass

def class_students():
    class_id = input('enter class id to show all class students: ')
    with open('class_students.txt' , 'r') as c:
        flag = 0
        for line in c:
            cs = []
            cs = line.rstrip().split('|')
            if cs[2] == class_id:
                print(f'{cs[0]}|{cs[1]}')
                flag +=1
        if flag > 0: 
            admin()

        
                


                     
            


def user():
     print('''---------user panel------------
           1. show all classes
           2.show all student's class
           3.enter a class by cy class id
           4.back to login\n\n  ''')
     op = int(input('>>>> '))
     
     if op == 1:
         show_all_class()
     elif op == 2:
         show_student_class()
     elif op == 3:
         enter_class()
     elif op == 4:
         login()
     else:
         print('enter a valid option')
         

def show_all_class():
    with open('class.txt' , 'r') as c:
        count = 0
        for line in c:
            print(line)
            count +=1
    if count > 0:
        user()

def show_student_class():
    with open('temp2.txt' , 'r') as temp:
        for line in temp:
            cs = []
            cs = line.rstrip().split('|')
            
    with open('class_students.txt' , 'r') as c:
                for item in c:
                   cs2 = []
                   cs2 = item.rstrip().split('|')
    if cs[1] == cs2[1]:
      with open('class.txt' , 'r') as c2:
                       count = 0
                       for item2 in cs2:
                         cs3 = []
                         cs3 = item2.rstrip().split('|')
                         if cs3[2] == cs[2]:
                             print(item2)
                             count +=1
    if count > 0:
        user()
    elif count == 0:
        print('not founded!')

                             



def enter_class():
    class_id = input('enter class id: ')
    with open('temp2.txt' , 'r') as temp:
        flag = 0
        if flag == 0:
         for item in temp:
            tempo =[]
            tempo = item.rstrip().split('|')

         with open('class.txt', 'r') as c:
            for line in c :
              cs = []
              cs = line.rstrip().split('|')
              if cs[2] == class_id:
                  print(f'welcome to class,{cs[0]},mr/miss,{tempo[0]}')
                  flag +=1
        elif flag > 0:
            user()
                    



    



def user_signUP():
    
    username = input('enter your user name: ')
    password = input('enter your password: ')
    with open('student_login.txt' , 'a') as enter:
        enter.write(f'{username}|{password}')
    national_code = input('enter your national code: ')
    while len(national_code) != 5:
        print('national code must be 5 digits!')
        national_code = input('please enter your national code: ')
    while True:
     with open('students.txt' , 'r') as info:
        count = 0
        for line in info:
            cs = []
            cs = line.rstrip().split('|')
            if cs[1] == national_code:
                count +=1
        if count > 0:
            print('national code already exist!')
            national_code = input('please enter your national code: ')
        elif count == 0:
            break
    student_name = input('please enter your name: ')
    student_last = input('please enter your last name: ')
    flag = 0
    with open('students.txt' , 'a') as student:
            student.write(f'{student_name}-{student_last}|{national_code}')
            flag +=1
    with open('temp2.txt' , 'w') as temp:
        temp.write(f'{student_name}-{student_last}|{national_code}|{username}|{password}')
    if flag == 1:
        user()

def user_login():
    username = input('enter user name: ')
    password = input('enter password: ')
    with open('student_login.txt' , 'r') as stud:
        count = 0
        for line in stud:
            cs = []
            cs = line.rstrip().split('|')
            if cs[0] == username and cs[1] == password:
                count +=1
    if count > 0:
        user()
    elif count == 0:
        print('username or password is incorrect!')





def admin_login():
    admin_name = input('please enter admin user name: ')
    admin_password = input('enter admin password: ')

    while admin_name != 'admin' or admin_password != 'admin':
            print('user name or password was incorrect!')
            admin_name = input('please enter admin user name: ')
            admin_password = input('enter admin password: ')

        
    else:
        admin()
    
    
def login():
    print("""
            1.admin login
            2.user login
            3.user sign up
            4.exit\n\n""")
    
    op = int(input('>>>> '))

    if op == 1:
        admin_login()
    elif op == 2:
        user_login()
    elif op == 3:
        user_signUP()
    elif op == 4:
        return
    else:
        print('enter a valid number!')

login()

