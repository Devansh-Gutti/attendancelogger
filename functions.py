from tkinter import *


def gui():
    # Modules import start
    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox
    import tkinter.simpledialog as tsd
    import cv2
    import os
    import csv
    import numpy as np
    from PIL import Image
    import pandas as pd
    import datetime
    import time

    # Modules import end

    ####################################################################################################################

    # The below functions will check if the path exists or not.
    def check_location_exists(path):
        location = os.path.dirname(path)
        if not os.path.exists(location):
            os.makedirs(location)

    # Changes time every second on the GUI
    def tick():
        time_string = time.strftime('%H:%M:%S')
        clock_label.config(text=time_string)
        clock_label.after(200, tick)

    # Activated when the contact us option is clicked on the help menu
    def contact_admin():
        import webbrowser

        def click_link(event):
            webbrowser.open_new(
                "https://mail.google.com/mail/u/0/?fs=1&to=ifly.charan@gmail.com,lsaathvik24@gmail.com,devanshguttikonda@gmail.com&su=Regarding%20Attendance%20management%20system&body=Type%20your%20issue%20here:&tf=cm")
            contact_window.destroy()

        contact_window = Tk()
        contact_window.title('Contact Us!')
        link2 = Label(contact_window, text="Address:Section-B,1st year Btech CSE,PES-University,EC campus")
        link2.pack()
        link1 = Label(contact_window, text="Click here to write an email to us :)", fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", click_link)

        contact_window.mainloop()

    # Check if the haar-caascade file exists
    def cascade_file_exists():
        file_exists = os.path.isfile("haarcascade_frontalface_default.xml")
        if file_exists:
            pass
        else:
            messagebox.showerror(title='File not found error!', message='Please contact Developer for help')
            window.destroy()

    ####################################################################################################################
    # SAVING A NEW PASSWORD
    def save_password():
        global pass_from_file
        check_location_exists("TrainingImageLabel/")
        file_exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
        if file_exists1:
            pass_file = open("TrainingImageLabel\psd.txt", "r")
            pass_from_file = pass_file.read()
        else:
            password_change_window.destroy()
            new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
            if new_pas is None:
                messagebox.showinfo(title='No Password Entered', message='Password not set!! Please try again')
            else:
                pass_file = open("TrainingImageLabel\psd.txt", "w")
                pass_file.write(new_pas)
                messagebox.showinfo(title='Password Registered', message='New password was registered successfully!!')
                return
        old_pass = old_pass_entry.get()
        new_pass = new_pass_entry.get()
        new_pass_confirm = new_pass_confirm_entry.get()
        if old_pass == pass_from_file:
            if new_pass == new_pass_confirm:
                txf = open('TrainingImageLabel\psd.txt', 'w')
                txf.write(new_pass)
            else:
                messagebox.showinfo(title='Error', message='Confirm new password again!!!')
                return
        else:
            messagebox.showinfo(title='Wrong Password', message='Please enter correct old password.')
            return
        messagebox.showinfo(title='Password Changed', message='Password changed successfully!!')
        password_change_window.destroy()

    ####################################################################################################################
    # PASSWORD CHANGE FUNCTION
    def change_current_password():
        global old_pass_entry, new_pass_entry, new_pass_confirm_entry, password_change_window
        password_change_window = tk.Tk()
        pass_screen_width = password_change_window.winfo_screenwidth()
        pass_screen_height = password_change_window.winfo_screenheight()
        pass_x_cord = int((pass_screen_width / 2) - (401 / 2))
        pass_y_cord = int((pass_screen_height / 2) - (161 / 2))
        password_change_window.geometry(f"401x161+{pass_x_cord}+{pass_y_cord}")
        password_change_window.resizable(False, False)
        password_change_window.title("Password Change Window")
        password_change_window.configure(background="#c5f2ff")
        old_pass_label = tk.Label(password_change_window, text='    Enter Old Password:', bg='#c5f2ff',
                                  font=('times', 12, ' bold '))
        old_pass_label.place(x=10, y=10)
        old_pass_entry = tk.Entry(password_change_window, show='*', width=25, relief='solid',
                                  font=('times', 12, ' bold '))
        old_pass_entry.place(x=180, y=10)
        new_pass_label = tk.Label(password_change_window, text='   Enter New Password:', bg='#c5f2ff',
                                  font=('times', 12, ' bold '))
        new_pass_label.place(x=10, y=45)
        new_pass_entry = tk.Entry(password_change_window, show='*', width=25, relief='solid',
                                  font=('times', 12, ' bold '))
        new_pass_entry.place(x=180, y=45)
        confirm_pass_label = tk.Label(password_change_window, text='Confirm New Password:', bg='#c5f2ff',
                                      font=('times', 12, ' bold '))
        confirm_pass_label.place(x=10, y=80)
        new_pass_confirm_entry = tk.Entry(password_change_window, show='*', width=25, relief='solid',
                                          font=('times', 12, ' bold '))
        new_pass_confirm_entry.place(x=180, y=80)
        cancel_button = tk.Button(password_change_window, text="Cancel", command=password_change_window.destroy,
                                  fg="black",
                                  bg="red", height=1, width=25,
                                  activebackground="white", font=('times', 10, ' bold '))
        cancel_button.place(x=200, y=120)
        save_button = tk.Button(password_change_window, text="Save", command=save_password, fg="black", bg="#3ece48",
                                height=1,
                                width=25,
                                activebackground="white", font=('times', 10, ' bold '))
        save_button.place(x=10, y=120)
        password_change_window.mainloop()

    ####################################################################################################################
    # Activated when save profile button of frame2 is clicked. checks for admin password to save the profile
    def check_admin_password():
        global password_from_file
        check_location_exists("TrainingImageLabel/")
        file_exists2 = os.path.isfile("TrainingImageLabel\psd.txt")
        if file_exists2:
            pass_file = open("TrainingImageLabel\psd.txt", "r")
            password_from_file = pass_file.read()
        else:
            new_pass = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
            if new_pass is None:
                messagebox.showinfo(title='No Password Entered', message='Password not set!! Please try again')
            else:
                pass_file = open("TrainingImageLabel\psd.txt", "w")
                pass_file.write(new_pass)
                messagebox.showinfo(title='Password Registered', message='New password was registered successfully!!')
                return
        password = tsd.askstring('Password', 'Enter Password', show='*')
        if password == password_from_file:
            train_images()
        elif password is None:
            pass
        else:
            messagebox.showinfo(title='Wrong Password', message='You have entered wrong password')

    ####################################################################################################################

    def change_display1():
        id_entry.delete(0, 'end')
        to_display1 = "1)Take Images  >>>  2)Save Profile"
        message1.configure(text=to_display1)

    def change_display2():
        name_entry.delete(0, 'end')
        to_display6 = "1)Take Images  >>>  2)Save Profile"
        message1.configure(text=to_display6)

    ####################################################################################################################
    # ACTIVATED WHEN TAKE IMAGES BUTTON IS CLICKED WHILE REGISTERING A NEW USER
    def capture_images():
        cascade_file_exists()
        columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
        check_location_exists("StudentDetails/")
        check_location_exists("TrainingImage/")
        serial = 0
        file_exists8 = os.path.isfile("StudentDetails\StudentDetails.csv")
        if file_exists8:
            with open("StudentDetails\StudentDetails.csv", 'r') as csv_file1:
                reader5 = csv.reader(csv_file1)
                for _ in reader5:
                    serial = serial + 1
            serial = (serial // 2)
            csv_file1.close()
        else:
            with open("StudentDetails\StudentDetails.csv", 'a+') as csv_file1:
                csvwriter = csv.writer(csv_file1)
                csvwriter.writerow(columns)
                serial = 1
            csv_file1.close()
        fetch_id = (id_entry.get())
        name = (name_entry.get())
        if (name.isalpha()) or (' ' in name):
            webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            cascade_path = "haarcascade_frontalface_default.xml"
            face_detector = cv2.CascadeClassifier(cascade_path)
            start_num = 0
            while True:
                ret, img = webcam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # Incrementing sample number
                    start_num = start_num + 1
                    # Saving the detected face in the folder TrainingImage
                    cv2.imwrite(
                        "TrainingImage\ " + name + "." + str(serial) + "." + fetch_id + '.' + str(start_num) + ".jpg",
                        gray[y:y + h, x:x + w])
                    # Display the individual frames continuously to show the video
                    cv2.imshow('Taking Images', img)
                # Wait for 100 milliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # Break if the sample number is more than 100
                elif start_num > 100:
                    break
            webcam.release()
            cv2.destroyAllWindows()
            text_display = "Images Saved for : " + name
            row = [serial, '', fetch_id, '', name]
            with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                csvwriter = csv.writer(csvFile)
                csvwriter.writerow(row)
            csvFile.close()
            message1.configure(text=text_display)
        else:
            if not name.isalpha():
                text_display = "Enter Correct name"
                message.configure(text=text_display)
        train_img_button.configure(state='active')

    ####################################################################################################################

    # noinspection PyBroadException
    def train_images():
        cascade_file_exists()
        check_location_exists("TrainingImageLabel/")
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        faces, face_id = get_images_and_labels("TrainingImage")
        try:
            recognizer.train(faces, np.array(face_id))
        except:
            messagebox.showinfo(title='No Registrations', message='Please Register someone first!!!')
            return
        recognizer.save("TrainingImageLabel\Trainner.yml")
        to_display = "Profile Saved Successfully"
        message1.configure(text=to_display)
        message.configure(text='Total Registrations till now  : ' + str(face_id[0]))

    ####################################################################################################################

    # noinspection PyTypeChecker
    def get_images_and_labels(path):
        # Get the path of all the files in the folder
        image_locations = [os.path.join(path, f) for f in os.listdir(path)]
        # Create empty face list
        faces = []
        # Create empty ID list
        face_ids = []
        # Now looping through all the images & fetching the Ids and the images
        for image_source in image_locations:
            # Fetching the image and converting it to black & white
            gray_img = Image.open(image_source).convert('L')
            # Now we are converting the PIL image into numpy array
            img_array = np.array(gray_img, 'uint8')
            # Student id fetched from the grayscale image
            id_from_image = int(os.path.split(image_source)[-1].split(".")[1])
            # Take the face from the training image
            faces.append(img_array)
            face_ids.append(id_from_image)
        return faces, face_ids

    ###########################################################################################
    # Take_attendance function gets activated when Take Attendance button is clicked
    # Worked on by -devansh

    def take_attendance():
        cascade_file_exists()
        check_location_exists("Attendance/")
        check_location_exists("StudentDetails/")
        for sample in tree_view.get_children():
            tree_view.delete(sample)
        start_number = 0
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        yml_exists = os.path.isfile("TrainingImageLabel\Trainner.yml")
        if yml_exists:
            recognizer.read("TrainingImageLabel\Trainner.yml")
        else:
            messagebox.showinfo(title='Data Missing', message='Please click on Save Profile to reset data!!')
            return
        haarcascade_path = "haarcascade_frontalface_default.xml"
        face_cascade = cv2.CascadeClassifier(haarcascade_path)

        webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Start webcam
        font = cv2.FONT_HERSHEY_SIMPLEX
        column_titles = ['Id', 'Name', 'Date', 'Time']
        file_exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
        if file_exists1:
            student_details = pd.read_csv("StudentDetails\StudentDetails.csv")  # Read student details from csv file
        else:
            messagebox.showinfo(title='Details Empty', message='No student records found!')
            webcam.release()  # Stop webcam
            cv2.destroyAllWindows()
            window.destroy()
        while True:
            ret, image = webcam.read()  # We are reading individual frames from the webcam
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(grayscale_image, 1.2, 5)
            found = False
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (225, 0, 0), 2)
                serial, conf = recognizer.predict(grayscale_image[y:y + h, x:x + w])
                if conf < 50:
                    time_details = time.time()
                    final_date = datetime.datetime.fromtimestamp(time_details).strftime('%d-%m-%Y')
                    final_time = datetime.datetime.fromtimestamp(time_details).strftime('%H:%M:%S')
                    raw_student_name = student_details.loc[student_details['SERIAL NO.'] == serial]['NAME'].values
                    student_id = student_details.loc[student_details['SERIAL NO.'] == serial]['ID'].values
                    student_id = str(student_id)
                    student_id = student_id[1:-1]
                    student_name = str(raw_student_name)
                    student_name = student_name[2:-2]
                    attendance = [str(student_id), student_name, str(final_date), str(final_time)]
                    found = True
                else:
                    student_name = 'Unknown'
                cv2.putText(image, str(student_name), (x, y + h), font, 1, (255, 255, 255), 2)
            cv2.imshow('Taking Attendance', image)
            if cv2.waitKey(1) == ord('q'):
                break
        if found:
            raw_time = time.time()
            final_date = datetime.datetime.fromtimestamp(raw_time).strftime('%d-%m-%Y')
            file_exists = os.path.isfile("Attendance\Attendance_" + final_date + ".csv")
            if file_exists:
                with open("Attendance\Attendance_" + final_date + ".csv", 'a+') as attendance_file:
                    csvwriter = csv.writer(attendance_file)
                    csvwriter.writerow(attendance)
                attendance_file.close()
            else:
                with open("Attendance\Attendance_" + final_date + ".csv", 'a+') as attendance_file:
                    csvwriter = csv.writer(attendance_file)
                    csvwriter.writerow(column_titles)
                    csvwriter.writerow(attendance)
                attendance_file.close()
            with open("Attendance\Attendance_" + final_date + ".csv", 'r') as attendance_file:
                reader1 = csv.reader(attendance_file)
                for lines in reader1:
                    start_number = start_number + 1
                    if start_number > 1:
                        if start_number % 2 != 0:
                            student_id_in_tree = str(lines[0]) + '   '
                            tree_view.insert('', 0, text=student_id_in_tree,
                                             values=(str(lines[1]), str(lines[2]), str(lines[3])))
            attendance_file.close()
        webcam.release()
        cv2.destroyAllWindows()

    ####################################################################################################################

    # Selecting a row of attendance tree view
    def select_attendance(event):
        global tree_view, row_name, row_date, row_time
        try:
            cursor_row = tree_view.focus()
            contents = tree_view.item(cursor_row)
            row = contents["values"]
            row_name = row[0]
            row_date = row[1]
            row_time = row[2]
        except IndexError:
            messagebox.showerror(title='Empty row!', message='No data selected!')

    ####################################################################################################################

    # Deleting the selected row from attendance
    def delete_attendance():
        if row_name == '' or row_date == '' or row_time == '':
            messagebox.showerror(title='Empty row!', message='No data selected!')
        else:
            csv_list = []
            with open("Attendance\Attendance_" + row_date + ".csv", 'r+') as f:
                reader = csv.reader(f)
                for line in reader:
                    csv_list.append(line)
            with open("Attendance\Attendance_" + row_date + ".csv", 'w') as f_w:
                csvwriter = csv.writer(f_w)
                for line in csv_list:
                    if line == []:
                        pass
                    elif line[1] == row_name and line[2] == row_date and line[3] == row_time:
                        pass
                    else:
                        csvwriter.writerow(line)
            f_w.close()
            frame1.destroy()
            frame1_build()
            with open("Attendance\Attendance_" + row_date + ".csv", 'r') as attendance_file:
                reader1 = csv.reader(attendance_file)
                start_number = 0
                for lines in reader1:
                    start_number = start_number + 1
                    if start_number > 1:
                        if start_number % 2 != 0:
                            student_id_in_tree = str(lines[0]) + '   '
                            tree_view.insert('', 0, text=student_id_in_tree,
                                             values=(str(lines[1]), str(lines[2]), str(lines[3])))

    ####################################################################################################################
    # Worked on by -devansh

    # frame1 assemble function
    def frame1_build():
        global tree_view, frame1
        frame1 = tk.Frame(window, bg="#00aeff")
        frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)
        head1 = tk.Label(frame1, text="                       For Existing Users                       ",
                         fg="#c5f2ff",
                         bg="#010141", font=('times', 17, ' bold '))
        head1.place(x=0, y=0, relwidth=1)
        lbl3 = tk.Label(frame1, text="Attendance", width=20, fg="#c5f2ff", bg="#00aeff", height=1,
                        font=('times', 17, ' bold '))
        lbl3.place(x=0, y=165, relwidth=1)

        # Display of Attendance table in frame1 start:

        tree_view = ttk.Treeview(frame1, height=13, columns=('name', 'date', 'time'))
        tree_view.column('#0', width=100)
        tree_view.column('name', width=160)
        tree_view.column('date', width=100)
        tree_view.column('time', width=80)
        tree_view.grid(row=4, column=0, padx=(70, 0), pady=(220, 0), columnspan=4)
        tree_view.heading('#0', text='ID')
        tree_view.heading('name', text='NAME')
        tree_view.heading('date', text='DATE')
        tree_view.heading('time', text='TIME')
        tree_view.bind("<ButtonRelease-1>", select_attendance)
        # Scrollbar code start :

        scroll_bar = ttk.Scrollbar(frame1, orient='vertical', command=tree_view.yview)
        scroll_bar.grid(row=4, column=4, padx=(0, 100), pady=(220, 0), sticky='ns')
        tree_view.configure(yscrollcommand=scroll_bar.set)
        attendance_button = tk.Button(frame1, text="Take Attendance", command=take_attendance, fg="#c5f2ff",
                                      bg="#010141",
                                      width=35,
                                      height=1,
                                      activebackground="white", font=('times', 15, ' bold '), cursor='hand2')
        attendance_button.place(x=80, y=50)

        sample_button = tk.Button(frame1, text="Register New User",
                                  command=frame1_to_frame2, fg="#c5f2ff", bg="#010141", width=35, height=1,
                                  activebackground="white", font=('times', 15, ' bold '), cursor='hand2')
        sample_button.place(x=80, y=115)

        delete_button = tk.Button(frame1, text='Delete selected attendance', command=delete_attendance, fg="#c5f2ff",
                                  bg="#010141", width=35, height=1,
                                  activebackground="white", font=('times', 15, ' bold '), cursor='hand2')
        delete_button.place(x=80, y=520)
        exit_window = tk.Button(frame1, text="Quit", command=window.destroy, fg="#c5f2ff", bg="red", width=35, height=1,
                                activebackground="white", font=('times', 15, ' bold '), cursor='hand2')
        exit_window.place(x=80, y=580)

        frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

    ####################################################################################################################
    # Worked on by -saatvik
    # ASSEMBLE FRAME 2 IN THE REQUIRED POSITION
    def frame2_build():
        global frame2, message, message1, id_entry, name_entry, train_img_button
        frame2 = tk.Frame(window, bg="#00aeff")
        title = tk.Label(frame2, text="                       For New Registrations                       ",
                         fg="#c5f2ff",
                         bg="#010141", font=('times', 17, ' bold '), width=45)
        title.grid(row=0, column=0)

        enter_id_label = tk.Label(frame2, text="Enter ID", height=1, fg="#c5f2ff", bg="#00aeff",
                                  font=('times', 17, ' bold '))
        enter_id_label.place(x=0, y=55, relwidth=1)

        id_entry = tk.Entry(frame2, width=32, font=('times', 15, ' bold '))
        id_entry.place(x=80, y=88)

        lbl2 = tk.Label(frame2, text="Enter Name", fg="#c5f2ff", bg="#00aeff", font=('times', 17, ' bold '))
        lbl2.place(x=0, y=140, relwidth=1)

        name_entry = tk.Entry(frame2, width=32, font=('times', 15, ' bold '))
        name_entry.place(x=80, y=173)

        message1 = tk.Label(frame2, text="1)Take Images  >>>  2)Save Profile", bg="#00aeff", fg="#c5f2ff", width=35,
                            height=1,
                            font=('times', 15, ' bold '))
        message1.place(x=80, y=230)

        message = tk.Label(frame2, text="", bg="#00aeff", fg="#c5f2ff", width=39, height=1, activebackground="yellow",
                           font=('times', 16, ' bold '))
        message.place(x=7, y=450)

        # Declaration of buttons of frame2 start

        clear_button = tk.Button(frame2, text="Clear", command=change_display1, fg="#c5f2ff", bg="#ea2a2a", width=11,
                                 activebackground="white", font=('times', 11, ' bold '), cursor='hand2')
        clear_button.place(x=390, y=86)
        clear_button2 = tk.Button(frame2, text="Clear", command=change_display2, fg="#c5f2ff", bg="#ea2a2a", width=11,
                                  activebackground="white", font=('times', 11, ' bold '), cursor='hand2')
        clear_button2.place(x=390, y=172)
        take_img_button = tk.Button(frame2, text="Take Images", command=capture_images, fg="white", bg="#010141",
                                    width=35,
                                    height=1,
                                    activebackground="white", font=('times', 15, ' bold '), cursor='hand2')
        take_img_button.place(x=80, y=300)
        train_img_button = tk.Button(frame2, text="Save Profile", command=check_admin_password, fg="white",
                                     bg="#010141", width=35,
                                     height=1, state='disabled', cursor='hand2',
                                     activebackground="white", font=('times', 15, ' bold '))
        train_img_button.place(x=80, y=380)

        back_button = tk.Button(frame2, text="Back", command=back_from_frame2, fg="white", bg="#010141", width=35,
                                height=1,
                                activebackground="white", font=('times', 15, ' bold '), cursor='hand2')
        back_button.place(x=80, y=450)

        exit_window = tk.Button(frame2, text="Quit", command=window.destroy, fg="#c5f2ff", bg="red", width=35, height=1,
                                activebackground="white", font=('times', 15, ' bold '), cursor='hand2')
        exit_window.place(x=80, y=520)

        frame2.place(relx=0.51, rely=0.17, relwidth=0.39, relheight=0.80)

        # Declaration of buttons of frame2 end

    ####################################################################################################################
    # TRANSITION FROM FRAME1 TO FRAME2
    def frame1_to_frame2():
        frame1.destroy()
        frame2_build()

    ####################################################################################################################
    # TRANSITION FROM FRAME2 TO FRAME1

    def back_from_frame2():
        # Activated when back button of FRAME2 is clicked . Moves from FRAME2 to FRAME1.

        frame2.destroy()
        frame1_build()

    ####################################################################################################################

    # Main code(initialisation):

    global pass_from_file, row_name, row_date, row_time
    pass_from_file = ''
    row_name = ''
    row_date = ''
    row_time = ''
    time_stamp = time.time()
    date = datetime.datetime.fromtimestamp(time_stamp).strftime('%d-%m-%Y')
    day, month, year = date.split("-")

    month_dictionary = {'01': 'January',
                        '02': 'February',
                        '03': 'March',
                        '04': 'April',
                        '05': 'May',
                        '06': 'June',
                        '07': 'July',
                        '08': 'August',
                        '09': 'September',
                        '10': 'October',
                        '11': 'November',
                        '12': 'December'
                        }

    # GUI FRONT-END START:

    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.resizable(False, False)
    window.title("Attendance Logger using Facial Recognition")
    window.configure(bg='#01004e')
    frame1_build()

    main_display = tk.Label(window, text="Face Recognition Based Attendance System", fg="#fd0e5c", bg="#01004e",
                            width=65, font=('times', 29, ' bold '))
    main_display.place(x=10, y=10)

    frame3 = tk.Frame(window, bg="#c4c6ce")
    frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

    frame4 = tk.Frame(window, bg="#c4c6ce")
    frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

    date_label = tk.Label(frame4, text=day + "-" + month_dictionary[month] + "-" + year + "  |  ", fg="#7591f6",
                          bg="#01004e",
                          width=55,
                          height=1, font=('times', 21, ' bold '))
    date_label.pack(fill='both', expand=1)

    clock_label = tk.Label(frame3, fg="#c5f2ff", bg="#01004e", width=55, height=1, font=('times', 22, ' bold '))
    clock_label.pack(fill='both', expand=1)
    tick()

    # MENU BAR CODE START

    menu_bar = tk.Menu(window, relief='ridge')
    ribbon_display = tk.Menu(menu_bar, tearoff=0)
    ribbon_display.add_command(label='Change Password', command=change_current_password)
    ribbon_display.add_command(label='Contact Us', command=contact_admin)
    ribbon_display.add_command(label='Exit', command=window.destroy)
    menu_bar.add_cascade(label='Help', font=('times', 29, ' bold '), menu=ribbon_display)

    window.configure(menu=menu_bar)
    window.mainloop()

# End of code
########################################################################################################################
########################################################################################################################
########################################################################################################################
