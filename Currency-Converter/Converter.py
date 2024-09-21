from tkinter import *
from datetime import datetime
from timezonefinder import TimezoneFinder
import pytz
from tkinter import ttk
import json
import requests


def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    querystring = {"from": option1.get(), "to": option2.get(), "amount": in_value.get()}

    headers = {
        "X-RapidAPI-Key": "{your key number}",
        "X-RapidAPI-Host": "{your host number}"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    j_data = json.loads(response.text)
    result = j_data["result"]["convertedAmount"]
    result = "{:,.3f}".format(result)
    out_value["text"] = result


# main window
window = Tk()
window.title("Currency Converter")
window.geometry("800x500")
window.resizable(False, False)
window.config(background="white")

# Title
title = Label(window, anchor="w", text="Currency Converter", font=("Bookman Old Style", 25, "bold"), fg="white",
              bg="black", width=800, height=1)
title.place(x=0, y=0)

# Labels for displaying current time
clock_label = Label(window, font=("Century", 15), bg="white")
clock_label.place(x=172, y=450)
clock_time = Label(window, font=("Century", 15), bg="white")
clock_time.place(x=380, y=448)
timezone = TimezoneFinder()
place = timezone.timezone_at(lng=-71.0589, lat=42.361145)
location = pytz.timezone(place)
time_info = datetime.now(location)
time = time_info.strftime("%m/%d/%y %I:%M %p")
clock_label.config(text="Current Time (EST): ")
clock_time.config(text=time)

text1 = Label(window, anchor="w", text="From", font=("Century", 21, "bold"), fg="black",
              bg="white", width=100, height=1)
text1.place(x=30, y=60)

text2 = Label(window, anchor="w", text="To", font=("Century", 21, "bold"), fg="black",
              bg="white", width=100, height=1)
text2.place(x=30, y=280)

currency_list = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AZN", "BRL", "BAM", "BBD", "BDT", "BGN", "BHD",
                 "BIF", "BMD", "BND", "BOB", "BSD", "BWP", "BYN", "BZD", "CAD", "CDF", "CLP", "CNH", "CNY", "COD",
                 "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "ECS", "EGP", "ERN", "ETB", "ETH",
                 "EUR", "FJD", "FKD", "GBP", "GEL", "GHS", "GID", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK",
                 "HTG", "HVF", "IDR", "ILS", "INR", "IQD", "IRR", "ISL", "JMD", "KES", "KGS", "KHR", "KMF", "KPW",
                 "KWD", "KWD", "KYD", "KDZ", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD",
                 "MMK", "MNT", "MOP", "MRU", "MUR", "MXN", "MYR", "MZN", "NAD", "NGN", "ILS", "INR", "JPY", "KRW",
                 "NZN", "PHP", "RUB", "USD", "VND"]

option1 = ttk.Combobox(window, width=18, height=20, font=("Century", 19), justify="center")
option1.set("Select the Currency")
option1["values"] = currency_list
option1.place(x=180, y=130)

option2 = ttk.Combobox(window, width=18, height=20, font=("Century", 19), justify="center")
option2.set("Select the Currency")
option2["values"] = currency_list
option2.place(x=180, y=340)

in_value = Entry(window, width=14, background="#f0f0f5", font=("Century", 20), justify="center", borderwidth=1,
                 relief="solid")
in_value.place(x=520, y=130)

out_value = Label(window, text=" ", width=12, relief="solid", anchor=CENTER, font=("Century", 20), borderwidth=1,
                  background="#f0f0f5")
out_value.place(x=520, y=340)

button = Button(window, text="Convert", font=("Bookman Old Style", 20, "bold"), fg="white", width=10, height=1,
                bg="#1565C0", borderwidth=4, command=convert)
button.place(x=320, y=205)

window.mainloop()
