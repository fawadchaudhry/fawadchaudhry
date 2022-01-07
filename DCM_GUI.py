## GUI Module
## Most of the functionality of the DCM is in this module
## including GUI objects and external module calls
## Hopefully this works out...
## ... I'm so tired

from tkinter import *
from tkinter import ttk
from tkinter import font as tkFont
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from decimal import Decimal
import DCM_users
import DCM_modes

import DCM_SerialClass

class DialogBox: #Pop-up
	def __init__(self,parent,text):
		top = self.top = Toplevel(parent)
		self.top.title("Notice")
		ttk.Label(top,text=text).grid(column=1,row=2,columnspan=3,padx=20,pady=20)
		ttk.Button(top,text="Okay",command=self.ok).grid(column=2,row=4,padx=20,pady=20)
	def ok(self):
		self.top.destroy()


class GUI:
	def __init__(self,master):
		self.master = master
		self.master.title("SECOND HEART BEATS DCM")

		# Create the user list
		self.List = DCM_users.UserList()
		self.List.loadFile("users.txt")

		# Create an instance of the Serial Module
		self.serialComm = DCM_SerialClass.Serial()

		#Create the pacing modes
		self.modes = [
                        DCM_modes.PacemakerMode("AOO"),
                        DCM_modes.PacemakerMode("VOO"),
                        DCM_modes.PacemakerMode("AAI"),
                        DCM_modes.PacemakerMode("VVI"),
                        DCM_modes.PacemakerMode("DOO"),
                        DCM_modes.PacemakerMode("AOOR"),
                        DCM_modes.PacemakerMode("VOOR"),
                        DCM_modes.PacemakerMode("AAIR"),
                        DCM_modes.PacemakerMode("VVIR"),
                        DCM_modes.PacemakerMode("DOOR"),
                ]
		
		# Screen 1.1 -- LOGIN/REGISTER CHOICE
		self.frame1 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame1.grid(row=0,column=0)
		self.frame1.grid_propagate(0)

		ttk.Label(self.frame1,text="Welcome to the Second Heart Beats'\n           Pacemaker DCM",font=(12),foreground="blue")\
								 .place(rely=0.2,relx=0.5,anchor=CENTER)
		self.login = ttk.Button(self.frame1,text="Login", width=20,command=lambda:self.RaiseFrame(self.frame3))\
								 .place(rely=0.475,relx=0.5,anchor=CENTER)
		self.register = ttk.Button(self.frame1,text="Register",width=20,command=lambda:self.RaiseFrame(self.frame2))\
								 .place(rely=0.65,relx=0.5,anchor=CENTER)
		self.exit = ttk.Button(self.frame1,text="Exit",command=self.Exit)\
								 .place(rely=0.9,relx=0.85,anchor=CENTER)

		# Screen 1.2 -- REGISTER NEW USER
		self.frame2 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame2.grid(row=0,column=0)
		self.frame2.grid_propagate(0)

		ttk.Label(self.frame2,text="Please enter your new username and password",font=(10),foreground="blue")\
									  .place(rely=0.1,relx=0.5,anchor=CENTER)
		ttk.Label(self.frame2,text="Username: ")\
											  .place(rely=0.35,relx=0.5,anchor=CENTER)
		self.NEWUSER = StringVar()
		self.newUser = ttk.Entry(self.frame2, textvariable=self.NEWUSER, justify=CENTER)
		self.newUser.place(rely=0.4,relx=0.5,anchor=CENTER)

		ttk.Label(self.frame2,text="Password: ")\
											  .place(rely=0.55,relx=0.5,anchor=CENTER)
		self.NEWPASS = StringVar()
		self.newPass = ttk.Entry(self.frame2, textvariable=self.NEWPASS, justify=CENTER)
		self.newPass.place(rely=0.6,relx=0.5,anchor=CENTER)

		ttk.Button(self.frame2,text="Register",command=self.SaveUser)\
												.place(rely=0.8,relx=0.5,anchor=CENTER)

		ttk.Button(self.frame2,text="Cancel",command=lambda:self.Cancel(self.frame2))\
												.place(rely=0.8,relx=0.85,anchor=CENTER)

		# Screen 1.3 -- LOGIN
		self.frame3 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame3.grid(row=0,column=0)
		self.frame3.grid_propagate(0)

		ttk.Label(self.frame3,text="Please enter your username and password",font=(10),foreground="blue")\
									  .place(rely=0.1,relx=0.5,anchor=CENTER)
		ttk.Label(self.frame3,text="Username: ")\
											  .place(rely=0.35,relx=0.5,anchor=CENTER)
		self.USER = StringVar()
		self.User = ttk.Entry(self.frame3, textvariable=self.USER, justify=CENTER)
		self.User.place(rely=0.4,relx=0.5,anchor=CENTER)

		ttk.Label(self.frame3,text="Password: ")\
											  .place(rely=0.55,relx=0.5,anchor=CENTER)
		self.PASS = StringVar()
		self.Pass = ttk.Entry(self.frame3, textvariable=self.PASS, show='*',justify=CENTER)
		self.Pass.place(rely=0.6,relx=0.5,anchor=CENTER)

		self.v = IntVar()
		ttk.Checkbutton(self.frame3,text="Show",variable=self.v,command=lambda:self.ShowOrHide(self.v.get()))\
		.place(rely=0.6,relx=0.8,anchor=CENTER)
		
		ttk.Button(self.frame3,text="Enter",command=self.VerifyLogin)\
												.place(rely=0.8,relx=0.5,anchor=CENTER)

		ttk.Button(self.frame3,text="Cancel",command=lambda:self.Cancel(self.frame3))\
												.place(rely=0.8,relx=0.85,anchor=CENTER)

		## Screen 2.1 -- PACEMAKER ID
		self.frame4 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame4.grid(row=0,column=0)
		self.frame4.grid_propagate(0)

		ttk.Label(self.frame4,text="Please enter the ID of the Pacemaker you wish to configure")\
										   .place(rely=0.2,relx=0.5,anchor=CENTER)
		ttk.Label(self.frame4,text="Pacemaker ID: ")\
											  .place(rely=0.45,relx=0.5,anchor=CENTER)
		self.ID = StringVar()
		self.id = ttk.Entry(self.frame4, textvariable=self.ID, justify=CENTER)
		self.id.place(rely=0.5,relx=0.5,anchor=CENTER)

		ttk.Button(self.frame4,text="Enter",command=lambda:self.checkID(self.ID.get()))\
												.place(rely=0.8,relx=0.5,anchor=CENTER)

		ttk.Button(self.frame4,text="Cancel",command=lambda:self.Cancel(self.frame4)).place(rely=0.8,relx=0.85,anchor=CENTER)

		## Screen 2.2 -- CHOOSE MODE
		self.frame5 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame5.grid(row=0,column=0)
		self.frame5.grid_propagate(0)

		ttk.Label(self.frame5,text="Please select the pacing mode you wish to edit",font=(11),foreground="blue")\
										   .place(rely=0.1,relx=0.5,anchor=CENTER)

		ttk.Button(self.frame5,text="AOO",command=lambda:self.RaiseFrame(self.frame6))\
											.place(rely=0.3,relx=0.25,anchor=CENTER)
		ttk.Button(self.frame5,text="VOO",command=lambda:self.RaiseFrame(self.frame7))\
											.place(rely=0.3,relx=0.5,anchor=CENTER)
		ttk.Button(self.frame5,text="AAI",command=lambda:self.RaiseFrame(self.frame8))\
											.place(rely=0.7,relx=0.25,anchor=CENTER)
		ttk.Button(self.frame5,text="VVI",command=lambda:self.RaiseFrame(self.frame9))\
											.place(rely=0.7,relx=0.5,anchor=CENTER)
		ttk.Button(self.frame5,text="DOO",command=lambda:self.RaiseFrame(self.frame10))\
											.place(rely=0.3,relx=0.75,anchor=CENTER)
		ttk.Button(self.frame5,text="AOOR",command=lambda:self.RaiseFrame(self.frame11))\
											.place(rely=0.5,relx=0.25,anchor=CENTER)
		ttk.Button(self.frame5,text="VOOR",command=lambda:self.RaiseFrame(self.frame12))\
											.place(rely=0.5,relx=0.5,anchor=CENTER)
		ttk.Button(self.frame5,text="AAIR",command=lambda:self.RaiseFrame(self.frame13))\
											.place(rely=0.9,relx=0.25,anchor=CENTER)
		ttk.Button(self.frame5,text="VVIR",command=lambda:self.RaiseFrame(self.frame14))\
											.place(rely=0.9,relx=0.5,anchor=CENTER)
		ttk.Button(self.frame5,text="DOOR",command=lambda:self.RaiseFrame(self.frame15))\
											.place(rely=0.5,relx=0.75,anchor=CENTER)
		
		Button(self.frame5,text="Save and Exit",command=self.LeaveEdit,bg="red").place(rely=0.9,relx=0.75,anchor=CENTER)

		## Screen 2.3 -- EDIT AOO
		self.frame6 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame6.grid(row=0,column=0)
		self.frame6.grid_propagate(0)

		ttk.Label(self.frame6,text="Edit AOO Mode").place(rely=0.1,relx=0.5,anchor=CENTER)
		
        		# Lower Limit
		self.ALRL = StringVar()
		self.aLowRate = Entry(self.frame6, textvariable=self.ALRL)
		self.aLowRate.place(rely=0.2,relx=0.4,anchor=W)
		self.ALRL.set(str(self.modes[0].params["Lower Rate Limit"]))
		ttk.Label(self.frame6,text="Lower Rate Limit(ppm): ").place(rely=0.2,relx=0.4,anchor=E)

				# Upper Limit
		self.AURL = StringVar()
		self.aUpRate = Entry(self.frame6, textvariable=self.AURL)
		self.aUpRate.place(rely=0.4,relx=0.4,anchor=W)
		self.AURL.set(str(self.modes[0].params["Upper Rate Limit"]))
		ttk.Label(self.frame6,text="Upper Rate Limit(ppm): ").place(rely=0.4,relx=0.4,anchor=E)

				# Amplitude
		self.AA = StringVar()
		self.aAmp = Entry(self.frame6, textvariable=self.AA)
		self.aAmp.place(rely=0.6,relx=0.4,anchor=W)
		self.AA.set(str(self.modes[0].params["Atrial Amp"]))
		ttk.Label(self.frame6,text="Atrial Amplitude(V): ").place(rely=0.6,relx=0.4,anchor=E)

				#Pulse Width
		self.APW = StringVar()
		self.apWidth = Entry(self.frame6, textvariable=self.APW)
		self.apWidth.place(rely=0.8,relx=0.4,anchor=W)
		self.APW.set(str(self.modes[0].params["Atrial Pulse Width"]))
		ttk.Label(self.frame6,text="Atrial Pulse Width(ms): ").place(rely=0.8,relx=0.4,anchor=E)

		ttk.Button(self.frame6,text="Set Values",command=lambda:self.VerifySet([self.aLowRate.get(),self.aUpRate.get(),self.aAmp.get(),self.apWidth.get()],0))\
                                                 .place(rely=0.9,relx=0.55,anchor=CENTER)
		ttk.Button(self.frame6,text="Back",command=lambda:self.Cancel(self.frame6)).place(rely=0.9,relx=0.25,anchor=CENTER)

		Button(self.frame6,text="    Send    ",command=lambda:self.Send("AOO",self.modes[0].params),bg="green").place(rely=0.9,relx=.85,anchor=CENTER)
		
		## Screen 2.4 -- EDIT VOO
		self.frame7 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame7.grid(row=0,column=0)
		self.frame7.grid_propagate(0)

		ttk.Label(self.frame7,text="Edit VOO Mode").place(rely=0.1,relx=0.5,anchor=CENTER)

        		# Lower Limit
		self.VLRL = StringVar()
		self.vLowRate = Entry(self.frame7, textvariable=self.VLRL)
		self.vLowRate.place(rely=0.2,relx=0.4,anchor=W)
		self.VLRL.set(str(self.modes[1].params["Lower Rate Limit"]))
		ttk.Label(self.frame7,text="Lower Rate Limit(ppm): ").place(rely=0.2,relx=0.4,anchor=E)

				# Upper Limit
		self.VURL = StringVar()
		self.vUpRate = Entry(self.frame7, textvariable=self.VURL)
		self.vUpRate.place(rely=0.4,relx=0.4,anchor=W)
		self.VURL.set(str(self.modes[1].params["Upper Rate Limit"]))
		ttk.Label(self.frame7,text="Upper Rate Limit(ppm): ").place(rely=0.4,relx=0.4,anchor=E)

				# Amplitude
		self.VA = StringVar()
		self.vAmp = Entry(self.frame7, textvariable=self.VA)
		self.vAmp.place(rely=0.6,relx=0.4,anchor=W)
		self.VA.set(str(self.modes[1].params["Ventricular Amp"]))
		ttk.Label(self.frame7,text="Ventricular Amplitude(V): ").place(rely=0.6,relx=0.4,anchor=E)

				# Pulse Width
		self.VPW = StringVar()
		self.vpWidth = Entry(self.frame7, textvariable=self.VPW)
		self.vpWidth.place(rely=0.8,relx=0.4,anchor=W)
		self.VPW.set(str(self.modes[1].params["Ventricular Pulse Width"]))
		ttk.Label(self.frame7,text="Ventricular Pulse Width(ms): ").place(rely=0.8,relx=0.4,anchor=E)

		ttk.Button(self.frame7,text="Set Values",command=lambda:self.VerifySet([self.vLowRate.get(),self.vUpRate.get(),self.vAmp.get(),self.vpWidth.get()],1))\
                                                 .place(rely=0.9,relx=0.55,anchor=CENTER)
		ttk.Button(self.frame7,text="Back",command=lambda:self.Cancel(self.frame7)).place(rely=0.9,relx=0.25,anchor=CENTER)

		Button(self.frame7,text="    Send    ",command=lambda:self.Send("VOO",self.modes[1].params),bg="green").place(rely=0.9,relx=.85,anchor=CENTER)
		
		## Screen 2.5 -- EDIT AAI
		self.frame8 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame8.grid(row=0,column=0)
		self.frame8.grid_propagate(0)

		ttk.Label(self.frame8,text="Edit AAI Mode").place(rely=0.1,relx=0.5,anchor=CENTER)

        		# Lower Limit
		self.ALRL2 = StringVar()
		self.aLowRate2 = Entry(self.frame8, textvariable=self.ALRL2)
		self.aLowRate2.place(rely=0.26,relx=0.4,anchor=W)
		self.ALRL2.set(str(self.modes[2].params["Lower Rate Limit"]))
		ttk.Label(self.frame8,text="Lower Rate Limit(ppm): ").place(rely=0.26,relx=0.4,anchor=E)

				# Upper Limit
		self.AURL2 = StringVar()
		self.aUpRate2 = Entry(self.frame8, textvariable=self.AURL2)
		self.aUpRate2.place(rely=0.42,relx=0.4,anchor=W)
		self.AURL2.set(str(self.modes[2].params["Upper Rate Limit"]))
		ttk.Label(self.frame8,text="Upper Rate Limit(ppm): ").place(rely=0.42,relx=0.4,anchor=E)

				# Amplitude
		self.AA2 = StringVar()
		self.aAmp2 = Entry(self.frame8, textvariable=self.AA2)
		self.aAmp2.place(rely=0.58,relx=0.4,anchor=W)
		self.AA2.set(str(self.modes[2].params["Atrial Amp"]))
		ttk.Label(self.frame8,text="Atrial Amplitude(V): ").place(rely=0.58,relx=0.4,anchor=E)

				# Pulse Width
		self.APW2 = StringVar()
		self.apWidth2 = Entry(self.frame8, textvariable=self.APW2)
		self.apWidth2.place(rely=0.74,relx=0.4,anchor=W)
		self.APW2.set(str(self.modes[2].params["Atrial Pulse Width"]))
		ttk.Label(self.frame8,text="Atrial Pulse Width(ms): ").place(rely=0.74,relx=0.4,anchor=E)

                # Sensitivity
		'''
		self.ASENS = StringVar()
		self.aSens = Entry(self.frame8, textvariable=self.ASENS)
		self.aSens.place(rely=0.5,relx=0.4,anchor=W)
		self.ASENS.set(str(self.modes[2].params["Atrial Sensitivity"]))
		ttk.Label(self.frame8, text="Atrial Sensitivity(mV): ").place(rely=0.5,relx=0.4,anchor=E)
		'''
		
                # ARP
		self.AREF = StringVar()
		self.aRef = Entry(self.frame8, textvariable=self.AREF)
		self.aRef.place(rely=0.9,relx=0.4,anchor=W)
		self.AREF.set(str(self.modes[2].params["ARP"]))
		ttk.Label(self.frame8, text="Atrial Refactory Period(ms): ").place(rely=0.9,relx=0.4,anchor=E)

                # PVARP
		'''
		self.APVARP = StringVar()
		self.aPvarp = Entry(self.frame8, textvariable=self.APVARP)
		self.aPvarp.place(rely=0.7,relx=0.4,anchor=W)
		self.APVARP.set(str(self.modes[2].params["PVARP"]))
		ttk.Label(self.frame8, text="PVARP(ms): ").place(rely=0.7,relx=0.4,anchor=E)

		
                # Hysteresis
		self.AHYS = StringVar()
		self.ahys = Entry(self.frame8, textvariable=self.AHYS)
		self.ahys.place(rely=0.8,relx=0.4,anchor=W)
		self.AHYS.set(str(self.modes[2].params["Hysteresis"]))
		ttk.Label(self.frame8, text="Hysteresis(ppm): ").place(rely=0.8,relx=0.4,anchor=E)
		
                # Rate Smoothing
		self.ARSMOOTH = StringVar()
		self.aRsmooth = Entry(self.frame8, textvariable=self.ARSMOOTH)
		self.aRsmooth.place(rely=0.9,relx=0.4,anchor=W)
		self.ARSMOOTH.set(str(self.modes[2].params["Rate Smoothing"]))
		ttk.Label(self.frame8, text="Rate Smoothing(%): ").place(rely=0.9,relx=0.4,anchor=E)
		'''

		ttk.Button(self.frame8,text="Set Values",command=lambda:self.VerifySet([self.aLowRate2.get(),self.aUpRate2.get(),\
                         self.aAmp2.get(),self.apWidth2.get(),self.aRef.get()],2))\
                                                 .place(rely=0.3,relx=0.875,anchor=CENTER)
		ttk.Button(self.frame8,text="Back",command=lambda:self.Cancel(self.frame8)).place(rely=0.7,relx=0.875,anchor=CENTER)

		Button(self.frame8,text="    Send    ",command=lambda:self.Send("AAI",self.modes[2].params),bg="green").place(rely=0.5,relx=.875,anchor=CENTER)
		
		## Screen 2.6 -- EDIT VVI
		self.frame9 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame9.grid(row=0,column=0)
		self.frame9.grid_propagate(0)

		ttk.Label(self.frame9,text="Edit VVI Mode").place(rely=0.1,relx=0.5,anchor=CENTER)
		
                # Lower Limit
		self.VLRL2 = StringVar()
		self.vLowRate2 = Entry(self.frame9, textvariable=self.VLRL2)
		self.vLowRate2.place(rely=0.26,relx=0.47,anchor=W)
		self.VLRL2.set(str(self.modes[3].params["Upper Rate Limit"]))
		ttk.Label(self.frame9,text="Lower Rate Limit(ppm): ").place(rely=0.26,relx=0.47,anchor=E)

				# Upper Limit
		self.VURL2 = StringVar()
		self.vUpRate2 = Entry(self.frame9, textvariable=self.VURL2)
		self.vUpRate2.place(rely=0.42,relx=0.47,anchor=W)
		self.VURL2.set(str(self.modes[3].params["Lower Rate Limit"]))
		ttk.Label(self.frame9,text="Upper Rate Limit(ppm): ").place(rely=0.42,relx=0.47,anchor=E)

				# Amplitude
		self.VA2 = StringVar()
		self.vAmp2 = Entry(self.frame9, textvariable=self.VA2)
		self.vAmp2.place(rely=0.58,relx=0.47,anchor=W)
		self.VA2.set(str(self.modes[3].params["Ventricular Amp"]))
		ttk.Label(self.frame9,text="Ventricular Amplitude(V): ").place(rely=0.58,relx=0.47,anchor=E)

				# Pulse Width
		self.VPW2 = StringVar()
		self.vpWidth2 = Entry(self.frame9, textvariable=self.VPW2)
		self.vpWidth2.place(rely=0.74,relx=0.47,anchor=W)
		self.VPW2.set(str(self.modes[3].params["Ventricular Pulse Width"]))
		ttk.Label(self.frame9,text="Ventricular Pulse Width(ms): ").place(rely=0.74,relx=0.47,anchor=E)

				# Sensitivity
		'''
		self.VSENS = StringVar()
		self.vSens = Entry(self.frame9, textvariable=self.VSENS)
		self.vSens.place(rely=0.5625,relx=0.47,anchor=W)
		self.VSENS.set(str(self.modes[3].params["Ventricular Sensitivity"]))
		ttk.Label(self.frame9, text="Ventricular Sensitivity(mV): ").place(rely=0.5625,relx=0.47,anchor=E)
		'''

                # VRP
		self.VREF = StringVar()
		self.vRef = Entry(self.frame9, textvariable=self.VREF)
		self.vRef.place(rely=0.9,relx=0.47,anchor=W)
		self.VREF.set(str(self.modes[3].params["VRP"]))
		ttk.Label(self.frame9, text="Ventricular Refactory Period(ms): ").place(rely=0.9,relx=0.47,anchor=E)

                # Hysteresis
		'''
		self.VHYS = StringVar()
		self.vHys = Entry(self.frame9, textvariable=self.VHYS)
		self.vHys.place(rely=0.7875,relx=0.47,anchor=W)
		self.VHYS.set(str(self.modes[3].params["Hysteresis"]))
		ttk.Label(self.frame9, text="Hysteresis(ppm): ").place(rely=0.7875,relx=0.47,anchor=E)

                # Rate Smoothing
		self.VRSMOOTH = StringVar()
		self.vRsmooth = Entry(self.frame9, textvariable=self.VRSMOOTH)
		self.vRsmooth.place(rely=0.9,relx=0.47,anchor=W)
		self.VRSMOOTH.set(str(self.modes[3].params["Rate Smoothing"]))
		ttk.Label(self.frame9, text="Rate Smoothing(%): ").place(rely=0.9,relx=0.47,anchor=E)
		'''

		ttk.Button(self.frame9,text="Set Values",command=lambda:self.VerifySet([self.vLowRate2.get(),self.vUpRate2.get(),self.vAmp2.get(),\
                         self.vpWidth2.get(),self.vRef.get()],3))\
                         .place(rely=0.3,relx=0.9,anchor=CENTER)
		ttk.Button(self.frame9,text="Back",command=lambda:self.Cancel(self.frame9)).place(rely=0.7,relx=0.9,anchor=CENTER)

		Button(self.frame9,text="    Send    ",command=lambda:self.Send("VVI",self.modes[3].params),bg="green").place(rely=0.5,relx=.9,anchor=CENTER)



		## Screen 2.7 -- EDIT DOO
		self.frame10 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame10.grid(row=0,column=0)
		self.frame10.grid_propagate(0)

		ttk.Label(self.frame10,text="Edit DOO Mode").place(rely=0.05,relx=0.5,anchor=CENTER)

                # Lower Limit
		self.LRL = StringVar()
		self.LowRate = Entry(self.frame10, textvariable=self.LRL)
		self.LowRate.place(rely=0.125,relx=0.4,anchor=W)
		self.LRL.set(str(self.modes[4].params["Lower Rate Limit"]))
		ttk.Label(self.frame10,text="Lower Rate Limit(ppm): ").place(rely=0.125,relx=0.4,anchor=E)

				# Upper Limit
		self.URL = StringVar()
		self.UpRate = Entry(self.frame10, textvariable=self.URL)
		self.UpRate.place(rely=0.25,relx=0.4,anchor=W)
		self.URL.set(str(self.modes[4].params["Upper Rate Limit"]))
		ttk.Label(self.frame10,text="Upper Rate Limit(ppm): ").place(rely=0.25,relx=0.4,anchor=E)

                # Fixed AV Delay
		self.AVDELAY = StringVar()
		self.avDelay = Entry(self.frame10, textvariable=self.AVDELAY)
		self.avDelay.place(rely=0.375,relx=0.4,anchor=W)
		self.AVDELAY.set(str(self.modes[4].params["Fixed AV Delay"]))
		ttk.Label(self.frame10, text="Fixed AV Delay(ms): ").place(rely=0.375,relx=0.4,anchor=E)

                # Atrial Amplitude
		self.AA3 = StringVar()
		self.aAmp3 = Entry(self.frame10, textvariable=self.AA3)
		self.aAmp3.place(rely=0.5,relx=0.4,anchor=W)
		self.AA3.set(str(self.modes[4].params["Atrial Amp"]))
		ttk.Label(self.frame10, text="Atrial Amplitude(V): ").place(rely=0.5,relx=0.4,anchor=E)

				# Ventricular Amplitude
		self.VA3 = StringVar()
		self.vAmp3 = Entry(self.frame10, textvariable=self.VA3)
		self.vAmp3.place(rely=0.625,relx=0.4,anchor=W)
		self.VA3.set(str(self.modes[4].params["Ventricular Amp"]))
		ttk.Label(self.frame10,text="Ventricular Amplitude(V): ").place(rely=0.625,relx=0.4,anchor=E)

                # Atrial Pulse Width
		self.APW3 = StringVar()
		self.apWidth3 = Entry(self.frame10, textvariable=self.APW3)
		self.apWidth3.place(rely=0.75,relx=0.4,anchor=W)
		self.APW3.set(str(self.modes[4].params["Atrial Pulse Width"]))
		ttk.Label(self.frame10, text="Atrial Pulse Width(ms): ").place(rely=0.75,relx=0.4,anchor=E)

				# Ventricular Pulse Width
		self.VPW3 = StringVar()
		self.vpWidth3 = Entry(self.frame10, textvariable=self.VPW3)
		self.vpWidth3.place(rely=0.875,relx=0.4,anchor=W)
		self.VPW3.set(str(self.modes[4].params["Ventricular Pulse Width"]))
		ttk.Label(self.frame10,text="Ventricular Pulse Width(ms): ").place(rely=0.875,relx=0.4,anchor=E)

                
		ttk.Button(self.frame10,text="Set Values",command=lambda:self.VerifySet([self.LowRate.get(),self.UpRate.get(),self.avDelay.get(),\
                         self.aAmp3.get(),self.vAmp3.get(),self.apWidth3.get(),self.vpWidth3.get()],4))\
                         .place(rely=0.3,relx=0.9,anchor=CENTER)
		ttk.Button(self.frame10,text="Back",command=lambda:self.Cancel(self.frame10)).place(rely=0.7,relx=0.9,anchor=CENTER)

		Button(self.frame10,text="    Send    ",command=lambda:self.Send("DOO",self.modes[4].params),bg="green").place(rely=0.5,relx=.9,anchor=CENTER)


		## Screen 2.8 -- EDIT AOOR
		self.frame11 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame11.grid(row=0,column=0)
		self.frame11.grid_propagate(0)

		ttk.Label(self.frame11,text="Edit AOOR Mode").place(rely=0.05,relx=0.5,anchor=CENTER)

                # Lower Limit
		self.ALRL3 = StringVar()
		self.aLowRate3 = Entry(self.frame11, textvariable=self.ALRL3)
		self.aLowRate3.place(rely=0.1,relx=0.4,anchor=W)
		self.ALRL3.set(str(self.modes[5].params["Lower Rate Limit"]))
		ttk.Label(self.frame11,text="Lower Rate Limit(ppm): ").place(rely=0.1,relx=0.4,anchor=E)

				# Upper Limit
		self.AURL3 = StringVar()
		self.aUpRate3 = Entry(self.frame11, textvariable=self.AURL3)
		self.aUpRate3.place(rely=0.2,relx=0.4,anchor=W)
		self.AURL3.set(str(self.modes[5].params["Upper Rate Limit"]))
		ttk.Label(self.frame11,text="Upper Rate Limit(ppm): ").place(rely=0.2,relx=0.4,anchor=E)

                # Max Sensor Rate
		self.AMAXSENS = StringVar()
		self.aMaxsens = Entry(self.frame11, textvariable=self.AMAXSENS)
		self.aMaxsens.place(rely=0.3,relx=0.4,anchor=W)
		self.AMAXSENS.set(str(self.modes[5].params["Max Sensor Rate"]))
		ttk.Label(self.frame11,text="Max Sensor Rate(ppm): ").place(rely=0.3,relx=0.4,anchor=E)

				# Amplitude
		self.AA4 = StringVar()
		self.aAmp4= Entry(self.frame11, textvariable=self.AA4)
		self.aAmp4.place(rely=0.4,relx=0.4,anchor=W)
		self.AA4.set(str(self.modes[5].params["Atrial Amp"]))
		ttk.Label(self.frame11,text="Atrial Amplitude(V): ").place(rely=0.4,relx=0.4,anchor=E)

				# Pulse Width
		self.APW4 = StringVar()
		self.apWidth4 = Entry(self.frame11, textvariable=self.APW4)
		self.apWidth4.place(rely=0.5,relx=0.4,anchor=W)
		self.APW4.set(str(self.modes[5].params["Atrial Pulse Width"]))
		ttk.Label(self.frame11,text="Atrial Pulse Width(ms): ").place(rely=0.5,relx=0.4,anchor=E)

                # Activity Threshold
		self.AACTTHRESH = StringVar()
		self.aActthresh = Entry(self.frame11, textvariable=self.AACTTHRESH)
		self.aActthresh.place(rely=0.6,relx=0.4,anchor=W)
		self.AACTTHRESH.set(str(self.modes[5].params["Activity Threshold"]))
		ttk.Label(self.frame11,text="Activity Threshold(1-7): ").place(rely=0.6,relx=0.4,anchor=E)

                # Reaction Time
		self.AREACTTIME = StringVar()
		self.aReacttime = Entry(self.frame11, textvariable=self.AREACTTIME)
		self.aReacttime.place(rely=0.7,relx=0.4,anchor=W)
		self.AREACTTIME.set(str(self.modes[5].params["Reaction Time"]))
		ttk.Label(self.frame11,text="Reaction Time(s): ").place(rely=0.7,relx=0.4,anchor=E)

                # Response Factor
		self.ARESPFACT = StringVar()
		self.aRespfact = Entry(self.frame11, textvariable=self.ARESPFACT)
		self.aRespfact.place(rely=0.8,relx=0.4,anchor=W)
		self.ARESPFACT.set(str(self.modes[5].params["Response Factor"]))
		ttk.Label(self.frame11,text="Response Factor(1-16): ").place(rely=0.8,relx=0.4,anchor=E)

                # Recovery Time
		self.ARECOVTIME = StringVar()
		self.aRecovtime = Entry(self.frame11, textvariable=self.ARECOVTIME)
		self.aRecovtime.place(rely=0.9,relx=0.4,anchor=W)
		self.ARECOVTIME.set(str(self.modes[5].params["Recovery Time"]))
		ttk.Label(self.frame11,text="Recovery Time(min): ").place(rely=0.9,relx=0.4,anchor=E)

		ttk.Button(self.frame11,text="Set Values",command=lambda:self.VerifySet([self.aLowRate3.get(),self.aUpRate3.get(),self.aMaxsens.get(),\
                                self.aAmp4.get(),self.apWidth4.get(),self.aActthresh.get(),self.aReacttime.get(),self.aRespfact.get(),self.aRecovtime.get()],5))\
                                .place(rely=0.3,relx=0.875,anchor=CENTER)
		ttk.Button(self.frame11,text="Back",command=lambda:self.Cancel(self.frame11)).place(rely=0.7,relx=0.875,anchor=CENTER)

		Button(self.frame11,text="    Send    ",command=lambda:self.Send("AOOR",self.modes[5].params),bg="green").place(rely=0.5,relx=.875,anchor=CENTER)



		## Screen 2.9 -- EDIT VOOR
		self.frame12 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame12.grid(row=0,column=0)
		self.frame12.grid_propagate(0)

		ttk.Label(self.frame12,text="Edit VOOR Mode").place(rely=0.05,relx=0.5,anchor=CENTER)

                # Lower Limit
		self.VLRL3 = StringVar()
		self.vLowRate3 = Entry(self.frame12, textvariable=self.VLRL3)
		self.vLowRate3.place(rely=0.1,relx=0.4,anchor=W)
		self.VLRL3.set(str(self.modes[6].params["Lower Rate Limit"]))
		ttk.Label(self.frame12,text="Lower Rate Limit(ppm): ").place(rely=0.1,relx=0.4,anchor=E)

				# Upper Limit
		self.VURL3 = StringVar()
		self.vUpRate3 = Entry(self.frame12, textvariable=self.VURL3)
		self.vUpRate3.place(rely=0.2,relx=0.4,anchor=W)
		self.VURL3.set(str(self.modes[6].params["Upper Rate Limit"]))
		ttk.Label(self.frame12,text="Upper Rate Limit(ppm): ").place(rely=0.2,relx=0.4,anchor=E)

				# Sensitivity
		self.VMAXSENS = StringVar()
		self.vMaxsens = Entry(self.frame12, textvariable=self.VMAXSENS)
		self.vMaxsens.place(rely=0.3,relx=0.4,anchor=W)
		self.VMAXSENS.set(str(self.modes[6].params["Max Sensor Rate"]))
		ttk.Label(self.frame12,text="Max Sensor Rate(ppm): ").place(rely=0.3,relx=0.4,anchor=E)

				# Amplitude
		self.VA4 = StringVar()
		self.vAmp4= Entry(self.frame12, textvariable=self.VA4)
		self.vAmp4.place(rely=0.4,relx=0.4,anchor=W)
		self.VA4.set(str(self.modes[6].params["Ventricular Amp"]))
		ttk.Label(self.frame12,text="Ventricular Amplitude(V): ").place(rely=0.4,relx=0.4,anchor=E)

				# Pulse Width
		self.VPW4 = StringVar()
		self.vpWidth4 = Entry(self.frame12, textvariable=self.VPW4)
		self.vpWidth4.place(rely=0.5,relx=0.4,anchor=W)
		self.VPW4.set(str(self.modes[6].params["Ventricular Pulse Width"]))
		ttk.Label(self.frame12,text="Ventricular Pulse Width(ms): ").place(rely=0.5,relx=0.4,anchor=E)

                # Activity Threshold
		self.VACTTHRESH = StringVar()
		self.vActthresh = Entry(self.frame12, textvariable=self.VACTTHRESH)
		self.vActthresh.place(rely=0.6,relx=0.4,anchor=W)
		self.VACTTHRESH.set(str(self.modes[6].params["Activity Threshold"]))
		ttk.Label(self.frame12,text="Activity Threshold(1-7): ").place(rely=0.6,relx=0.4,anchor=E)

                # Reaction Time
		self.VREACTTIME = StringVar()
		self.vReacttime = Entry(self.frame12, textvariable=self.VREACTTIME)
		self.vReacttime.place(rely=0.7,relx=0.4,anchor=W)
		self.VREACTTIME.set(str(self.modes[6].params["Reaction Time"]))
		ttk.Label(self.frame12,text="Reaction Time(s): ").place(rely=0.7,relx=0.4,anchor=E)

                # Response Factor
		self.VRESPFACT = StringVar()
		self.vRespfact = Entry(self.frame12, textvariable=self.VRESPFACT)
		self.vRespfact.place(rely=0.8,relx=0.4,anchor=W)
		self.VRESPFACT.set(str(self.modes[6].params["Response Factor"]))
		ttk.Label(self.frame12,text="Response Factor(1-16): ").place(rely=0.8,relx=0.4,anchor=E)

                # Recovery Time
		self.VRECOVTIME = StringVar()
		self.vRecovtime = Entry(self.frame12, textvariable=self.VRECOVTIME)
		self.vRecovtime.place(rely=0.9,relx=0.4,anchor=W)
		self.VRECOVTIME.set(str(self.modes[6].params["Recovery Time"]))
		ttk.Label(self.frame12,text="Recovery Time(min): ").place(rely=0.9,relx=0.4,anchor=E)

		ttk.Button(self.frame12,text="Set Values",command=lambda:self.VerifySet([self.vLowRate3.get(),self.vUpRate3.get(),self.vMaxsens.get(),\
                                self.vAmp4.get(),self.vpWidth4.get(),self.vActthresh.get(),self.vReacttime.get(),self.vRespfact.get(),self.vRecovtime.get()],6))\
                                .place(rely=0.3,relx=0.875,anchor=CENTER)
		ttk.Button(self.frame12,text="Back",command=lambda:self.Cancel(self.frame12)).place(rely=0.7,relx=0.875,anchor=CENTER)

		Button(self.frame12,text="    Send    ",command=lambda:self.Send("VOOR",self.modes[6].params),bg="green").place(rely=0.5,relx=.875,anchor=CENTER)


		## Screen 2.10 -- EDIT AAIR
		self.frame13 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame13.grid(row=0,column=0)
		self.frame13.grid_propagate(0)

		ttk.Label(self.frame13,text="Edit AAIR Mode").place(rely=0.05,relx=0.5,anchor=CENTER)

                # Lower Limit
		self.ALRL5 = StringVar()
		self.aLowRate5 = Entry(self.frame13, textvariable=self.ALRL5)
		self.aLowRate5.place(rely=0.14,relx=0.4,anchor=W)
		self.ALRL5.set(str(self.modes[7].params["Lower Rate Limit"]))
		ttk.Label(self.frame13,text="Lower Rate Limit(ppm): ").place(rely=0.14,relx=0.4,anchor=E)

				# Upper Limit
		self.AURL5 = StringVar()
		self.aUpRate5 = Entry(self.frame13, textvariable=self.AURL5)
		self.aUpRate5.place(rely=0.23,relx=0.4,anchor=W)
		self.AURL5.set(str(self.modes[7].params["Upper Rate Limit"]))
		ttk.Label(self.frame13,text="Upper Rate Limit(ppm): ").place(rely=0.23,relx=0.4,anchor=E)

                # Max Sensor Rate
		self.AMAXSENS5 = StringVar()  
		self.aMaxsens5 = Entry(self.frame13, textvariable=self.AMAXSENS5)
		self.aMaxsens5.place(rely=0.32,relx=0.4,anchor=W)
		self.AMAXSENS5.set(str(self.modes[7].params["Max Sensor Rate"]))
		ttk.Label(self.frame13,text="Max Sensor Rate(ppm): ").place(rely=0.32,relx=0.4,anchor=E)

				# Amplitude
		self.AA5 = StringVar()
		self.aAmp5 = Entry(self.frame13, textvariable=self.AA5)
		self.aAmp5.place(rely=0.41,relx=0.4,anchor=W)
		self.AA5.set(str(self.modes[7].params["Atrial Amp"]))
		ttk.Label(self.frame13,text="Atrial Amplitude(V): ").place(rely=0.41,relx=0.4,anchor=E)

				# Pulse Width
		self.APW5 = StringVar()
		self.apWidth5 = Entry(self.frame13, textvariable=self.APW5)
		self.apWidth5.place(rely=0.5,relx=0.4,anchor=W)
		self.APW5.set(str(self.modes[7].params["Atrial Pulse Width"]))
		ttk.Label(self.frame13,text="Atrial Pulse Width(ms): ").place(rely=0.5,relx=0.4,anchor=E)

		
		'''
		self.ASENS5 = StringVar()
		self.aSens5 = Entry(self.frame13, textvariable=self.ASENS5)
		self.aSens5.place(rely=0.42,relx=0.4,anchor=W)
		self.ASENS5.set(str(self.modes[7].params["Atrial Sensitivity"]))
		ttk.Label(self.frame13, text="Atrial Sensitivity(mV): ").place(rely=0.42,relx=0.4,anchor=E)
		'''
		
                # ARP
		self.AREF5 = StringVar()
		self.aRef5 = Entry(self.frame13, textvariable=self.AREF5)
		self.aRef5.place(rely=0.59,relx=0.4,anchor=W)
		self.AREF5.set(str(self.modes[7].params["ARP"]))
		ttk.Label(self.frame13, text="ARP(ms): ").place(rely=0.59,relx=0.4,anchor=E)

		'''
		self.APVARP5 = StringVar()
		self.aPvarp5 = Entry(self.frame13, textvariable=self.APVARP5)
		self.aPvarp5.place(rely=0.56,relx=0.4,anchor=W)
		self.APVARP5.set(str(self.modes[7].params["PVARP"]))
		ttk.Label(self.frame13, text="PVARP(ms): ").place(rely=0.56,relx=0.4,anchor=E)

                # Hysteresis
		self.AHYS5 = StringVar()
		self.ahys5 = Entry(self.frame13, textvariable=self.AHYS5)
		self.ahys5.place(rely=0.63,relx=0.4,anchor=W)
		self.AHYS5.set(str(self.modes[7].params["Hysteresis"]))
		ttk.Label(self.frame13, text="Hysteresis(ppm): ").place(rely=0.63,relx=0.4,anchor=E)

                # Rate Smoothing
		self.ARSMOOTH5 = StringVar()
		self.aRsmooth5 = Entry(self.frame13, textvariable=self.ARSMOOTH5)
		self.aRsmooth5.place(rely=0.7,relx=0.4,anchor=W)
		self.ARSMOOTH5.set(str(self.modes[7].params["Rate Smoothing"]))
		ttk.Label(self.frame13, text="Rate Smoothing(%): ").place(rely=0.7,relx=0.4,anchor=E)
		'''

                # Activity Threshold
		self.AACTTHRESH5 = StringVar()
		self.aActthresh5 = Entry(self.frame13, textvariable=self.AACTTHRESH5)
		self.aActthresh5.place(rely=0.68,relx=0.4,anchor=W)
		self.AACTTHRESH5.set(str(self.modes[7].params["Activity Threshold"]))
		ttk.Label(self.frame13,text="Activity Threshold(1-7): ").place(rely=0.68,relx=0.4,anchor=E)

                # Reaction Time
		self.AREACTTIME5 = StringVar()
		self.aReacttime5 = Entry(self.frame13, textvariable=self.AREACTTIME5)
		self.aReacttime5.place(rely=0.77,relx=0.4,anchor=W)
		self.AREACTTIME5.set(str(self.modes[7].params["Reaction Time"]))
		ttk.Label(self.frame13,text="Reaction Time(s): ").place(rely=0.77,relx=0.4,anchor=E)

                # Response Factor
		self.ARESPFACT5 = StringVar()
		self.aRespfact5 = Entry(self.frame13, textvariable=self.ARESPFACT5)
		self.aRespfact5.place(rely=0.86,relx=0.4,anchor=W)
		self.ARESPFACT5.set(str(self.modes[7].params["Response Factor"]))
		ttk.Label(self.frame13,text="Response Factor(1-16): ").place(rely=0.86,relx=0.4,anchor=E)

                # Recovery Time
		self.ARECOVTIME5 = StringVar()
		self.aRecovtime5 = Entry(self.frame13, textvariable=self.ARECOVTIME5)
		self.aRecovtime5.place(rely=0.95,relx=0.4,anchor=W)
		self.ARECOVTIME5.set(str(self.modes[7].params["Recovery Time"]))
		ttk.Label(self.frame13,text="Recovery Time(min): ").place(rely=0.95,relx=0.4,anchor=E)


		ttk.Button(self.frame13,text="Set Values",command=lambda:self.VerifySet([self.aLowRate5.get(),self.aUpRate5.get(),self.aMaxsens5.get(),\
                                self.aAmp5.get(),self.apWidth5.get(),self.aRef5.get(),\
                                self.aActthresh5.get(),self.aReacttime5.get(),self.aRespfact5.get(),self.aRecovtime5.get()],7))\
                                .place(rely=0.3,relx=0.875,anchor=CENTER)
		ttk.Button(self.frame13,text="Back",command=lambda:self.Cancel(self.frame13)).place(rely=0.7,relx=0.875,anchor=CENTER)

		Button(self.frame13,text="    Send    ",command=lambda:self.Send("AAIR",self.modes[7].params),bg="green").place(rely=0.5,relx=.875,anchor=CENTER)


		## Screen 2.11 -- EDIT VVIR
		self.frame14 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame14.grid(row=0,column=0)
		self.frame14.grid_propagate(0)

		ttk.Label(self.frame14,text="Edit VVIR Mode").place(rely=0.05,relx=0.5,anchor=CENTER)

                # Lower Limit
		self.VLRL5 = StringVar()
		self.vLowRate5 = Entry(self.frame14, textvariable=self.VLRL5)
		self.vLowRate5.place(rely=0.14,relx=0.4,anchor=W)
		self.VLRL5.set(str(self.modes[8].params["Lower Rate Limit"]))
		ttk.Label(self.frame14,text="Lower Rate Limit(ppm): ").place(rely=0.14,relx=0.4,anchor=E)

				# Upper Limit
		self.VURL5 = StringVar()
		self.vUpRate5 = Entry(self.frame14, textvariable=self.VURL5)
		self.vUpRate5.place(rely=0.23,relx=0.4,anchor=W)
		self.VURL5.set(str(self.modes[8].params["Upper Rate Limit"]))
		ttk.Label(self.frame14,text="Upper Rate Limit(ppm): ").place(rely=0.23,relx=0.4,anchor=E)

				# Max Sensor Rate
		self.VMAXSENS5 = StringVar()
		self.vMaxsens5 = Entry(self.frame14, textvariable=self.VMAXSENS5)
		self.vMaxsens5.place(rely=0.32,relx=0.4,anchor=W)
		self.VMAXSENS5.set(str(self.modes[8].params["Max Sensor Rate"]))
		ttk.Label(self.frame14,text="Max Sensor Rate(ppm): ").place(rely=0.32,relx=0.4,anchor=E)

				# Amplitude
		self.VA5 = StringVar()
		self.vAmp5 = Entry(self.frame14, textvariable=self.VA5)
		self.vAmp5.place(rely=0.41,relx=0.4,anchor=W)
		self.VA5.set(str(self.modes[8].params["Ventricular Amp"]))
		ttk.Label(self.frame14,text="Ventricular Amplitude(V): ").place(rely=0.41,relx=0.4,anchor=E)

				# Pulse Width
		self.VPW5 = StringVar()
		self.vpWidth5 = Entry(self.frame14, textvariable=self.VPW5)
		self.vpWidth5.place(rely=0.5,relx=0.4,anchor=W)
		self.VPW5.set(str(self.modes[8].params["Ventricular Pulse Width"]))
		ttk.Label(self.frame14,text="Ventricular Pulse Width(ms): ").place(rely=0.5,relx=0.4,anchor=E)

				# Sensitivity
		'''
		self.VSENS5 = StringVar()
		self.vSens5 = Entry(self.frame14, textvariable=self.VSENS5)
		self.vSens5.place(rely=0.42,relx=0.4,anchor=W)
		self.VSENS5.set(str(self.modes[8].params["Ventricular Sensitivity"]))
		ttk.Label(self.frame14, text="Ventricular Sensitivity(mV): ").place(rely=0.42,relx=0.4,anchor=E)
		'''

                # VRP
		self.VREF5 = StringVar()
		self.vRef5 = Entry(self.frame14, textvariable=self.VREF5)
		self.vRef5.place(rely=0.59,relx=0.4,anchor=W)
		self.VREF5.set(str(self.modes[8].params["VRP"]))
		ttk.Label(self.frame14, text="VRP(ms): ").place(rely=0.59,relx=0.4,anchor=E)

		#Hysteresis
		'''
		self.VHYS5 = StringVar()
		self.vhys5 = Entry(self.frame14, textvariable=self.VHYS5)
		self.vhys5.place(rely=0.56,relx=0.4,anchor=W)
		self.VHYS5.set(str(self.modes[8].params["Hysteresis"]))
		ttk.Label(self.frame14, text="Hysteresis(ppm): ").place(rely=0.56,relx=0.4,anchor=E)

                # Rate Smoothing
		self.VRSMOOTH5 = StringVar()
		self.vRsmooth5 = Entry(self.frame14, textvariable=self.VRSMOOTH5)
		self.vRsmooth5.place(rely=0.63,relx=0.4,anchor=W)
		self.VRSMOOTH5.set(str(self.modes[8].params["Rate Smoothing"]))
		ttk.Label(self.frame14, text="Rate Smoothing(%): ").place(rely=0.63,relx=0.4,anchor=E)
		'''

                # Activity Threshold
		self.VACTTHRESH5 = StringVar()
		self.vActthresh5 = Entry(self.frame14, textvariable=self.VACTTHRESH5)
		self.vActthresh5.place(rely=0.68,relx=0.4,anchor=W)
		self.VACTTHRESH5.set(str(self.modes[8].params["Activity Threshold"]))
		ttk.Label(self.frame14,text="Activity Threshold(1-7): ").place(rely=0.68,relx=0.4,anchor=E)

                # Reaction Time
		self.VREACTTIME5 = StringVar()
		self.vReacttime5 = Entry(self.frame14, textvariable=self.VREACTTIME5)
		self.vReacttime5.place(rely=0.77,relx=0.4,anchor=W)
		self.VREACTTIME5.set(str(self.modes[8].params["Reaction Time"]))
		ttk.Label(self.frame14,text="Reaction Time(s): ").place(rely=0.77,relx=0.4,anchor=E)

                # Response Factor
		self.VRESPFACT5 = StringVar()
		self.vRespfact5 = Entry(self.frame14, textvariable=self.VRESPFACT5)
		self.vRespfact5.place(rely=0.86,relx=0.4,anchor=W)
		self.VRESPFACT5.set(str(self.modes[8].params["Response Factor"]))
		ttk.Label(self.frame14,text="Response Factor(1-16): ").place(rely=0.86,relx=0.4,anchor=E)

                # Recovery Time
		self.VRECOVTIME5 = StringVar()
		self.vRecovtime5 = Entry(self.frame14, textvariable=self.VRECOVTIME5)
		self.vRecovtime5.place(rely=0.95,relx=0.4,anchor=W)
		self.VRECOVTIME5.set(str(self.modes[8].params["Recovery Time"]))
		ttk.Label(self.frame14,text="Recovery Time(min): ").place(rely=0.95,relx=0.4,anchor=E)


		ttk.Button(self.frame14,text="Set Values",command=lambda:self.VerifySet([self.vLowRate5.get(),self.vUpRate5.get(),self.vMaxsens5.get(),\
                                self.vAmp5.get(),self.vpWidth5.get(),self.vRef5.get(),\
                                self.vActthresh5.get(),self.vReacttime5.get(),self.vRespfact5.get(),self.vRecovtime5.get()],8))\
                                .place(rely=0.3,relx=0.875,anchor=CENTER)
		ttk.Button(self.frame14,text="Back",command=lambda:self.Cancel(self.frame14)).place(rely=0.7,relx=0.875,anchor=CENTER)

		Button(self.frame14,text="    Send    ",command=lambda:self.Send("VVIR",self.modes[8].params),bg="green").place(rely=0.5,relx=.875,anchor=CENTER)


		## Screen 2.12 -- EDIT DOOR
		self.frame15 = ttk.Frame(self.master,width=400,height=400,relief=RAISED,padding='3 3 12 12')
		self.frame15.grid(row=0,column=0)
		self.frame15.grid_propagate(0)

		ttk.Label(self.frame15,text="Edit DOOR Mode").place(rely=0.02,relx=0.5,anchor=CENTER)

                # Lower Limit
		self.LRL6 = StringVar()
		self.LowRate6 = Entry(self.frame15, textvariable=self.LRL6)
		self.LowRate6.place(rely=0.08,relx=0.4,anchor=W)
		self.LRL6.set(str(self.modes[9].params["Lower Rate Limit"]))
		ttk.Label(self.frame15,text="Lower Rate Limit(ppm): ").place(rely=0.08,relx=0.4,anchor=E)

				# Upper Limit
		self.URL6 = StringVar()
		self.UpRate6 = Entry(self.frame15, textvariable=self.URL6)
		self.UpRate6.place(rely=0.16,relx=0.4,anchor=W)
		self.URL6.set(str(self.modes[9].params["Upper Rate Limit"]))
		ttk.Label(self.frame15,text="Upper Rate Limit(ppm): ").place(rely=0.16,relx=0.4,anchor=E)

				# Max Sensor Rate
		self.MAXSENS6 = StringVar()
		self.Maxsens6 = Entry(self.frame15, textvariable=self.MAXSENS6)
		self.Maxsens6.place(rely=0.24,relx=0.4,anchor=W)
		self.MAXSENS6.set(str(self.modes[9].params["Max Sensor Rate"]))
		ttk.Label(self.frame15,text="Max Sensor Rate(ppm): ").place(rely=0.24,relx=0.4,anchor=E)

				# Fixed AV Delay
		self.AVDELAY6 = StringVar()
		self.avDelay6 = Entry(self.frame15, textvariable=self.AVDELAY6)
		self.avDelay6.place(rely=0.32,relx=0.4,anchor=W)
		self.AVDELAY6.set(str(self.modes[9].params["Fixed AV Delay"]))
		ttk.Label(self.frame15, text="Fixed AV Delay(ms): ").place(rely=0.32,relx=0.4,anchor=E)

				# Atrial Amp
		self.AA6 = StringVar()
		self.aAmp6 = Entry(self.frame15, textvariable=self.AA6)
		self.aAmp6.place(rely=0.4,relx=0.4,anchor=W)
		self.AA6.set(str(self.modes[9].params["Atrial Amp"]))
		ttk.Label(self.frame15,text="Atrial Amplitude(V): ").place(rely=0.4,relx=0.4,anchor=E)

				# Ventricular Amp
		self.VA6 = StringVar()
		self.vAmp6 = Entry(self.frame15, textvariable=self.VA6)
		self.vAmp6.place(rely=0.48,relx=0.4,anchor=W)
		self.VA6.set(str(self.modes[9].params["Ventricular Amp"]))
		ttk.Label(self.frame15,text="Ventricular Amplitude(V): ").place(rely=0.48,relx=0.4,anchor=E)

				# Atrial Pulse Width
		self.APW6 = StringVar()
		self.apWidth6 = Entry(self.frame15, textvariable=self.APW6)
		self.apWidth6.place(rely=0.56,relx=0.4,anchor=W)
		self.APW6.set(str(self.modes[9].params["Atrial Pulse Width"]))
		ttk.Label(self.frame15,text="Atrial Pulse Width(ms): ").place(rely=0.56,relx=0.4,anchor=E)

				# Ventricular Pulse Width
		self.VPW6 = StringVar()
		self.vpWidth6 = Entry(self.frame15, textvariable=self.VPW6)
		self.vpWidth6.place(rely=0.64,relx=0.4,anchor=W)
		self.VPW6.set(str(self.modes[9].params["Ventricular Pulse Width"]))
		ttk.Label(self.frame15,text="Ventricular Pulse Width(ms): ").place(rely=0.64,relx=0.4,anchor=E)

                # Activity Threshold
		self.ACTTHRESH6 = StringVar()
		self.Actthresh6 = Entry(self.frame15, textvariable=self.ACTTHRESH6)
		self.Actthresh6.place(rely=0.72,relx=0.4,anchor=W)
		self.ACTTHRESH6.set(str(self.modes[9].params["Activity Threshold"]))
		ttk.Label(self.frame15,text="Activity Threshold(1-7): ").place(rely=0.72,relx=0.4,anchor=E)

                # Reaction Time
		self.REACTTIME6 = StringVar()
		self.Reacttime6 = Entry(self.frame15, textvariable=self.REACTTIME6)
		self.Reacttime6.place(rely=0.80,relx=0.4,anchor=W)
		self.REACTTIME6.set(str(self.modes[9].params["Reaction Time"]))
		ttk.Label(self.frame15,text="Reaction Time(s): ").place(rely=0.80,relx=0.4,anchor=E)

                # Response Factor
		self.RESPFACT6 = StringVar()
		self.Respfact6 = Entry(self.frame15, textvariable=self.RESPFACT6)
		self.Respfact6.place(rely=0.88,relx=0.4,anchor=W)
		self.RESPFACT6.set(str(self.modes[9].params["Response Factor"]))
		ttk.Label(self.frame15,text="Response Factor(1-16): ").place(rely=0.88,relx=0.4,anchor=E)

                # Recovery Time
		self.RECOVTIME6 = StringVar()
		self.Recovtime6 = Entry(self.frame15, textvariable=self.RECOVTIME6)
		self.Recovtime6.place(rely=0.96,relx=0.4,anchor=W)
		self.RECOVTIME6.set(str(self.modes[9].params["Recovery Time"]))
		ttk.Label(self.frame15,text="Recovery Time(min): ").place(rely=0.96,relx=0.4,anchor=E)

				#BACK, SET, and SEND buttons
		ttk.Button(self.frame15,text="Set Values",command=lambda:self.VerifySet([self.LowRate6.get(),self.UpRate6.get(),self.Maxsens6.get(),\
                                self.avDelay6.get(),self.aAmp6.get(),self.vAmp6.get(),self.apWidth6.get(),self.vpWidth.get(),\
                                self.Actthresh6.get(),self.Reacttime6.get(),self.Respfact6.get(),self.Recovtime6.get()],9))\
                                .place(rely=0.3,relx=0.875,anchor=CENTER)
		ttk.Button(self.frame15,text="Back",command=lambda:self.Cancel(self.frame15)).place(rely=0.7,relx=0.875,anchor=CENTER)

		Button(self.frame15,text="    Send    ",command=lambda:self.Send("DOOR",self.modes[9].params),bg="green").place(rely=0.5,relx=.875,anchor=CENTER)



		## Make sure frame1 is the first frame the user sees
		self.RaiseFrame(self.frame1)
		
	def RaiseFrame(self,frame): #Uses tkraise function to switch between screens
		frame.tkraise()

	def Cancel(self,frame): #Return to 'homescreen' 
		if frame==self.frame2:
			self.NEWUSER.set('')
			self.NEWPASS.set('')
			self.RaiseFrame(self.frame1)
		elif frame==self.frame3:
			self.USER.set('')
			self.PASS.set('')
			self.RaiseFrame(self.frame1)
		elif frame==self.frame4:
			self.ID.set('')
			self.RaiseFrame(self.frame1)
		elif frame==self.frame6 or self.frame7 or self.frame8 or self.frame9 or self.frame10\
                     or self.frame11 or self.frame12 or self.frame13 or self.frame14 or self.frame15:
			self.RaiseFrame(self.frame5)

	def ShowOrHide(self,val):
		if val==1:
			self.Pass.config(show='')
		else:
			self.Pass.config(show='*')


	def SaveUser(self): #saves new username and password in users.txt file
		print("user save")
		if self.newUser.get()=='' or self.newPass.get()=='':
			box = DialogBox(self.master,"Please fill out both entries to register")
		else:
			opts = [self.newUser.get(),self.newPass.get()]
			self.List.addUser(DCM_users.User(opts[0],opts[1]))
			self.NEWUSER.set('')
			self.NEWPASS.set('')
			string = self.List.__str__()
			print(string)
			box = DialogBox(self.master,"Successfully registered")
			self.RaiseFrame(self.frame1)

	def VerifyLogin(self): #Checks if username and password have been registered/are correct
		print("user login")
		if self.User.get()=='' or self.Pass.get()=='':
			box = DialogBox(self.frame3,"Please fill out both entries to continue")
		else:
			check = False
			n = self.User.get()
			pos = 0
			for i in self.List.users:
				if n == i.name:
					check=True
					pos = i
			if check:
				p = self.Pass.get()
				if p==pos.password:
					print("successful login")
					self.RaiseFrame(self.frame4)
					self.USER.set('')
					self.PASS.set('')
				else:
					print("wrong password")
					box = DialogBox(self.frame3,"Username or password not recognised")
			else:
				print("username not registered")
				box = DialogBox(self.frame3,"Username or password not recognised")

	def checkID(self,id): #Hardcoded for now
		if id=='1234':
			self.RaiseFrame(self.frame5)
		else:
			box = DialogBox(self.master,text="You have not entered the correct ID")
4
	def VerifySet(self,params,mode):
		print("Verify parameters")
		result = self.modes[mode].verifyAndSet(params)
		if result==False:
			box = DialogBox(self.master,"One (or more) of the following issues has been found:\n"\
                                        +"-Data is of the wrong type\n-One or more entry fields are empty\n"\
                                        +"-Lower Rate Limit is higher than Upper Rate Limit")
		elif result==True:
			box = DialogBox(self.master,"Parameters successfully set")
		else:
			box = DialogBox(self.master,result)

	def Send(self,mode,params):
		print("Parameters will be sent")
		try:
			self.serialComm.Communicate(mode,params)
			box = DialogBox(self.master,"Paramaters Sent to Pacemaker")
		except:
			box = DialogBox(self.master,"Serial Port not connected")
		
	def LeaveEdit(self):
		for i in self.modes:
			i.saveParams(i.params)
		self.RaiseFrame(self.frame1)

	def Exit(self):
		self.List.saveFile("users.txt")
		self.master.destroy()






root = Tk()
DCM = GUI(root)


root.mainloop()
		
