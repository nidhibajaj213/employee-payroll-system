from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import *
from tkcalendar import *
from tkinter import filedialog
from fpdf import FPDF  
import os
import matplotlib.pyplot as plt

# Global Variable
tempVal="Department"

"""def store_temp(value):
    print(f"Selected option: {value}")
    #global tempVal
    #tempVal=set_temp"""

def report_open():
    er.deiconify()
    ew.withdraw()
    ap.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    aw.withdraw()
    em.withdraw()
    sw.withdraw()
    ep.withdraw()
    sc.withdraw()
    ps.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

    # Retrieve data from the Employee Details window
    employee_name = entr2.get()
    gender = gender1.get()
    dob = entr5.get()
    employee_id = entr6.get()
    position = entr7.get()
    department = entr8.get()
    basic_salary = float(entr10.get())
    allowances_option= yes1.get()
    allowance_split = float(allowances_option.split("-->Rs:")[1])
    try:
        allowances = float(allowance_split)
    except (ValueError, IndexError) as e:
        print("Error:", e)
        allowances = 0.0
    
    deductions = float(entr14.get())

    gross_salary = basic_salary + allowances - deductions
    net_salary = gross_salary - deductions
    
    data = {
        'Basic Salary': basic_salary,
        'Allowances': allowances,
        'Deductions': deductions,
        'Gross Salary': gross_salary,
        'Net Salary': net_salary
    }

    #Create bar graph
    plt.figure(figsize=(8,4))
    plt.bar(data.keys(),data.values(), color='skyblue')
    plt.title('Employee Salary Distribution')
    plt.xlabel('Employee Names')
    plt.ylabel('Salary')
    plt.savefig('bar_chart.png')

    #create pie chart
    plt.figure(figsize=(4,4))
    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
    plt.title('Employee salary Distribution')
    plt.savefig('pie_chart.png')

    

    performance_description =  f"""
    The employee report provides a comprehensive overview of the individual's financial particulars and personal details. 
    It starts by identifying the employee, {employee_name} (Employee ID: {employee_id}), through their name and unique ID, offering an immediate association with the provided information. 
    Next, the report outlines the critical components of the employee's salary, including the basic salary of Rs. {basic_salary:.2f}, various allowances totaling Rs. {allowances:.2f}, and deductions amounting to Rs. {deductions:.2f}. 
    By combining these elements, the report calculates the gross salary of Rs. {gross_salary:.2f} and the net salary of Rs. {net_salary:.2f}, providing a clear picture of the employee's overall earnings and the impact of deductions. 
    Additionally, the report includes visual representations in the form of a pie chart and a bar graph to visually communicate the distribution of the employee's salary components, promoting a deeper understanding of the financial breakdown. 
    These graphical elements complement the descriptive text, offering an engaging and informative presentation of the employee's financial profile. 
    Finally, the report is compiled into a PDF document, providing a tangible and easily shareable format for the gathered information.

    The Graphs are as follows:
    """
    er_st_data.tag_configure("description", font=("Arial", 12,"bold"))  # Set the font to Arial with size 12
    er_st_data.tag_add("description", "1.0", "end")
    er_st_data.delete('1.0', tk.END)
    er_st_data.insert(tk.INSERT, performance_description,"description")

def save_pdf():
    employee_name = entr2.get()
    gender = gender1.get()
    dob = entr5.get()
    employee_id = entr6.get()
    position = entr7.get()
    department = entr8.get()
    basic_salary = float(entr10.get())
    allowances_option= yes1.get()
    allowance_split = float(allowances_option.split("-->Rs:")[1])
    try:
        allowances = float(allowance_split)
    except (ValueError, IndexError) as e:
        print("Error:", e)
        allowances = 0.0
    
    deductions = float(entr14.get())

    gross_salary = basic_salary + allowances - deductions
    net_salary = gross_salary - deductions
    
    data = {
        'Basic Salary': basic_salary,
        'Allowances': allowances,
        'Deductions': deductions,
        'Gross Salary': gross_salary,
        'Net Salary': net_salary
    }
    performance_description =  f"""
    The employee report provides a comprehensive overview of the individual's financial particulars and personal details. 
    It starts by identifying the employee, {employee_name} (Employee ID: {employee_id}), through their name and unique ID, offering an immediate association with the provided information. 
    Next, the report outlines the critical components of the employee's salary, including the basic salary of Rs. {basic_salary:.2f}, various allowances totaling Rs. {allowances:.2f}, and deductions amounting to Rs. {deductions:.2f}. 
    By combining these elements, the report calculates the gross salary of Rs. {gross_salary:.2f} and the net salary of Rs. {net_salary:.2f}, providing a clear picture of the employee's overall earnings and the impact of deductions. 
    Additionally, the report includes visual representations in the form of a pie chart and a bar graph to visually communicate the distribution of the employee's salary components, promoting a deeper understanding of the financial breakdown. 
    These graphical elements complement the descriptive text, offering an engaging and informative presentation of the employee's financial profile. 
    Finally, the report is compiled into a PDF document, providing a tangible and easily shareable format for the gathered information.

    The Graphs are as follows:
    """

    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=13,style='B')
    pdf.cell(200,10,txt="Employee Salary Report",ln=True)
    pdf.multi_cell(0,10,performance_description)
    pdf.image('bar_chart.png',x=10,y=pdf.y,w=120)
    first_chart_height=100
    pdf.ln(first_chart_height + 20)
    pdf.cell(200,10)
    pdf.image('pie_chart.png',x=10,y=pdf.y,w=120)

    file_path=filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=[("PDF files","*.pdf")])
    if file_path:
        pdf.output(file_path)

    os.remove('bar_chart.png')
    os.remove('pie_chart.png')

def asave_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Hello, this is a sample PDF file.", ln=True)
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf.output(file_path)

def handle_selection(selected_item):
    #selected_item = dropdown.get()
    print(f"Selected option: {selected_item}")

def elogin():
    eusername="Employee"
    epassword="1234"
    un=entm1.get()
     # Data Validation
    if len(un)==0:
        showerror("Invalid Entry","Username Cannot be Empty")
    
    if un.isspace():
        showerror("Invalid Entry","Username cannot be only spaces")
    
    if un.isdigit():
        showerror("Invalid Entry","Username cannot contain Digits")
    
    pw=entm2.get()
    # Data Validation
    if len(pw)==0:
        showerror("Invalid Entry","Password cannot be Empty")
    
    if pw.isspace():
        showerror("Invalid Entry","Password cannot be only spaces")
    
    if un==eusername and pw==epassword:
        showinfo("Login Successful","You have Successfully logged-in !!")
        ep.deiconify()
        er.withdraw()
        ew.withdraw()
        ap.withdraw()
        gw.withdraw()
        gr.withdraw()
        sw.withdraw()
        mw.withdraw()
        aw.withdraw()
        em.withdraw()
        sc.withdraw()
        ps.withdraw()
        ae.withdraw()
        me.withdraw()
        dr.withdraw()
        sr.withdraw()
        ve.withdraw()
        entm1.delete(0,END)
        entm2.delete(0,END)
    else:
        showerror("Invalid Credentials","Please Enter Valid Username and Password")
        entm1.delete(0,END)
        entm2.delete(0,END)

def del_record():
    if askyesno("WARNING","DATA WILL NOT RECOVER AGAIN, STILL DELETE ?"):
        pass
    
def esave_profile(): 
    # Store profile information
    employee_profile = {
            "Name": entae2.get(),
            "Age": entae3.get(),
            "Gender": gender4.get(),
            "DOB": entae5.get(),
            "EID": entae6.get(),
            "Position": entae7.get(),
            "Department": entae8.get(),
            "DOJ": entae9.get(),
            "BS": entae10.get(),
            "Overtime": work4.get(),
            "Allow": allow4.get(),
            "Yes":yes4.get(),
            "Deductions": entae14.get()
        }
    if all(employee_profile.values()):
        showinfo("Success", "Employee-Profile Successfully Created !!")
    else:
        showerror("Error", "Please fill all the fields !!")
        entae2.delete(0,END)
        entae3.delete(0,END)
        gender4.set('')
        entae5.delete(0,END)
        entae6.delete(0,END)
        entae7.delete(0,END)
        entae8.delete(0,END)
        entae9.delete(0,END)
        entae10.delete(0,END)
        work4.set('')
        allow4.set('')
        yes4.set('')
        entae14.delete(0,END)

    
def save_profile(): 
    # Store profile information
    employee_profile = {
            "Name": ente2.get(),
            "Age": ente3.get(),
            "Gender": gender.get(),
            "DOB": ente5.get(),
            "EID": ente6.get(),
            "Position": ente7.get(),
            "Department": ente8.get(),
            "DOJ": ente9.get(),
            "BS": ente10.get(),
            "Overtime": work.get(),
            "Allow": allow.get(),
            "Yes":yes.get(),
            "Deductions": ente14.get()
        }
    if all(employee_profile.values()):
        showinfo("Success", "Employee-Profile Successfully Created !!")
        ep.deiconify()
        er.withdraw()
        ew.withdraw()
        ap.withdraw()
        gw.withdraw()
        gr.withdraw()
        mw.withdraw()
        aw.withdraw()
        sw.withdraw()
        em.withdraw()
        sc.withdraw()
        ae.withdraw()
        me.withdraw()
        dr.withdraw()
        sr.withdraw()
        ve.withdraw()
    else:
        showerror("Error", "Please fill all the fields !!")
        ente2.delete(0,END)
        ente3.delete(0,END)
        gender.set('')
        ente5.delete(0,END)
        ente6.delete(0,END)
        ente7.delete(0,END)
        ente8.delete(0,END)
        ente9.delete(0,END)
        ente10.delete(0,END)
        work.set('')
        allow.set('')
        yes.set('')
        ente14.delete(0,END)

def alogin():
    ausername="Admin"
    apassword="1234"
    un=ent1.get()
     # Data Validation
    if len(un)==0:
        showerror("Invalid Entry","Username Cannot be Empty")
    
    if un.isspace():
        showerror("Invalid Entry","Username cannot be only spaces")
    
    if un.isdigit():
        showerror("Invalid Entry","Username cannot contain Digits")
    
    pw=ent2.get()
    # Data Validation
    if len(pw)==0:
        showerror("Invalid Entry","Password cannot be Empty")
        
    if pw.isspace():
        showerror("Invalid Entry","Password cannot be only spaces")
    
    if un==ausername and pw==apassword:
        showinfo("Login Successful","You have Successfully logged into the Admin-Pannel")
        ap.deiconify()
        aw.withdraw()
        gw.withdraw()
        gr.withdraw()
        sw.withdraw()
        mw.withdraw()
        em.withdraw()
        ew.withdraw()
        ep.withdraw()
        er.withdraw()
        sc.withdraw()
        ps.withdraw()
        ae.withdraw()
        me.withdraw()
        dr.withdraw()
        sr.withdraw()
        ve.withdraw()
        ent1.delete(0,END)
        ent2.delete(0,END)
    else:
        showerror("Invalid Credentials","Please Enter Valid Username and Password")
        ent1.delete(0,END)
        ent2.delete(0,END)

def alogout():
    if askyesno("Logout","Are you sure, you want to logout?"):
        aw.deiconify()
        ap.withdraw()
        gw.withdraw()
        gr.withdraw()
        mw.withdraw()
        em.withdraw()
        sw.withdraw()
        ew.withdraw()
        ep.withdraw()
        er.withdraw()
        sc.withdraw()
        ps.withdraw()
        ae.withdraw()
        me.withdraw()
        dr.withdraw()
        sr.withdraw()
        ve.withdraw()
    else:
        ap.deiconify()
        aw.withdraw()
        gw.withdraw()
        gr.withdraw()
        mw.withdraw()
        sw.withdraw()
        em.withdraw()
        ew.withdraw()
        ep.withdraw()
        er.withdraw()
        sc.withdraw()
        ps.withdraw()
        ae.withdraw()
        me.withdraw()
        dr.withdraw()
        sr.withdraw()
        ve.withdraw()

def elogout():
    if askyesno("Logout","Are you sure, you want to logout?"):
        em.deiconify()
        ap.withdraw()
        gw.withdraw()
        gr.withdraw()
        mw.withdraw()
        aw.withdraw()
        ew.withdraw()
        sw.withdraw()
        ep.withdraw()
        er.withdraw()
        sc.withdraw()
        ps.withdraw()
        ae.withdraw()
        me.withdraw()
        dr.withdraw()
        sr.withdraw()
        ve.withdraw()
    else:
        ep.deiconify()
        aw.withdraw()
        gw.withdraw()
        gr.withdraw()
        mw.withdraw()
        em.withdraw()
        ew.withdraw()
        sw.withdraw()
        ap.withdraw()
        er.withdraw()
        sc.withdraw()
        ps.withdraw()
        ae.withdraw()
        me.withdraw()
        dr.withdraw()
        sr.withdraw()
        ve.withdraw()

def aopen(): 
    aw.deiconify()
    ap.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    em.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    sc.withdraw()
    ps.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

def eopen(): 
    em.deiconify()
    ap.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    aw.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    sc.withdraw()
    ps.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

def esopen():
    ew.deiconify()
    ap.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    sw.withdraw()
    aw.withdraw()
    em.withdraw()
    er.withdraw()
    ep.withdraw()
    sc.withdraw()
    ps.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

def eropen():
    er.deiconify()
    ew.withdraw()
    ap.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    aw.withdraw()
    em.withdraw()
    sw.withdraw()
    ep.withdraw()
    sc.withdraw()
    ps.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

def swopen():
    sw.deiconify()
    ep.withdraw()
    er.withdraw()
    ew.withdraw()
    ap.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    aw.withdraw()
    em.withdraw()
    sc.withdraw()
    ps.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

def psopen():
    ps.deiconify()
    ep.withdraw()
    er.withdraw()
    ew.withdraw()
    ap.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    aw.withdraw()
    em.withdraw()
    sc.withdraw()
    sw.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

def epopen():
    ep.deiconify()
    er.withdraw()
    ew.withdraw()
    ap.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    aw.withdraw()
    sw.withdraw()
    em.withdraw()
    sc.withdraw()
    ps.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

def gwopen():
    gw.deiconify()
    aw.withdraw()
    ap.withdraw()
    gr.withdraw()
    mw.withdraw()
    em.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    sc.withdraw()
    ps.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

def scopen():
    sc.deiconify()
    aw.withdraw()
    ap.withdraw()
    gw.withdraw()
    mw.withdraw()
    em.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    gr.withdraw()
    ps.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

def gropen():
    gr.deiconify()
    aw.withdraw()
    ap.withdraw()
    gw.withdraw()
    mw.withdraw()
    em.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    sc.withdraw()
    ps.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

def aeopen():
    ae.deiconify()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()
    gr.withdraw()
    aw.withdraw()
    ap.withdraw()
    gw.withdraw()
    mw.withdraw()
    em.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    sc.withdraw()
    ps.withdraw()

def meropen():
    me.deiconify()
    ve.withdraw()
    dr.withdraw()
    sr.withdraw()
    ae.withdraw()
    ap.withdraw()
    aw.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    em.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    sc.withdraw()
    ps.withdraw()

def sropen():
    sr.deiconify()
    dr.withdraw()
    me.withdraw()
    ae.withdraw()
    ve.withdraw()
    ap.withdraw()
    aw.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    em.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    sc.withdraw()
    ps.withdraw()

def dropen():
    dr.deiconify()
    me.withdraw()
    ae.withdraw()
    sr.withdraw()
    ve.withdraw()
    ap.withdraw()
    aw.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    em.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    sc.withdraw()
    ps.withdraw()

def meopen():
    me.deiconify()
    ae.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()
    ap.withdraw()
    aw.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    em.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    sc.withdraw()
    ps.withdraw()

def veopen():
    ve.deiconify()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ae.withdraw()
    ap.withdraw()
    aw.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    em.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    sc.withdraw()
    ps.withdraw()

def gwclose():
    ap.deiconify()
    aw.withdraw()
    gw.withdraw()
    gr.withdraw()
    mw.withdraw()
    em.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    sc.withdraw()
    ps.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

def mwopen():
    mw.deiconify()
    aw.withdraw()
    gw.withdraw()
    gr.withdraw()
    ap.withdraw()
    em.withdraw()
    ew.withdraw()
    ep.withdraw()
    er.withdraw()
    sw.withdraw()
    sc.withdraw()
    ps.withdraw()
    ae.withdraw()
    me.withdraw()
    dr.withdraw()
    sr.withdraw()
    ve.withdraw()

#Salary Calculations:
def c_salary():

    e_id = int(entsc2.get())
    e_name = str(entsc3.get())
    basic_salary = float(entsc4.get())
    overtime = float(entsc6.get())
    allowances = float(yes2.get().split("-->Rs:")[1])  # Extract value
    deductions = float(entsc5.get())

    if not e_id or not basic_salary or not overtime or not deductions or yes2.get() == "select allowances":
      showerror("Error", "Please Enter all fields correctly !!")
    

    gross_salary = basic_salary + overtime + allowances
    net_salary = gross_salary - deductions

    # Update the labels
    labsc9.config(text=f"Gross-Salary: Rs {gross_salary:.2f}")
    labsc10.config(text=f"Net-Salary: Rs {net_salary:.2f}")


#Payroll Calculations:
def c_payroll():

    payroll_type = week1.get()
    e_id = int(entps2.get())
    e_name = str(entps3.get())
    basic_salary = float(entps4.get())
    overtime = float(entps6.get())
    allowances = float(yes3.get().split("-->Rs:")[1])  # Extract allowance value
    deductions = float(entps5.get()) 

    Monthly_payroll = basic_salary + overtime + allowances - deductions
    #print(Monthly_payroll)
    Weekly_payroll = (basic_salary + overtime + allowances - deductions) / 2
    #print(Weekly_payroll)

    if payroll_type == "Monthly":
            labps10.config(text=f"Monthly Payroll: Rs {Monthly_payroll:.2f} ")
            labps11.config(text="") 
    elif payroll_type == "Bi-Weekly":
            labps11.config(text=f"Bi-Weekly Payroll: Rs {Weekly_payroll:.2f}")
    

    if not e_id or not basic_salary or not overtime or not deductions:
      showwarning("Error", "Please Enter all fields correctly !!")
    

# Function to clear all data fields-->Salary
def clear_data():
    entsc2.delete(0,END)
    entsc3.delete(0,END)
    entsc4.delete(0,END)
    entsc6.delete(0,END)
    yes2.set('')
    entsc5.delete(0,END)
    labsc9.config(text="Gross-Salary:")
    labsc10.config(text="Net-Salary:")

# Function to clear all data fields-->Payroll
def clear_paydata():
    entps2.delete(0,END)
    entps3.delete(0,END)
    entps4.delete(0,END)
    entps6.delete(0,END)
    yes3.set('')
    var.set("Monthly")
    entps5.delete(0,END)
    labps10.config(text=" ")
    labps11.config(text=" ")

def on_exit():
    if askokcancel("Quit","Do you want to Exit?"):
        aw.destroy()
        ap.destroy()
        gw.destroy()
        gr.destroy()
        mw.destroy()
        em.destroy()
        ew.destroy()
        ep.destroy()
        er.destroy()
        sw.destroy()
        sc.destroy()
        ps.destroy()
        ae.destroy()
        me.destroy()
        dr.destroy()
        sr.destroy()
        ve.destroy()


# Main Window
mw=tk.Tk()
mw.title("EPS-System")
mw.geometry("400x370+100+100")
mw.configure(bg="light grey")
f=("Comic Sans-Serif",17,"bold")

labm1=Label(mw,text="Employee Payroll System",font=("Comic Sans-Serif",17,"bold","underline"),background="light grey")
labm1.pack(pady=15)

seperator=ttk.Separator(mw,orient="horizontal")
seperator.pack(fill='x',padx=4, pady=15)

btnm1=Button(mw,text="Employee",font=f,width=20,command=eopen)
btnm1.pack(pady=15)

btnm2=Button(mw,text="Admin",font=f,width=20,command=aopen)
btnm2.pack(pady=15)

seperator=ttk.Separator(mw,orient="horizontal")
seperator.pack(fill='x',padx=4, pady=10)

btnm3=Button(mw,text="EXIT",font=f,command=on_exit,background="navy blue",foreground="white")
btnm3.pack(pady=10)


# Employee- Main Window
em= Tk()
em.title("Employee-Pannel")
em.geometry("400x460+100+100")
em.configure(bg="light grey")
f=("Comic Sans-Serif",17,"bold")
em.withdraw()

labm2=Label(em,text="EPS-Employee",font=("Comic Sans-Serif",17,"bold","underline"),bg="light grey")
labm2.pack(pady=10)

separator = ttk.Separator(em, orient='horizontal')
separator.pack(fill='x', padx=5, pady=10)

labm3=Label(em,text="Enter the Username: ",font=f,bg="light grey")
labm3.pack(pady=10)
entm1=Entry(em,font=f)
entm1.pack(pady=11)

labm4=Label(em,text="Enter the Password: ",font=f,bg="light grey")
labm4.pack(pady=10)
entm2=Entry(em,font=f,show="*")
entm2.pack(pady=11)

btnm4=Button(em,text="LOGIN",font=f,bg="navy blue",foreground="white",command=elogin)
btnm4.pack(pady=15)

separator = ttk.Separator(em, orient='horizontal')
separator.pack(fill='x', padx=20, pady=10)

btnm5=Button(em,text="SIGN-UP",font=f,bg="navy blue",foreground="white",command=swopen)
btnm5.place(x=60,y=390)

btnm5=Button(em,text="BACK",font=f,bg="navy blue",foreground="white",command=mwopen)
btnm5.place(x=260,y=390)


# Employee Sign-up Window
sw= Tk()
sw.title("Employee-Pannel")
sw.geometry("400x480+100+100")
sw.configure(bg="light grey")
f=("Comic Sans-Serif",17,"bold")
sw.withdraw()

labs2=Label(sw,text="EPS-Employee",font=("Comic Sans-Serif",17,"bold","underline"),bg="light grey")
labs2.pack(pady=10)

separator = ttk.Separator(sw, orient='horizontal')
separator.pack(fill='x', padx=5, pady=10)

labs3=Label(sw,text="Enter the Username: ",font=f,bg="light grey")
labs3.pack(pady=10)
ents1=Entry(sw,font=f)
ents1.pack(pady=11)

labs4=Label(sw,text="Enter the Password: ",font=f,bg="light grey")
labs4.pack(pady=10)
ents2=Entry(sw,font=f,show="*")
ents2.pack(pady=11)

labs4=Label(sw,text="Re-enter the Password: ",font=f,bg="light grey")
labs4.pack(pady=10)
ents3=Entry(sw,font=f,show="*")
ents3.pack(pady=11)

btns4=Button(sw,text="SIGN-UP",font=f,bg="navy blue",foreground="white",command=esopen)
btns4.pack(pady=15)


#Employee after signup window
ew=tk.Tk()
ew.title("Employee-Pannel")
ew.geometry("500x700+100+100")
ew.configure(bg="light grey")
f=("Comic Sans-Serif",15,"bold")
ew.withdraw()

labe1=Label(ew,text="EPS-Employee",font=("Comic Sans-Serif",16,"bold","underline"),bg="light grey")
labe1.pack(pady=10)

seperator=ttk.Separator(ew,orient="horizontal")
seperator.pack(fill='x',padx=5,pady=10)

labe2=Label(ew,text="Employee Name: ",font=f,bg="light grey")
labe2.place(x=20,y=80)
ente2=Entry(ew,font=f,width=25)
ente2.place(x=200,y=80)

labe3=Label(ew,text="Age: ",font=f,bg="light grey")
labe3.place(x=20,y=120)
ente3=Entry(ew,font=f,width=25)
ente3.place(x=200,y=120)

labe4=Label(ew,text="Gender: ",font=f,bg="light grey")
labe4.place(x=20,y=160)
gender=ttk.Combobox(ew, textvariable="Select Gender: ", values=["Male", "Female", "Other"],state="readonly")
gender.place(x=200, y=160)
combo_style = ttk.Style()
combo_style.configure('Custom.TCombobox', font=('Comic Sans-Serif', 15))  # Set the desired font and size
gender['style'] = 'Custom.TCombobox'

labe5=Label(ew,text="Date of Birth: ",font=f,bg="light grey")
labe5.place(x=20,y=200)

cal_text=tk.StringVar()
ente5= DateEntry(ew, width=15, year=2024, month=9, day=20, background='darkblue', foreground='white', borderwidth=2,font=("Comic Sans-Serif",11,"bold"))
ente5.place(x=200,y=200)

labe6=Label(ew,text="Employee-ID: ",font=f,bg="light grey")
labe6.place(x=20,y=240)
ente6=Entry(ew,font=f,width=25)
ente6.place(x=200,y=240)

labe7=Label(ew,text="Position: ",font=f,bg="light grey")
labe7.place(x=20,y=280)
ente7=Entry(ew,font=f,width=25)
ente7.place(x=200,y=280)

labe8=Label(ew,text="Department: ",font=f,bg="light grey")
labe8.place(x=20,y=320)
ente8=Entry(ew,font=f,width=25)
ente8.place(x=200,y=320)

labe9=Label(ew,text="Date of Joining: ",font=f,bg="light grey")
labe9.place(x=20,y=360)

cal_text=tk.StringVar()
ente9=DateEntry(ew, width=15, year=2024, month=9, day=10, background='darkblue', foreground='white', borderwidth=2,font=("Comic Sans-Serif",11,"bold"))
ente9.place(x=200,y=360)

seperator=ttk.Separator(ew,orient="horizontal")
seperator.pack(fill='x',padx=5,pady=313)

labe10=Label(ew,text="Basic Salary: ",font=f,bg="light grey")
labe10.place(x=20,y=400)
ente10=Entry(ew,font=f,width=25)
ente10.place(x=200,y=400)

labe11=Label(ew,text="Working Overtime: ",font=f,bg="light grey")
labe11.place(x=20,y=440)
work=ttk.Combobox(ew, textvariable="Working Overtime: ", values=["Yes","No"],state="readonly")
work.place(x=220, y=440)
combo_style = ttk.Style()
combo_style.configure('Custom.TCombobox', font=('Comic Sans-Serif', 15))  # Set the desired font and size
work['style'] = 'Custom.TCombobox'

labe12=Label(ew,text="Allowances: ",font=f,bg="light grey")
labe12.place(x=20,y=480)
allow=ttk.Combobox(ew, textvariable="Allowances: ", values=["Yes","No"],state="readonly")
allow.place(x=200, y=480)
combo_style = ttk.Style()
combo_style.configure('Custom.TCombobox', font=('Comic Sans-Serif', 15))  # Set the desired font and size
allow['style'] = 'Custom.TCombobox'

labe13=Label(ew,text="If 'Yes' then select option: ",font=f,bg="light grey")
labe13.place(x=20,y=520)
yes=ttk.Combobox(ew, textvariable="Options: ", values=["Housing-->Rs:10,000","Transport-->Rs:5,000","Both-->Rs:15,000","Not Applicable"],state="readonly")
yes.place(x=300, y=520)
combo_style = ttk.Style()
combo_style.configure('Custom.TCombobox', font=('Comic Sans-Serif', 15))  # Set the desired font and size
yes['style'] = 'Custom.TCombobox'

labe14=Label(ew,text="Deductions: ",font=f,bg="light grey")
labe14.place(x=20,y=560)
ente14=Entry(ew,font=f,width=25)
ente14.place(x=200,y=560)

btn1=Button(ew,text="Create Employee Profile",font=f,background="blue",foreground="white",command=save_profile)
btn1.place(x=120,y=620)


# Employee login Window
ep=tk.Tk()
ep.title("Employee-Pannel")
ep.geometry("500x730+100+100")
ep.configure(bg="light grey")
f=("Comic Sans-Serif",15,"bold")
ep.withdraw()

labr1=Label(ep,text="EPS-Employee",font=("Comic Sans-Serif",16,"bold","underline"),bg="light grey")
labr1.pack(pady=10)

seperator=ttk.Separator(ep,orient="horizontal")
seperator.pack(fill='x',padx=5,pady=10)

labr2=Label(ep,text="Employee Name: ",font=f,bg="light grey")
labr2.place(x=20,y=80)
entr2=Entry(ep,font=f,width=25)
entr2.place(x=200,y=80)

labr3=Label(ep,text="Age: ",font=f,bg="light grey")
labr3.place(x=20,y=120)
entr3=Entry(ep,font=f,width=25)
entr3.place(x=200,y=120)

labr4=Label(ep,text="Gender: ",font=f,bg="light grey")
labr4.place(x=20,y=160)
gender1=ttk.Combobox(ep, textvariable="Select Gender: ", values=["Male", "Female", "Other"],state="readonly")
gender1.place(x=200, y=160)
combo_style = ttk.Style()
combo_style.configure('Custom.TCombobox', font=('Comic Sans-Serif', 15))  # Set the desired font and size
gender1['style'] = 'Custom.TCombobox'

labr5=Label(ep,text="Date of Birth: ",font=f,bg="light grey")
labr5.place(x=20,y=200)

cal_text=tk.StringVar()
entr5= DateEntry(ep, width=15, year=2024, month=9, day=20, background='darkblue', foreground='white', borderwidth=2,font=("Comic Sans-Serif",11,"bold"))
entr5.place(x=200,y=200)

labr6=Label(ep,text="Employee-ID: ",font=f,bg="light grey")
labr6.place(x=20,y=240)
entr6=Entry(ep,font=f,width=25)
entr6.place(x=200,y=240)

labr7=Label(ep,text="Position: ",font=f,bg="light grey")
labr7.place(x=20,y=280)
entr7=Entry(ep,font=f,width=25)
entr7.place(x=200,y=280)

labr8=Label(ep,text="Department: ",font=f,bg="light grey")
labr8.place(x=20,y=320)
entr8=Entry(ep,font=f,width=25)
entr8.place(x=200,y=320)

labr9=Label(ep,text="Date of Joining: ",font=f,bg="light grey")
labr9.place(x=20,y=360)

cal_text=tk.StringVar()
entr9=DateEntry(ep, width=15, year=2024, month=9, day=10, background='darkblue', foreground='white', borderwidth=2,font=("Comic Sans-Serif",11,"bold"))
entr9.place(x=200,y=360)

seperator=ttk.Separator(ep,orient="horizontal")
seperator.pack(fill='x',padx=5,pady=313)

labr10=Label(ep,text="Basic Salary: ",font=f,bg="light grey")
labr10.place(x=20,y=400)
entr10=Entry(ep,font=f,width=25)
entr10.place(x=200,y=400)

labr11=Label(ep,text="Working Overtime: ",font=f,bg="light grey")
labr11.place(x=20,y=440)
work1=ttk.Combobox(ep, textvariable="Working Overtime: ", values=["Yes","No"],state="readonly")
work1.place(x=220, y=440)
combo_style = ttk.Style()
combo_style.configure('Custom.TCombobox', font=('Comic Sans-Serif', 15))  # Set the desired font and size
work1['style'] = 'Custom.TCombobox'

labr12=Label(ep,text="Allowances: ",font=f,bg="light grey")
labr12.place(x=20,y=480)
allow1=ttk.Combobox(ep, textvariable="Allowances: ", values=["Yes","No"],state="readonly")
allow1.place(x=200, y=480)
combo_style = ttk.Style()
combo_style.configure('Custom.TCombobox', font=('Comic Sans-Serif', 15))  # Set the desired font and size
allow1['style'] = 'Custom.TCombobox'

labr13=Label(ep,text="If 'Yes' then select option: ",font=f,bg="light grey")
labr13.place(x=20,y=520)
yes1=ttk.Combobox(ep, textvariable="Options: ", values=["Housing-->Rs:10000","Transport-->Rs:5000","Both-->Rs:15000","Not Applicable-->Rs:0"],state="readonly")
yes1.place(x=300, y=520)
combo_style = ttk.Style()
combo_style.configure('Custom.TCombobox', font=('Comic Sans-Serif', 15))  # Set the desired font and size
yes1['style'] = 'Custom.TCombobox'

labr14=Label(ep,text="Deductions: ",font=f,bg="light grey")
labr14.place(x=20,y=560)
entr14=Entry(ep,font=f,width=25)
entr14.place(x=200,y=560)

btn2=Button(ep,text="Edit",font=f,background="blue",foreground="white")
btn2.place(x=110,y=610)

btn3=Button(ep,text="Generate Reports",font=f,background="blue",foreground="white",command=report_open)
btn3.place(x=210,y=610)

btn4=Button(ep,text="LOGOUT",font=f,background="navy blue",foreground="white",command=elogout)
btn4.place(x=200,y=670)


# Employee-Report View Window
er=tk.Tk()
er.title("Employee Reports")
er.geometry("700x600+100+100")
er.configure(bg="light grey")
f=("Comic Sans-Serif",17,"bold")
er.withdraw()

labr7=Label(er,text="EPS-Employee",font=("Comic Sans-Serif",17,"bold","underline"),background="light grey")
labr7.pack(pady=10)

seperator=ttk.Separator(er,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

labr8=Label(er,text="Generated Employee Reports",font=f,background="light grey")
labr8.pack(pady=5)

seperator=ttk.Separator(er,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

er_st_data=ScrolledText(er,width=45,height=10,font=f)
er_st_data.pack(pady=10)

btnr8=Button(er,text="Download Reports(Pdf)",font=f,background="blue",foreground="white",command=save_pdf)
btnr8.pack(pady=10)

seperator=ttk.Separator(er,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

btnr9=Button(er,text="Back to Profile",font=f,background="navy blue",foreground="white",command=epopen)
btnr9.pack(pady=10)


# Admin-Login Main Window
aw= Tk()
aw.title("Admin-Pannel")
aw.geometry("400x460+100+100")
aw.configure(bg="light grey")
f=("Comic Sans-Serif",17,"bold")
aw.withdraw()

lab=Label(aw,text="EPS-Admin",font=("Comic Sans-Serif",17,"bold","underline"),bg="light grey")
lab.pack(pady=10)

separator = ttk.Separator(aw, orient='horizontal')
separator.pack(fill='x', padx=5, pady=10)

lab1=Label(aw,text="Enter the Username: ",font=f,bg="light grey")
lab1.pack(pady=10)
ent1=Entry(aw,font=f)
ent1.pack(pady=11)

lab2=Label(aw,text="Enter the Password: ",font=f,bg="light grey")
lab2.pack(pady=10)
ent2=Entry(aw,font=f,show="*")
ent2.pack(pady=11)

btn=Button(aw,text="LOGIN",font=f,bg="navy blue",foreground="white",command=alogin)
btn.pack(pady=15)

separator = ttk.Separator(aw, orient='horizontal')
separator.pack(fill='x', padx=5, pady=10)

btn1=Button(aw,text="BACK",font=f,bg="navy blue",foreground="white",command=mwopen)
btn1.pack(pady=10)


# Admin-Pannel Window
ap=tk.Tk()
ap.title("Admin-Pannel")
ap.geometry("400x490+100+100")
ap.configure(bg="light grey")
f=("Comic Sans-Serif",17,"bold")
ap.withdraw()

lab3=Label(ap,text="EPS-Admin",font=("Comic Sans-Serif",17,"bold","underline"),background="light grey")
lab3.pack(pady=10)

seperator=ttk.Separator(ap,orient="horizontal")
seperator.pack(fill='x',padx=4, pady=10)

btn1=Button(ap,text="Manage Employee Record",font=f,width=20,command=meropen)
btn1.pack(pady=10)

btn2=Button(ap,text="Salary Calculation",font=f,width=20,command=scopen)
btn2.pack(pady=10)

btn3=Button(ap,text="Payroll Calculation",font=f,width=20,command=psopen)
btn3.pack(pady=10)

btn4=Button(ap,text="Generate Reports",font=f,width=20,command=gwopen)
btn4.pack(pady=10)

btn5=Button(ap,text="LOGOUT",font=f,command=alogout,background="navy blue",foreground="white")
btn5.pack(pady=10)


#Manage-Employee records window
me=tk.Tk()
me.title("Admin-Pannel")
me.geometry("400x500+100+100")
me.configure(bg="light grey")
f=("Comic Sans-Serif",17,"bold")
me.withdraw()

labme1=Label(me,text="EPS-Admin",font=("Comic Sans-Serif",17,"bold","underline"),background="light grey")
labme1.pack(pady=10)

seperator=ttk.Separator(me,orient="horizontal")
seperator.pack(fill='x',padx=4, pady=10)

labme2=Label(me,text="Manage Employee Records",font=f,background="light grey")
labme2.pack(pady=5)

seperator=ttk.Separator(me,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

btnme1=Button(me,text="View Employee Data",font=f,width=20,command=veopen)
btnme1.pack(pady=10)

btnme2=Button(me,text="Add Employee Data",font=f,width=20,command=aeopen)
btnme2.pack(pady=10)

btnme3=Button(me,text="Delete a record",font=f,width=20,command=dropen)
btnme3.pack(pady=10)

btnme4=Button(me,text="Search Employee",font=f,width=20,command=sropen)
btnme4.pack(pady=10)

btnme5=Button(me,text="Back to Main Menu",font=f,background="navy blue",foreground="white",command=gwclose)
btnme5.pack(pady=20)

#View Employee record Window:
ve=tk.Tk()
ve.title("Admin-Pannel-->View Records")
ve.geometry("400x500+100+100")
ve.configure(bg="light grey")
f=("Comic Sans-Serif",15,"bold")
ve.withdraw()

labve1=Label(ve,text="EPS-Admin",font=("Comic Sans-Serif",16,"bold","underline"),bg="light grey")
labve1.pack(pady=10)

seperator=ttk.Separator(ve,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=7)

labve2=Label(ve,text="View Employee Record",font=f,bg="light grey")
labve2.pack(pady=7)

seperator=ttk.Separator(ve,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

ve_data=ScrolledText(ve,width=32,height=11,font=f)
ve_data.pack(pady=10)

btnve1=Button(ve,text="Back",font=f,background="navy blue",foreground="white",command=meopen)
btnve1.place(x=160,y=430)

#Add Employee Record
ae=tk.Tk()
ae.title("Admin-Pannel-->Add Employee")
ae.geometry("500x750+100+100")
ae.configure(bg="light grey")
f=("Comic Sans-Serif",15,"bold")
ae.withdraw()

labae1=Label(ae,text="EPS-Admin",font=("Comic Sans-Serif",16,"bold","underline"),bg="light grey")
labae1.pack(pady=10)

seperator=ttk.Separator(ae,orient="horizontal")
seperator.pack(fill='x',padx=5,pady=10)

labae15=Label(ae,text="Add Employee Records",font=("Comic Sans-Serif",16,"bold","underline"),background="light grey")
labae15.pack(pady=5)

seperator=ttk.Separator(me,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

labae2=Label(ae,text="Employee Name: ",font=f,bg="light grey")
labae2.place(x=20,y=120)
entae2=Entry(ae,font=f,width=25)
entae2.place(x=200,y=120)

labae3=Label(ae,text="Age: ",font=f,bg="light grey")
labae3.place(x=20,y=160)
entae3=Entry(ae,font=f,width=25)
entae3.place(x=200,y=160)

labae4=Label(ae,text="Gender: ",font=f,bg="light grey")
labae4.place(x=20,y=200)
gender4=ttk.Combobox(ae, textvariable="Select Gender: ", values=["Male", "Female", "Other"],state="readonly")
gender4.place(x=200, y=200)
combo_style = ttk.Style()
combo_style.configure('Custom.TCombobox', font=('Comic Sans-Serif', 15))  # Set the desired font and size
gender4['style'] = 'Custom.TCombobox'

labae5=Label(ae,text="Date of Birth: ",font=f,bg="light grey")
labae5.place(x=20,y=240)

cal_text=tk.StringVar()
entae5= DateEntry(ae, width=15, year=2024, month=9, day=20, background='darkblue', foreground='white', borderwidth=2,font=("Comic Sans-Serif",11,"bold"))
entae5.place(x=200,y=240)

labae6=Label(ae,text="Employee-ID: ",font=f,bg="light grey")
labae6.place(x=20,y=280)
entae6=Entry(ae,font=f,width=25)
entae6.place(x=200,y=280)

labae7=Label(ae,text="Position: ",font=f,bg="light grey")
labae7.place(x=20,y=320)
entae7=Entry(ae,font=f,width=25)
entae7.place(x=200,y=320)

labae8=Label(ae,text="Department: ",font=f,bg="light grey")
labae8.place(x=20,y=360)
entae8=Entry(ae,font=f,width=25)
entae8.place(x=200,y=360)

labae9=Label(ae,text="Date of Joining: ",font=f,bg="light grey")
labae9.place(x=20,y=400)
cal_text=tk.StringVar()
entae9=DateEntry(ae, width=15, year=2024, month=9, day=10, background='darkblue', foreground='white', borderwidth=2,font=("Comic Sans-Serif",11,"bold"))
entae9.place(x=200,y=400)

seperator=ttk.Separator(ae,orient="horizontal")
seperator.pack(fill='x',padx=5,pady=413)

labae10=Label(ae,text="Basic Salary: ",font=f,bg="light grey")
labae10.place(x=20,y=440)
entae10=Entry(ae,font=f,width=25)
entae10.place(x=200,y=440)

labae11=Label(ae,text="Working Overtime: ",font=f,bg="light grey")
labae11.place(x=20,y=480)
work4=ttk.Combobox(ae, textvariable="Working Overtime: ", values=["Yes","No"],state="readonly")
work4.place(x=220, y=480)
combo_style = ttk.Style()
combo_style.configure('Custom.TCombobox', font=('Comic Sans-Serif', 15))  # Set the desired font and size
work4['style'] = 'Custom.TCombobox'

labae12=Label(ae,text="Allowances: ",font=f,bg="light grey")
labae12.place(x=20,y=520)
allow4=ttk.Combobox(ae, textvariable="Allowances: ", values=["Yes","No"],state="readonly")
allow4.place(x=200, y=520)
combo_style = ttk.Style()
combo_style.configure('Custom.TCombobox', font=('Comic Sans-Serif', 15))  # Set the desired font and size
allow4['style'] = 'Custom.TCombobox'

labae13=Label(ae,text="If 'Yes' then select option: ",font=f,bg="light grey")
labae13.place(x=20,y=560)
yes4=ttk.Combobox(ae, textvariable="Options: ", values=["Housing-->Rs:10000","Transport-->Rs:5000","Both-->Rs:15000"],state="readonly")
yes4.place(x=300, y=560)
combo_style = ttk.Style()
combo_style.configure('Custom.TCombobox', font=('Comic Sans-Serif', 15))  # Set the desired font and size
yes4['style'] = 'Custom.TCombobox'

labae14=Label(ae,text="Deductions: ",font=f,bg="light grey")
labae14.place(x=20,y=600)
entae14=Entry(ae,font=f,width=25)
entae14.place(x=200,y=600)

btnae2=Button(ae,text="Edit",font=f,background="blue",foreground="white")
btnae2.place(x=110,y=640)

btnae3=Button(ae,text="Add Employee",font=f,background="blue",foreground="white",command=esave_profile)
btnae3.place(x=210,y=640)

btnae4=Button(ae,text="Back",font=f,background="navy blue",foreground="white",command=meopen)
btnae4.place(x=200,y=700)

#Delete a record
dr=tk.Tk()
dr.title("Admin-Pannel-->Delete record")
dr.geometry("400x370+100+100")
dr.configure(bg="light grey")
f=("Comic Sans-Serif",15,"bold")
dr.withdraw()

labdr1=Label(dr,text="EPS-Admin",font=("Comic Sans-Serif",16,"bold","underline"),bg="light grey")
labdr1.pack(pady=10)

seperator=ttk.Separator(dr,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=7)

labdr2=Label(dr,text="Delete a record",font=f,bg="light grey")
labdr2.pack(pady=7)

seperator=ttk.Separator(dr,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

labdr3=Label(dr,text="Enter the Employee-Id to be Deleted: ",font=f,bg="light grey")
labdr3.pack(pady=10)
entdr3=Entry(dr,font=f,width=25)
entdr3.pack(pady=10)

btndr1=Button(dr,text="Delete record",font=f,command=del_record)
btndr1.pack(pady=10)

btndr2=Button(dr,text="Back",font=f,background="navy blue",foreground="white",command=meopen)
btndr2.pack(pady=10)

#Search a Employee record
sr=tk.Tk()
sr.title("Admin-Pannel-->Search a record")
sr.geometry("400x500+100+100")
sr.configure(bg="light grey")
f=("Comic Sans-Serif",15,"bold")
sr.withdraw()

labsr1=Label(sr,text="EPS-Admin",font=("Comic Sans-Serif",16,"bold","underline"),bg="light grey")
labsr1.pack(pady=10)

seperator=ttk.Separator(sr,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=7)

labsr2=Label(sr,text="Search Employee record",font=f,bg="light grey")
labsr2.pack(pady=7)

seperator=ttk.Separator(sr,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

labsr3=Label(sr,text="Enter the Employee-Id to Search: ",font=f,bg="light grey")
labsr3.place(x=5,y=140)
entsr3=Entry(sr,font=f,width=5)
entsr3.place(x=320,y=140)

btnsr1=Button(sr,text="Search record",font=f)
btnsr1.pack(pady=60)

sr_data=ScrolledText(sr,width=32,height=7,font=f)
sr_data.place(x=10,y=250)

btnsr2=Button(sr,text="Back",font=f,background="navy blue",foreground="white",command=meopen)
btnsr2.place(x=160,y=440)


# Salary calculations Window
sc=tk.Tk()
sc.title("Salary Calculation")
sc.geometry("500x610+100+100")
sc.configure(bg="light grey")
f=("Comic Sans-Serif",15,"bold")
sc.withdraw()

labsc1=Label(sc,text="EPS-Admin",font=("Comic Sans-Serif",16,"bold","underline"),bg="light grey")
labsc1.pack(pady=10)

seperator=ttk.Separator(sc,orient="horizontal")
seperator.pack(fill='x',padx=5,pady=10)

labsc8=Label(sc,text="Salary Calculations",font=f,background="light grey")
labsc8.pack(pady=5)

seperator=ttk.Separator(sc,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

labsc2=Label(sc,text="Employee-ID: ",font=f,bg="light grey")
labsc2.place(x=20,y=140)
entsc2=Entry(sc,font=f,width=25)
entsc2.place(x=200,y=140)

labsc3=Label(sc,text="Employee Name: ",font=f,bg="light grey")
labsc3.place(x=20,y=180)
entsc3=Entry(sc,font=f,width=25)
entsc3.place(x=200,y=180)

labsc4=Label(sc,text="Basic Salary: ",font=f,bg="light grey")
labsc4.place(x=20,y=220)
entsc4=Entry(sc,font=f,width=25)
entsc4.place(x=200,y=220)

labsc5=Label(sc,text="Working Overtime: ",font=f,bg="light grey")
labsc5.place(x=20,y=260)
entsc6=Entry(sc,font=f,width=25)
entsc6.place(x=210, y=260)

labsc6=Label(sc,text="Allowances: ",font=f,bg="light grey")
labsc6.place(x=20,y=300)
yes2=ttk.Combobox(sc, textvariable="Options: ", values=["Housing-->Rs:10000","Transport-->Rs:5000","Both-->Rs:15000","Not Applicable-->Rs:0"],state="readonly")
yes2.place(x=220, y=300)

labsc7=Label(sc,text="Deductions: ",font=f,bg="light grey")
labsc7.place(x=20,y=340)
entsc5=Entry(sc,font=f,width=25)
entsc5.place(x=200,y=340)

labsc9=Label(sc,text="Gross-Salary: ",font=f,background="light grey")
labsc9.place(x=20,y=380)

labsc10=Label(sc,text="Net-Salary: ",font=f,background="light grey")
labsc10.place(x=20,y=420)

btnsc1=Button(sc,text="Clear",font=f,background="blue",foreground="white",command=clear_data)
btnsc1.place(x=120,y=470)

btnsc2=Button(sc,text="Calculate Salary",font=f,background="blue",foreground="white",command=c_salary)
btnsc2.place(x=230,y=470)

seperator=ttk.Separator(sc,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=430)

btnsc3=Button(sc,text="Back to Main Menu",font=f,background="navy blue",foreground="white",command=gwclose)
btnsc3.place(x=160,y=540)



# Payroll-Stub calculations Window
ps=tk.Tk()
ps.title("Payroll Calculation")
ps.geometry("500x640+100+100")
ps.configure(bg="light grey")
f=("Comic Sans-Serif",15,"bold")
ps.withdraw()

labps1=Label(ps,text="EPS-Admin",font=("Comic Sans-Serif",16,"bold","underline"),bg="light grey")
labps1.pack(pady=10)

seperator=ttk.Separator(ps,orient="horizontal")
seperator.pack(fill='x',padx=5,pady=10)

labps8=Label(ps,text="Payroll Calculations",font=f,background="light grey")
labps8.pack(pady=5)

seperator=ttk.Separator(ps,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

labps2=Label(ps,text="Employee-ID: ",font=f,bg="light grey")
labps2.place(x=20,y=140)
entps2=Entry(ps,font=f,width=25)
entps2.place(x=200,y=140)

labps3=Label(ps,text="Employee Name: ",font=f,bg="light grey")
labps3.place(x=20,y=180)
entps3=Entry(ps,font=f,width=25)
entps3.place(x=200,y=180)

labps4=Label(ps,text="Basic Salary: ",font=f,bg="light grey")
labps4.place(x=20,y=220)
entps4=Entry(ps,font=f,width=25)
entps4.place(x=200,y=220)

labps5=Label(ps,text="Working Overtime: ",font=f,bg="light grey")
labps5.place(x=20,y=260)
entps6=Entry(ps,font=f,width=25)
entps6.place(x=210, y=260)

labps6=Label(ps,text="Allowances: ",font=f,bg="light grey")
labps6.place(x=20,y=300)
yes3=ttk.Combobox(ps, textvariable="Options: ", values=["Housing-->Rs:10000","Transport-->Rs:5000","Both-->Rs:15000","Not Applicable-->Rs:0"],state="readonly")
yes3.place(x=220, y=300)

labps7=Label(ps,text="Deductions: ",font=f,bg="light grey")
labps7.place(x=20,y=340)
entps5=Entry(ps,font=f,width=25)
entps5.place(x=200,y=340)

labps9=Label(ps,text="Select Pay Stub Period: ",font=f,bg="light grey")
labps9.place(x=20,y=380)
#val1=ttk.Combobox(ps, textvariable="select: ", values=["Weekly","Bi-Weekly"],state="readonly")
 # Set default value to "Monthly"
week1= ttk.Combobox(ps,values=["Monthly", "Bi-Weekly"],state="readonly")
week1.place(x=260, y=380)

labps10=Label(ps,text=" ",font=f,background="light grey")
labps10.place(x=20,y=420)

labps11=Label(ps,text=" ",font=f,background="light grey")
labps11.place(x=20,y=460)

btnps1=Button(ps,text="Clear",font=f,background="blue",foreground="white",command=clear_paydata)
btnps1.place(x=120,y=500)

btnps2=Button(ps,text="Calculate Payroll",font=f,background="blue",foreground="white",command=c_payroll)
btnps2.place(x=230,y=500)

btnps3=Button(ps,text="Back to Main Menu",font=f,background="navy blue",foreground="white",command=gwclose)
btnps3.place(x=160,y=570)


#Generate Reports Window
gw=tk.Tk()
gw.title("Generate Reports")
gw.geometry("700x430+100+100")
gw.configure(bg="light grey")
f=("Comic Sans-Serif",17,"bold")
gw.withdraw()

lab4=Label(gw,text="EPS-Admin",font=("Comic Sans-Serif",17,"bold","underline"),background="light grey")
lab4.pack(pady=10)

seperator=ttk.Separator(gw,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

lab5=Label(gw,text="Generate Reports",font=f,background="light grey")
lab5.pack(pady=5)

seperator=ttk.Separator(gw,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

lab6=Label(gw,text="Filter Reports by",font=f,background="light grey")
lab6.pack(pady=10)

var=tk.StringVar()
#dropdown=tk.OptionMenu(gw,var,*droplist,command=handle_selection)
value1=["Select Option", "Department", "Position", "Time-Period"]
dropdown = tk.OptionMenu(gw, var, *value1, command=handle_selection)
dropdown.configure(font=f)
dropdown["menu"].config(font=("Comic Sans-Serif",15),background="lightgrey", foreground="black")
var.set(value1[0])
dropdown.pack(pady=10)

btn6=Button(gw,text="Generate Reports",font=f,background="blue",foreground="white",command=gropen)
btn6.pack(pady=10)

seperator=ttk.Separator(gw,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

btn7=Button(gw,text="Back to Main Menu",font=f,background="navy blue",foreground="white",command=gwclose)
btn7.pack(pady=10)


#Generated Report View Window
gr=tk.Tk()
gr.title("Generated Reports")
gr.geometry("700x600+100+100")
gr.configure(bg="light grey")
f=("Comic Sans-Serif",17,"bold")
gr.withdraw()

lab7=Label(gr,text="EPS-Admin",font=("Comic Sans-Serif",17,"bold","underline"),background="light grey")
lab7.pack(pady=10)

seperator=ttk.Separator(gr,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

lab8=Label(gr,text="Generated Reports",font=f,background="light grey")
lab8.pack(pady=5)

seperator=ttk.Separator(gr,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

gr_st_data=ScrolledText(gr,width=45,height=10,font=f)
gr_st_data.pack(pady=10)

btn8=Button(gr,text="Download Reports(Pdf)",font=f,background="blue",foreground="white",command=asave_pdf)
btn8.pack(pady=10)

seperator=ttk.Separator(gr,orient="horizontal")
seperator.pack(fill='x',padx=4,pady=10)

btn9=Button(gr,text="Back to Main Menu",font=f,background="navy blue",foreground="white",command=gwclose)
btn9.pack(pady=10)


def on_closing():
    if askokcancel("Quit","Do you want to Exit?"):
        aw.destroy()
        ap.destroy()
        gw.destroy()
        gr.destroy()
        mw.destroy()
        em.destroy()
        ew.destroy()
        ep.destroy()
        er.destroy()
        sw.destroy()
        sc.destroy()
        ps.destroy()
        ae.destroy()
        me.destroy()
        dr.destroy()
        sr.destroy()
        ve.destroy()

aw.protocol("WM_DELETE_WINDOW",on_closing)
ap.protocol("WM_DELETE_WINDOW",on_closing)
gw.protocol("WM_DELETE_WINDOW",on_closing)
gr.protocol("WM_DELETE_WINDOW",on_closing)
mw.protocol("WM_DELETE_WINDOW",on_closing)
em.protocol("WM_DELETE_WINDOW",on_closing)
ew.protocol("WM_DELETE_WINDOW",on_closing)
ep.protocol("WM_DELETE_WINDOW",on_closing)
er.protocol("WM_DELETE_WINDOW",on_closing)
sw.protocol("WM_DELETE_WINDOW",on_closing)
sc.protocol("WM_DELETE_WINDOW",on_closing)
ps.protocol("WM_DELETE_WINDOW",on_closing)
ae.protocol("WM_DELETE_WINDOW",on_closing)
me.protocol("WM_DELETE_WINDOW",on_closing)
dr.protocol("WM_DELETE_WINDOW",on_closing)
sr.protocol("WM_DELETE_WINDOW",on_closing)
ve.protocol("WM_DELETE_WINDOW",on_closing)

mw.mainloop() 



