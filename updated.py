import urllib.request
import json
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Humare project ka front-end")
window.geometry('900x900')

lbl1=Label(window,text="ENVIRONMENT")
lbl1.grid(column=0,row=0)
var1 =StringVar(window)
var1.set('Acetaldehyde')
choices1 = ['Acetaldehyde','Acetamide','Acetic Acid','Acetic Anhydride','Acetochloride','Acetone','Acetosalicylic Acid','Adipic Acid','Aluminum Acetate','Aluminum Ammonium Sulfate','Aluminum Chloride','Aluminum Fluoride','Aluminum Hydroxide','Aluminum Nitrate','Aluminum Sulfate','Aminoacetic Acid','Ammonia','Ammonium Bicarbonate','Ammonium Bifluoride','Ammonium Bisulfate','Ammonium Carbonate','Ammonium Chloride','Ammonium Fluoride','Ammonium Hexachlorostannate','Ammonium Hydroxide','Ammonium Nitrate','Ammonium Oxalate','Ammonium Perchlorate','Ammonium Phosphate','Ammonium Sulfate','Ammonium Sulfite','Aniline','Aniline Hydrochloride','Antimony Chloride','Aqua Regia','Arsenic Acid','Atmospheric Environments','Barium ']
txt1= OptionMenu(window, var1, *choices1)
txt1.grid(column=1,row=0)

lbl2 = Label(window,text="MATERIAL GROUP")
lbl2.grid(column=0,row=1)
var2 =StringVar(window)
var2.set('irons')
choices2 = ['Aluminum and alloys','Carbon and alloy steels','Copper and alloys','Iron-nickel alloys','Irons','Irons and alloys','Miscellaneous','Miscellaneous','Nickel and alloys','Nickel and alloys','Nickel and alloys','Refractory metals and alloys','Refractory metals and alloys','Refractroy metals and alloys','Stainless Steels']
txt2 = OptionMenu(window, var2, *choices2)
txt2.grid(column=1,row=1)


lbl3 = Label(window,text="MATERIAL FAMILY")
lbl3.grid(column=0,row=2)
var3 =StringVar(window)
var3.set('Aluminum')
choices3 = ['Alloy Steel','Alloy steel','Aluminum','Aluminum brass','Aluminum bronze','Aluminum Bronze','Aluminum-copper','Aluminum-magnesium','Aluminum-magnesium-silicon','Aluminum-manganese','Aluminum-silicon','Aluminum-zinc','Austenitc','Austenitic','Austenitic ','Austenitic cast iron','Austenitic ductile cast iron',
'Brass','Carbon steel','Cast steel','Chromium','Chromium alloy','Chromium and alloys','Cobalt and alloys','Copper','Copper-nickel','Ductile cast iron','Duplex','Ferritic''Gray cast iron','Hafnium','Hafnium and alloys','Ingot iron','Iron-nickel','Lead and allloys','Lead and alloys','Lead and alloys ','Lead and aloys','Leaded brass','Magnesium','Magnesium and alloys','Martensitic','Miscellaneous','Molybdenum','Molybdenum and alloys','Ni-Cr-P','Nickel','Nickel steel','Nickel-chromium','Nickel-chromium- molybdenum- tungsten','NIckel-chromium-iron','Nickel-chromium-iron','Nickel-chromium-iron-molybdenum','Nickel-chromium-molybdenum','Nickel-chromium-molybdenum-(tungsten)','Nickel-chromium-molybdenum-cobalt','Nickel-chromium-molybdenum-tungsten','Nickel-copper','Nickel-molybdenum']
txt3= OptionMenu(window, var3, *choices3)
txt3.grid(column=1,row=2)

lbl4 = Label(window,text="MATERIAL")
lbl4.grid(column=0,row=3)
var4 = StringVar(window)
var4.set('Copper')
choices4=['Copper- tin','Copper-aluminum-iron','Copper-aluminum-silicon','Copper-nickel','Copper-nickel-zinc (75Cu-20Ni-5Zn)','Copper-silicon','Copper-tin','Copper-zinc','Inconel 625 Inco Alloys International, Inc.','Inconel 671 Inco International, Inc.','Inconel 690 ','Inconel 690 Inco Alloys International In','Nickel6','Nickel alloy','Nickel -silver','Nickel 201','Nickel 200','Nickel 201','Nickel 400 ','Nickel 600 ','Nickel 625 ','Nickel 825 ','Nickel alloy','Nickel alloy B','Nickel alloy C','Nickel alloy C ','Nickel B-2 ','Zr7O2 ']
txt4=OptionMenu(window, var4, *choices4)
txt4.grid(column=1,row=3)

lbl5=Label(window,text="LOCALIZED ATTACK")
lbl5.grid(column=0,row=4)
txt5=Entry(window,width=10)
txt5.grid(column=1,row=4)
lbl6=Label(window,text="CONCENTRATION")
lbl6.grid(column=0,row=5)
txt6=Entry(window,width=10)
txt6.grid(column=1,row=5)
lbl7=Label(window,text="DAYS")
lbl7.grid(column=0,row=6)
txt7=Entry(window,width=10)
txt7.grid(column=1,row=6)
lbl8=Label(window,text="TEMPERATURE")
lbl8.grid(column=0,row=7)
txt8=Entry(window,width=10)
txt8.grid(column=1,row=7)
lbl9=Label(window,text="RATE")
lbl9.grid(column=0,row=8)
txt9=Entry(window,width=10)
txt9.grid(column=1,row=8)
lbl10=Label(window,text="")
lbl10.grid(column=2,row=20)

def clicked():
  data={
    "Inputs":{
      "input1":
        [
          {
            'Environment': var1.get(),
            'mGroup': var2.get(),
            'mFamily': var3.get(),
            'Material': var4.get(),
            'localizedAttack': txt5.get(),
            'Conc': txt6.get(),
            'days':txt7.get(),
            'Temperature (deg C)': txt8.get(),
            'rate1': txt9.get(),
          }
        ],
      	 		 },
  	 "GlobalParameters":  {
   			      }
	}
  body = str.encode(json.dumps(data))
  url = 'https://ussouthcentral.services.azureml.net/workspaces/053fd63ff313491a94553e4597480612/services/8adf385ca8f74d399a95f35b096571de/execute?api-version=2.0&format=swagger'
  api_key = 'tUGXC2NFb5s5ZykrvnA9RgRup3UbwxEymEFXU7I6LCIyulNbLJYJUBhNSSMQQio4MIFUbhGiIAYvkCVmIpmvXA==' # Replace this with the API key for the web service
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

  req = urllib.request.Request(url, body, headers)

  try:
    response = urllib.request.urlopen(req)
    result = response.read()
    lbl10.config(text=result)
   
  except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    
  
btn=Button(window,text="SUBMIT",bg="orange", fg="black", command=clicked)
btn.grid(column=2,row=10) 
window.mainloop()