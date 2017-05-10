import time
import weather
import news
from tkinter import *
# VNC
time_format = 12 # 12 or 24
date_format = "%b %d, %Y" #  %b = month, %d = day, %Y = year.
dictday = {'Sunday': 'Domingo', 'Monday': 'Segunda-feira', 'Tuesday': 'Terça-feira','Wednesday':'Quarta-feira',"Thursday":"Quinta-feira","Friday":"Sexta-feira","Saturay":"Sábado"}
dictmonth ={"January":"Janeiro","February":"Fevereiro","March":"Março", "April":"Abril","May":"Maio","June":"Junho", "July":"Julho","August":"Agosto","Seṕtember":"Setembro","October":"Outubro","November":"Novembro","December":"Dezembro"}
dictweather = {'Clouds':'Nublado', 'Rain':'Chuvoso', 'Thunderstorm':'Chuva de Raios!', 'Drizzle':'Garoa', 'Snow':'Neve', 'Clear':'Ensolarado', 'Extreme':'RUN TO THE HILLS'}

class Clock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        # initialize time label
        self.time1 = ''
        self.timeLbl = Label(self, font=('Helvetica', 40), fg="white", bg="black")
        self.timeLbl.pack(side=TOP, anchor=E)
        # initialize day of week
        self.day_of_week1 = ''
        self.dayOWLbl = Label(self, text=self.day_of_week1, font=('Helvetica', 18), fg="white", bg="black")
        self.dayOWLbl.pack(side=TOP, anchor=E)
        # initialize date label
        self.date1 = ''
        self.dateLbl = Label(self, text=self.date1, font=('Helvetica', 18), fg="white", bg="black")
        self.dateLbl.pack(side=TOP, anchor=E)
        self.tick()

    def tick(self):
            if time_format == 12:
                time2 = time.strftime('%I:%M %p') #hour in 12h format
            else:
                time2 = time.strftime('%H:%M') #hour in 24h format

            day_of_week2 = time.strftime('%A')
            
            date2 = time.strftime(date_format)
            # if time string has changed, update it
            if time2 != self.time1:
                self.time1 = time2
                self.timeLbl.config(text=time2)
            if day_of_week2 != self.day_of_week1:
                self.day_of_week1 = day_of_week2
                self.dayOWLbl.config(text=dictday[day_of_week2])
            if date2 != self.date1:
                self.date1 = date2
                array = date2.split(" ")
                formatedDate =array[1].split(",")[0]+ " de " +dictmonth[array[0]]+" de "+array[2] #this do the date translation to portuguese
                self.dateLbl.config(text=formatedDate)
            # calls itself every 200 milliseconds
            # to update the time display as needed
            # could use >200 ms, but display gets jerky
            self.timeLbl.after(200, self.tick)

class Weather (Frame):
    def __init__ ( self , parent, *args, **kwargs):
        Frame.__init__(self,parent, bg = 'black')
        # Init a label
        self.temp = weather.get_temperature()
        self.tempLabel = Label ( self, font = ('Helvetca', 40), fg = "white", bg = "black")
        self.tempLabel.pack( side = TOP, anchor = E)
        self.condition = weather.get_condition()
        self.conditionLabel = Label ( self,text = dictweather[self.condition], font = ('Helvetca', 40), fg = "white", bg = "black")
        self.conditionLabel.pack( side = TOP, anchor = E)
        self.tick()
    def tick(self):
        self.tempLabel.config(text = self.temp)

class News (Frame):
    def __init__ ( self , parent, *args, **kwargs):
        Frame.__init__(self,parent, bg = 'black')
        # Init a label
        newss = news.get_news()
        self.new0 = newss[0]
        self.new1 = newss[1]
        self.new2 = newss[2]
        self.meuLabel = Label ( self, font = ('Helvetca', 18), fg = "white", bg = "black")
        self.meuLabel.pack( side = TOP, anchor = W)
        self.meuLabel2 = Label ( self, text=self.new1,font = ('Helvetca', 18), fg = "white", bg = "black")
        self.meuLabel2.pack( side = TOP, anchor = W)
        self.meuLabel3 = Label ( self,text= self.new2, font = ('Helvetca', 18), fg = "white", bg = "black")
        self.meuLabel3.pack( side = TOP, anchor = W)
        self.tick()
    def tick(self):
        self.meuLabel.config(text = self.new0) 

class FullscreenWindow:

    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background='black')
        self.topFrame = Frame(self.tk, background = 'black')
        self.bottomFrame = Frame(self.tk, background = 'black')
        self.topFrame.pack(side = TOP, fill=BOTH, expand = YES)
        self.bottomFrame.pack(side = BOTTOM, fill=BOTH, expand = YES)
        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        # clock
        self.clock = Clock(self.topFrame)
        self.clock.pack(side=RIGHT, anchor=N, padx=100, pady=60)
        # weather
        self.temp = Weather(self.topFrame)
        self.temp.pack(side=LEFT,anchor=N,padx=100, pady = 60)
         # news
        self.news = News(self.bottomFrame)
        self.news.pack(side=LEFT, anchor=S, padx=100, pady=60)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"


if __name__ == '__main__':
    weather.get_weather()
    news.get_news_data()
    w = FullscreenWindow()
    w.tk.mainloop()
