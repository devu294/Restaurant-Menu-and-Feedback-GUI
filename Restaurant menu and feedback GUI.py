import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random
import webbrowser


window=tk.Tk()
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Restaurant Menu")

l1=tk.Label(window, text = "Welcome to our restaurant",pady=50, font=("Arial Bold",50))
l1.pack()


def menu_pg():

    def regular_menu():
        im = Image.open(r"") #Add image URL Here
        im.show()

    def advance_menu():

        pg_2=tk.Tk()
        width= pg_2.winfo_screenwidth()
        height= pg_2.winfo_screenheight()
        pg_2.geometry("%dx%d" % (width, height))
        pg_2.title("Restaurant Menu")

        fm=Frame(pg_2, padx=350, pady=20)
        fm.grid()
        
        #Question 1
        q1=Label(fm, text="Q. How are you feeling today?", padx=50, pady=15, font=("Arial Bold",20))
        q1.grid()

        q1_value=StringVar()
        q1_entry=Entry(fm, textvariable=q1_value, font=("Arial",20))
        q1_entry.grid()

        #BlankLabel
        Label(fm, text="",pady=20).grid()

        #questiion 2
        q2=Label(fm, text="Q. What's your taste?", pady=10, font=("Arial Bold",20)).grid()
        q21=Label(fm, text="1. Spicy", font=("Arial ",12)).grid()
        q22=Label(fm, text="2. Mild Spicy", font=("Arial ",12)).grid()
        q23=Label(fm, text="3. Sweet", font=("Arial ",12)).grid()
        q24=Label(fm, text="4. Sour", font=("Arial ",12)).grid()

        q2_value=StringVar()
        q2_entry=Entry(fm, textvariable=q2_value, font=("Arial",20))
        q2_entry.grid()


        #BlankLabel
        Label(fm, text="",pady=20).grid()

        #Question 3
        q3=Label(fm, text="Q. Are you allergic to any food item?", font=("Arial Bold",20))
        q3.grid()

        q3_value=IntVar()
        q3_cb1=Radiobutton(fm , text="YES", variable=q3_value ,value=1, font=("Helvetica",15)).grid()
        q3_cb2=Radiobutton(fm , text="NO", variable=q3_value, value=2, font=("Helvetica",15)).grid()

        Ifyes=Label(fm, text="If yes please specify ", font=("Helvetica",15) ).grid(row=100, column=0)
        Ifyes_value=StringVar()
        Ifyes_entry=Entry(fm, textvariable= Ifyes_value, font=("Arial",20)).grid(row=100, column=1)


        #BlankLabel
        Label(fm, text="",pady=20).grid()





        #####################################

        def V_NV():
            pg_3=tk.Tk()
            width= pg_3.winfo_screenwidth()
            height= pg_3.winfo_screenheight()
            pg_3.geometry("%dx%d" % (width, height))
            pg_3.title("Restaurant Menu")

            fm=Frame(pg_3, padx=250, pady=20)
            fm.grid(row=10, column=10)

            q=Label(fm, text="Q. Are you veg or Non-Veg", padx=50, pady=15, font=("Arial Bold",20))
            q.grid(row=0, column=10)

            def Veg():

                V_fm=Frame(pg_3, padx=250, pady=20)
                fm.grid(row=70, column=10)

                V_Label=Label(fm, text="Our suggestions are", pady=50, font=("Arial",25)).grid(row=80, column=10)

                
                veg=["Vegetarian Mushroom Risotto","Vegetable Lasagna","Penne A Le Vodka", "Lentil Sweet Potato Shepherd's Pie",
                "Butternut Squash Ravioli With White Wine Sauce","Classic Italian Potato Gnocchi", "Spaghetti With Winter Vegetables Sauce",
                "Baked Macaroni and Cheese","traditional ratatouille","Spinach and Ricotta Baked Stuffed Shells"]

                item=random.choices(veg, k = 4)

                Label(fm, text=item, pady= 25, font=("Arial Bold",15)).grid(row=100, column=10)

                #BlankLabel
                Label(fm, text="",pady=5).grid()
                
                Label(fm, text="Enter your choice here",font=("Arial ",10)).grid(row=120, column=10)

                
                value= StringVar()
                entry=Entry(fm, textvariable=value, font=("Arial",20)).grid(row=140, column=10)

                #BlankLabel
                Label(fm, text="",pady=20).grid()

                def submission_page():
                    
                    pg_5=tk.Tk()
                    width= pg_5.winfo_screenwidth()
                    height= pg_5.winfo_screenheight()
                    pg_5.geometry("%dx%d" % (width, height))
                    pg_5.title("Restaurant Menu")

                    fm=Frame(pg_5, padx=350, pady=20)
                    fm.grid()

                    Label(fm, text="Your food is preparing", pady=50, font=("Arial Bold",50)).grid()

                    #BlankLabel
                    Label(fm, text="",pady=100).grid()

                    def payment_pg():
                        pg_6=tk.Tk()
                        width= pg_6.winfo_screenwidth()
                        height= pg_6.winfo_screenheight()
                        pg_6.geometry("%dx%d" % (width, height))
                        pg_6.title("Restaurant Menu")

                        fm=Frame(pg_6, padx=350, pady=20)
                        fm.grid()

                        Label(fm, text= "Choose your Payment mode", pady=50, font=("Arial Bold",30)).grid()


                        #BlankLabel
                        Label(fm, text="",pady=50).grid()


                    #Card Payemnt
                        def cc_dc():
                            pg_7=tk.Tk()
                            width= pg_7.winfo_screenwidth()
                            height= pg_7.winfo_screenheight()
                            pg_7.geometry("%dx%d" % (width, height))
                            pg_7.title("Restaurant Menu")

                            Label(pg_7, text="Card machine on its way..",  pady=50, font=("Arial Bold",50)).grid()            
                                

                                

                        Button(fm, text="Credit Card / Debit Card", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25,command=cc_dc).grid()


                    #Netbanking
                        def netbanking():
                            
                            pg_7=tk.Tk()
                            width= pg_7.winfo_screenwidth()
                            height= pg_7.winfo_screenheight()
                            pg_7.geometry("%dx%d" % (width, height))
                            pg_7.title("Restaurant Menu")

                            fm=Frame(pg_7, padx=350, pady=20)
                            fm.grid()

                            Label(fm, text="Choose your bank", pady=50, font=("Arial Bold",30)).grid()
                                
                            def hdfc():
                                url1='https://netbanking.hdfcbank.com/netbanking/'
                                webbrowser.open_new_tab(url1)

                            def icici():
                                url2='https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=ICI&ITM=nli_cms_IB_internetbanking_login_btn&_gl=1*8pxqn4*_ga*Mjc3NDE3NTkxLjE2NDEyMDA2NjY.*_ga_SKB78GHTFV*MTY0MjEzNjIxMS4zNy4xLjE2NDIxMzg3MzEuMjM.&_ga=2.235261633.1704225377.1672896575-1704339805.1672896575'
                                webbrowser.open_new_tab(url2)

                            def sbi():
                                url3='https://www.onlinesbi.sbi/'
                                webbrowser.open_new_tab(url3)

                            def pnb():
                                url4='https://netpnb.com/'
                                webbrowser.open_new_tab(url4)
                                    
                                    
                            Button(fm, text="HDFC BANK", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=hdfc).grid()
                            Button(fm, text="ICICI BANK", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=icici).grid()
                            Button(fm, text="SBI BANK", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=sbi).grid()
                            Button(fm, text="PNB BANK", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=pnb).grid()

                        Button(fm, text="Netbanking", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=netbanking).grid()
                                



                    #Upi payment
                        def upi():
                            qrim = Image.open(r"") #upload UPI QR CODE HERE
                            qrim.show()

                        Button(fm, text="UPI", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=upi).grid()


                    #Cash Payment
                        def cash():
                            pg_7=tk.Tk()
                            width= pg_7.winfo_screenwidth()
                            height= pg_7.winfo_screenheight()
                            pg_7.geometry("%dx%d" % (width, height))
                            pg_7.title("Restaurant Menu")

                            Label(pg_7, text="Waiter on his way to collect the cash..",  pady=50, font=("Arial Bold",50)).grid()
                                
                        Button(fm, text="Cash", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=cash).grid()


                        #BlankLabel
                        Label(fm, text="",pady=5).grid(row=350, column=100)


                        def feedback():
                            
                            pg_8=tk.Tk()
                            width= pg_8.winfo_screenwidth()
                            height= pg_8.winfo_screenheight()
                            pg_8.geometry("%dx%d" % (width, height))
                            pg_8.title("Feedback")

                            fm=Frame(pg_8, padx=250, pady=20)
                            fm.grid(row=10, column=10)

                            #Question 1
                            fb1=Label(fm, text="Q. How was your overall experience ?", font=("Arial Bold",20))
                            fb1.grid()

                            fb1_value=IntVar()
                            fb1_cb1=Radiobutton(fm , text="Too bad", variable=fb1_value ,value=1, font=("Helvetica",15)).grid()
                            fb1_cb2=Radiobutton(fm , text="Poor", variable=fb1_value ,value=2, font=("Helvetica",15)).grid()
                            fb1_cb3=Radiobutton(fm , text="Fine", variable=fb1_value ,value=3, font=("Helvetica",15)).grid()
                            fb1_cb4=Radiobutton(fm , text="Good", variable=fb1_value ,value=4, font=("Helvetica",15)).grid()
                            fb1_cb5=Radiobutton(fm , text="Excellent", variable=fb1_value ,value=5, font=("Helvetica",15)).grid()


                            #BlankLabel
                            Label(fm, text="",pady=10).grid()

                            #Question 2
                            fb2=Label(fm, text="Q. Was the space clean and organised ?", font=("Arial Bold",20))
                            fb2.grid()

                            fb2_value=IntVar()
                            fb2_cb1=Radiobutton(fm , text="YES", variable=fb2_value ,value=1, font=("Helvetica",15)).grid()
                            fb2_cb2=Radiobutton(fm , text="NO", variable=fb2_value, value=2, font=("Helvetica",15)).grid()

                            #BlankLabel
                            Label(fm, text="",pady=10).grid()


                            #Question 3
                            fb3=Label(fm, text="Q. Is there anything we need to improve ?", font=("Arial Bold",20))
                            fb3.grid()

                            q3_value=IntVar()
                            q3_cb1=Radiobutton(fm , text="YES", variable=q3_value ,value=1, font=("Helvetica",15)).grid()
                            q3_cb2=Radiobutton(fm , text="NO", variable=q3_value, value=2, font=("Helvetica",15)).grid()

                            Ifyes=Label(fm, text="If yes please specify ", font=("Helvetica",15) ).grid(row=100, column=0)
                            Ifyes_value=StringVar()
                            Ifyes_entry=Entry(fm, textvariable= Ifyes_value, font=("Arial",20)).grid(row=100, column=1)

                            #BlankLabel
                            Label(fm, text="",pady=10).grid()

                            def end():
                                pg_9=tk.Tk()
                                width= pg_9.winfo_screenwidth()
                                height= pg_9.winfo_screenheight()
                                pg_9.geometry("%dx%d" % (width, height))
                                pg_9.title("Feedback")

                                fm=Frame(pg_9, padx=250, pady=20)
                                fm.grid(row=10, column=10)

                                lab=Label(fm, text = "Thank you for your feedback",pady=50, font=("Arial Bold",50))
                                lab.pack()
                                

                            Button(fm, text="Next", font=("Helvetica Bold",10), bg="orange" ,pady=10, height= 1, width=15, command=end).grid()

                    

                        Button(fm, text="Next", font=("Helvetica Bold",10), bg="orange" ,pady=10, height= 1, width=15,command=feedback).grid()

                        


                        

                    Button(fm, text="Next", font=("Helvetica Bold",10), bg="orange" ,pady=10, height= 1, width=15, command=payment_pg).grid()




                Button(fm, text="Next", font=("Helvetica Bold",10), bg="orange" ,pady=10, height= 1, width=15, command=submission_page).grid(row=160, column=10)

                
            def N_veg():
                V_fm=Frame(pg_3, padx=250, pady=20)
                fm.grid(row=70, column=10)

                V_Label=Label(fm, text="Our suggestions are", pady=50, font=("Arial",25)).grid(row=80, column=10)

                Nveg=["Garlic Butter Shrimps", "Rava Fried Prawns", " Filet-O-Fish Burger", "Chicken Dimsums",
                "Hakka Chicken Noodles", "led Chicken Escalope with Fresh Salsa", "Grilled Chicken Wraps", "Murgh Seekh Kebab", "Crab Curry", "Butter Chicken"]

                item=random.choices(Nveg, k = 4)

                Label(fm, text=item, pady= 25, font=("Arial Bold",10)).grid(row=100, column=10)

                value= StringVar()
                entry=Entry(fm, textvariable=value, font=("Arial",20)).grid(row=120, column=10)

                #BlankLabel
                Label(fm, text="",pady=20).grid()

                def submission_page():
                    
                    pg_5=tk.Tk()
                    width= pg_5.winfo_screenwidth()
                    height= pg_5.winfo_screenheight()
                    pg_5.geometry("%dx%d" % (width, height))
                    pg_5.title("Restaurant Menu")

                    fm=Frame(pg_5, padx=350, pady=20)
                    fm.grid()

                    Label(fm, text="Your food is preparing", pady=50, font=("Arial Bold",50)).grid()

                    #BlankLabel
                    Label(fm, text="",pady=100).grid()

                    def payment_pg():
                        pg_6=tk.Tk()
                        width= pg_6.winfo_screenwidth()
                        height= pg_6.winfo_screenheight()
                        pg_6.geometry("%dx%d" % (width, height))
                        pg_6.title("Restaurant Menu")

                        fm=Frame(pg_6, padx=350, pady=20)
                        fm.grid()

                        Label(fm, text= "Choose your Payment mode", pady=50, font=("Arial Bold",30)).grid()


                        #BlankLabel
                        Label(fm, text="",pady=50).grid()


                    #Card Payemnt
                        def cc_dc():
                            pg_7=tk.Tk()
                            width= pg_7.winfo_screenwidth()
                            height= pg_7.winfo_screenheight()
                            pg_7.geometry("%dx%d" % (width, height))
                            pg_7.title("Restaurant Menu")

                            Label(pg_7, text="Card machine on its way..",  pady=50, font=("Arial Bold",50)).grid()            
                                

                                

                        Button(fm, text="Credit Card / Debit Card", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25,command=cc_dc).grid()


                    #Netbanking
                        def netbanking():
                            
                            pg_7=tk.Tk()
                            width= pg_7.winfo_screenwidth()
                            height= pg_7.winfo_screenheight()
                            pg_7.geometry("%dx%d" % (width, height))
                            pg_7.title("Restaurant Menu")

                            fm=Frame(pg_7, padx=350, pady=20)
                            fm.grid()

                            Label(fm, text="Choose your bank", pady=50, font=("Arial Bold",30)).grid()
                                
                            def hdfc():
                                url1='https://netbanking.hdfcbank.com/netbanking/'
                                webbrowser.open_new_tab(url1)

                            def icici():
                                url2='https://infinity.icicibank.com/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=1&BANK_ID=ICI&ITM=nli_cms_IB_internetbanking_login_btn&_gl=1*8pxqn4*_ga*Mjc3NDE3NTkxLjE2NDEyMDA2NjY.*_ga_SKB78GHTFV*MTY0MjEzNjIxMS4zNy4xLjE2NDIxMzg3MzEuMjM.&_ga=2.235261633.1704225377.1672896575-1704339805.1672896575'
                                webbrowser.open_new_tab(url2)

                            def sbi():
                                url3='https://www.onlinesbi.sbi/'
                                webbrowser.open_new_tab(url3)

                            def pnb():
                                url4='https://netpnb.com/'
                                webbrowser.open_new_tab(url4)
                                    
                                    
                            Button(fm, text="HDFC BANK", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=hdfc).grid()
                            Button(fm, text="ICICI BANK", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=icici).grid()
                            Button(fm, text="SBI BANK", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=sbi).grid()
                            Button(fm, text="PNB BANK", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=pnb).grid()

                        Button(fm, text="Netbanking", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=netbanking).grid()
                                



                    #Upi payment
                        def upi():
                            qrim = Image.open(r" ") #upload UPI QR CODE HERE
                            qrim.show()

                        Button(fm, text="UPI", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=upi).grid()


                    #Cash Payment
                        def cash():
                            pg_7=tk.Tk()
                            width= pg_7.winfo_screenwidth()
                            height= pg_7.winfo_screenheight()
                            pg_7.geometry("%dx%d" % (width, height))
                            pg_7.title("Restaurant Menu")

                            Label(pg_7, text="Waiter on his way to collect the cash..",  pady=50, font=("Arial Bold",50)).grid()
                                
                        Button(fm, text="Cash", font=("Helvetica Bold",10), bg="grey" ,pady=10, height= 1, width=25, command=cash).grid()


                        #BlankLabel
                        Label(fm, text="",pady=5).grid(row=350, column=100)


                        def feedback():
                            
                            pg_8=tk.Tk()
                            width= pg_8.winfo_screenwidth()
                            height= pg_8.winfo_screenheight()
                            pg_8.geometry("%dx%d" % (width, height))
                            pg_8.title("Feedback")

                            fm=Frame(pg_8, padx=250, pady=20)
                            fm.grid(row=10, column=10)

                            #Question 1
                            fb1=Label(fm, text="Q. How was your overall experience ?", font=("Arial Bold",20))
                            fb1.grid()

                            fb1_value=IntVar()
                            fb1_cb1=Radiobutton(fm , text="Too bad", variable=fb1_value ,value=1, font=("Helvetica",15)).grid()
                            fb1_cb2=Radiobutton(fm , text="Poor", variable=fb1_value ,value=2, font=("Helvetica",15)).grid()
                            fb1_cb3=Radiobutton(fm , text="Fine", variable=fb1_value ,value=3, font=("Helvetica",15)).grid()
                            fb1_cb4=Radiobutton(fm , text="Good", variable=fb1_value ,value=4, font=("Helvetica",15)).grid()
                            fb1_cb5=Radiobutton(fm , text="Excellent", variable=fb1_value ,value=5, font=("Helvetica",15)).grid()


                            #BlankLabel
                            Label(fm, text="",pady=10).grid()

                            #Question 2
                            fb2=Label(fm, text="Q. Was the space clean and organised ?", font=("Arial Bold",20))
                            fb2.grid()

                            fb2_value=IntVar()
                            fb2_cb1=Radiobutton(fm , text="YES", variable=fb2_value ,value=1, font=("Helvetica",15)).grid()
                            fb2_cb2=Radiobutton(fm , text="NO", variable=fb2_value, value=2, font=("Helvetica",15)).grid()

                            #BlankLabel
                            Label(fm, text="",pady=10).grid()


                            #Question 3
                            fb3=Label(fm, text="Q. Is there anything we need to improve ?", font=("Arial Bold",20))
                            fb3.grid()

                            q3_value=IntVar()
                            q3_cb1=Radiobutton(fm , text="YES", variable=q3_value ,value=1, font=("Helvetica",15)).grid()
                            q3_cb2=Radiobutton(fm , text="NO", variable=q3_value, value=2, font=("Helvetica",15)).grid()

                            Ifyes=Label(fm, text="If yes please specify ", font=("Helvetica",15) ).grid(row=100, column=0)
                            Ifyes_value=StringVar()
                            Ifyes_entry=Entry(fm, textvariable= Ifyes_value, font=("Arial",20)).grid(row=100, column=1)

                            #BlankLabel
                            Label(fm, text="",pady=10).grid()

                            def end():
                                pg_9=tk.Tk()
                                width= pg_9.winfo_screenwidth()
                                height= pg_9.winfo_screenheight()
                                pg_9.geometry("%dx%d" % (width, height))
                                pg_9.title("Feedback")

                                fm=Frame(pg_9, padx=250, pady=20)
                                fm.grid(row=10, column=10)

                                lab=Label(fm, text = "Thank you for your feedback",pady=50, font=("Arial Bold",50))
                                lab.pack()
                                

                            Button(fm, text="Next", font=("Helvetica Bold",10), bg="orange" ,pady=10, height= 1, width=15, command=end).grid()

                    

                        Button(fm, text="Next", font=("Helvetica Bold",10), bg="orange" ,pady=10, height= 1, width=15,command=feedback).grid()

                        


                        

                    Button(fm, text="Next", font=("Helvetica Bold",10), bg="orange" ,pady=10, height= 1, width=15, command=payment_pg).grid()



                    

                Button(fm, text="Submit", font=("Helvetica Bold",10), bg="orange" ,pady=20,height= 1, width=15, command=submission_page).grid(row=140, column=10)
                

    ##########################            

            Button(fm, text="Veg", bg="orange", pady=25, font=("Helvetica Bold",10),height= 1, width=15, command=Veg).grid(row=10, column=10)
            Button(fm, text="Non-Veg", bg="orange", pady=25, font=("Helvetica Bold",10),height= 1, width=15, command=N_veg).grid(row=40, column=10)

            pg_3.mainloop()
        

        #Submit_Button
        Button(fm, text="Submit", bg="orange", pady=25, font=("Helvetica Bold",10), height= 1, width=15, command=V_NV).grid()

            
            
    pg_1=tk.Tk()
    width= window.winfo_screenwidth()
    height= window.winfo_screenheight()
    pg_1.geometry("%dx%d" % (width, height))
    
    pg_1.title("Restaurant Menu")
    

    fm=Frame(pg_1,pady=50)
    fm.pack()

    rm_bt=Button(fm, text="Regular Menu", bg="orange", fg="black",padx=30, pady=50, borderwidth=3, relief=SUNKEN, font=("Arial Bold",20), command=regular_menu)
    rm_bt.pack(side=TOP,pady=20)

    am_bt=Button(fm, text="Advance Menu", bg="orange", fg="black",padx=30, pady=50, borderwidth=3, relief=SUNKEN, font=("Arial Bold",20), command=advance_menu)
    am_bt.pack(side=TOP,pady=20)
    
    

fm1=Frame(window)
fm1.pack()

startbt=Button(fm1, text="Start", bg="orange", fg="black", font=("Arial Bold",20), command=menu_pg)
startbt.pack()

window.mainloop()
