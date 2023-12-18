# World Clock
# By Siddharth Jai Gokulan

import datetime as dt
import pytz
import customtkinter as ctk
import pycountry

countryZones = dict(pytz.country_timezones)
countryCodeList = list(countryZones.keys())
countryList = []
for i in countryCodeList :
    countryList.append((pycountry.countries.get(alpha_2 = i)).name)
timezoneList = ['UTC']

def getZones(country) :
    global timezoneList
    global zoneSelect
    timezoneList = list(countryZones[(pycountry.countries.get(name = country)).alpha_2])
    zoneSelect.destroy()
    zoneSelect = ctk.CTkOptionMenu(master=root, width=450, height=30, values=timezoneList, command=checkTime)
    zoneSelect.place(relx=0.5, rely=0.22, anchor=ctk.N)
    checkTime(zoneSelect.get())

def checkTime(currentZone) :
    localisedTime = dt.datetime.now(pytz.timezone(currentZone))
    zoneTime = localisedTime.strftime("%H:%M:%S %d-%m-%Y")
    zoneOffset = localisedTime.strftime("%z")
    offsetString = zoneOffset[0:3] + ":" + zoneOffset[3:]
    timeString.set(f"Current timezone: {currentZone} (UTC{offsetString})\nTime: {zoneTime}")
    root.after(1000, lambda: checkTime(zoneSelect.get()))

root = ctk.CTk()
root.geometry("500x500")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root.title("World Clock")
title = ctk.CTkLabel(master=root, text="WORLD CLOCK", font=("Bahnschrift", 30))
title.place(relx=0.5, rely=0.04, anchor=ctk.N)
countrySelect = ctk.CTkOptionMenu(master=root, width=450, height=30, values=countryList, command=getZones)
countrySelect.place(relx=0.5, rely=0.15, anchor=ctk.N)
zoneSelect = ctk.CTkOptionMenu(master=root, width=450, height=30, values=timezoneList, command=checkTime)
zoneSelect.place(relx=0.5, rely=0.22, anchor=ctk.N)
zoneSelect.set("Select a timezone...")
timeString = ctk.StringVar()
timeString.set("Select a timezone to begin.")
timeLabel = ctk.CTkLabel(master=root, textvariable=timeString)
timeLabel.place(relx=0.5, rely=0.3, anchor=ctk.N)

root.mainloop()