from pydoc import text
import tkinter as tk
from turtle import bgcolor
import tkinter.font as tkFont
import webbrowser


class MyApp():

    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("650x400+345+150")
        self.root.title("Crypto Price Calculator")
        self.root.configure(bg = "#393E46")

        self.label = tk.Label(self.root, text="Choose an action:", font=("Calibri",30) ,bg = "#393E46", fg = "#F7F7F7")
        self.label.pack(padx = 10, pady = 30)

        self.optionFrame = tk.Frame(self.root,pady = 15, bg = "#393E46")
        self.optionFrame.columnconfigure(0,weight = 1)

        self.option1 = tk.Button(
            self.optionFrame,
            text='Calculate the number of tokens',
            font=('Calbri',14),
            bg = "#6D9886",
            width = 30, 
            borderwidth = 5,
            command = Window1
        )
        self.option1.grid(row=0,column=0,pady=5)

        self.option2 = tk.Button(
            self.optionFrame,
            text='How many dollars is N tokens',
            font=('Calbri',14), 
            bg = "#6D9886",
            width = 30,
            borderwidth = 5,
            command = Window2
        )
        self.option2.grid(row=1,column=0,pady=5)

        self.option3 = tk.Button(
            self.optionFrame,
            text='At what rate will you double/triple',
            font=('Calbri',14), 
            bg = "#6D9886",
            width = 30,
            borderwidth = 5,
            command = Window3
        )
        self.option3.grid(row=2,column=0,pady=5)

        self.option4 = tk.Button(
            self.optionFrame,
            text='Links to useful websites',
            font=('Calbri',14), 
            bg = "#6D9886",
            width = 30,
            borderwidth = 5,
            command = Window4
        )
        self.option4.grid(row=3,column=0,pady=5)

        self.optionFrame.pack(fill ='x')

        f = tkFont.Font(self.label, self.label.cget("font"))
        f.configure(underline = True, weight = 'bold')
        self.label.configure(font=f)
        
        self.root.mainloop()
    


class Window1():
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("550x350+400+225")
        self.root.title("Crypto Price Calculator")
        self.root.configure(bg = "#393E46")

        self.label = tk.Label(
            self.root, 
            text="Token Calculator", 
            font=("Calibri",25) ,
            fg = "#F7F7F7", 
            bg = "#393E46"
        )
        self.label.pack(padx = 10, pady = 30)

        self.calcFrame = tk.Frame(self.root,pady = 15,padx=50, bg = "#393E46")
        self.calcFrame.columnconfigure(0,weight = 1)
        self.calcFrame.columnconfigure(1,weight = 1)
        #self.calcFrame.rowconfigure(0,weight=2)


        self.l1 = tk.Label(
            self.calcFrame,
            text='Enter Dollar Amount: ', 
            bg = "#393E46", 
            fg = "#F7F7F7",
            font=("Calibri",12)
        )
        self.l1.grid(row=0,column=0)
        self.dollar_amount = tk.Entry(self.calcFrame,width=20,fg='black')
        self.dollar_amount.grid(row=1,column=0)

        self.l2 = tk.Label(
            self.calcFrame,
            text='Enter The Coin\'s Value: ', 
            bg = "#393E46", 
            fg = "#F7F7F7",
            font=("Calibri",12)
        )
        self.l2.grid(row=0,column=1)
        self.dollar_value = tk.Entry(self.calcFrame,width=20,fg='black')
        self.dollar_value.grid(row=1,column=1)


        self.resultFrame = tk.Frame(self.root,pady = 15, bg = "#393E46")


        def func1():
            self.num_tokens.destroy()
            amount,value = self.dollar_amount.get(),self.dollar_value.get()
            result = (float(amount)/float(value))
            self.num_tokens = tk.Label(
            self.resultFrame,
            text = 'You will get ' + str("{:.4f}".format(result)) + ' coins/tokens.', 
            bg = "#393E46", 
            fg = "#F7F7F7",
            font=("Calibri",18)
            )
            self.num_tokens.pack()



        self.calcButton = tk.Button(
            self.resultFrame,
            text='Calculate', 
            bg = "#6D9886", 
            fg = "black",
            font=("Calibri",14),
            width = 30, 
            borderwidth = 5,
            command = func1
        )
        self.calcButton.pack()

        self.num_tokens = tk.Label(self.resultFrame, bg = "#393E46")
        self.num_tokens.pack()

        self.calcFrame.pack(fill ='x')
        self.resultFrame.pack(fill ='x')

        f = tkFont.Font(self.label, self.label.cget("font"))
        f.configure(underline = True, weight = 'bold')
        self.label.configure(font=f)



class Window2():
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("550x350+400+225")
        self.root.title("Crypto Price Calculator")
        self.root.configure(bg = "#393E46")

        self.label = tk.Label(
            self.root, 
            text="Dollar Calculator", 
            font=("Calibri",25) ,
            fg = "#F7F7F7", 
            bg = "#393E46"
        )
        self.label.pack(padx = 10, pady = 30)

        self.calcFrame = tk.Frame(self.root,pady = 15,padx=50, bg = "#393E46")
        self.calcFrame.columnconfigure(0,weight = 1)
        self.calcFrame.columnconfigure(1,weight = 1)
        #self.calcFrame.rowconfigure(0,weight=2)


        self.l1 = tk.Label(
            self.calcFrame,
            text='Enter Token Amount: ', 
            bg = "#393E46", 
            fg = "#F7F7F7",
            font=("Calibri",12)
        )
        self.l1.grid(row=0,column=0)
        self.token_amount = tk.Entry(self.calcFrame,width=20,fg='black')
        self.token_amount.grid(row=1,column=0)

        self.l2 = tk.Label(
            self.calcFrame,
            text='Enter The Coin\'s Value: ', 
            bg = "#393E46", 
            fg = "#F7F7F7",
            font=("Calibri",12)
        )
        self.l2.grid(row=0,column=1)
        self.dollar_value = tk.Entry(self.calcFrame,width=20,fg='black')
        self.dollar_value.grid(row=1,column=1)


        self.resultFrame = tk.Frame(self.root,pady = 15, bg = "#393E46")


        def func1():
            self.num_dollars.destroy()
            amount,value = self.token_amount.get(),self.dollar_value.get()
            result = (float(amount)*float(value))
            self.num_dollars = tk.Label(
            self.resultFrame,
            text = 'You will get ' + str("{:.2f}".format(result)) + ' dollars.', 
            bg = "#393E46", 
            fg = "#F7F7F7",
            font=("Calibri",18)
            )
            self.num_dollars.pack()


        self.calcButton = tk.Button(
            self.resultFrame,
            text='Calculate', 
            bg = "#6D9886", 
            fg = "black",
            font=("Calibri",14),
            width = 30, 
            borderwidth = 5,
            command = func1
        )
        self.calcButton.pack()

        self.num_dollars = tk.Label(self.resultFrame, bg = "#393E46")
        self.num_dollars.pack()

        self.calcFrame.pack(fill ='x')
        self.resultFrame.pack(fill ='x')

        f = tkFont.Font(self.label, self.label.cget("font"))
        f.configure(underline = True, weight = 'bold')
        self.label.configure(font=f)
     
        f = tkFont.Font(self.label, self.label.cget("font"))
        f.configure(underline = True, weight = 'bold')
        self.label.configure(font=f)



class Window3():
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("550x400+400+225")
        self.root.title("Crypto Price Calculator")
        self.root.configure(bg = "#393E46")

        self.label = tk.Label(
            self.root, 
            text="2x, 3x, 5x, 10x Calculator", 
            font=("Calibri",25) ,
            fg = "#F7F7F7", 
            bg = "#393E46"
        )
        self.label.pack(padx = 10, pady = 30)

        def func1():
            self.l2x.destroy()
            self.l3x.destroy()
            self.l5x.destroy()
            self.l10x.destroy()

            value = float(self.dollar_value.get())

            self.l2x = tk.Label(self.resultFrame, text= '2x = ' + str("{:.4f}".format(value*2)), bg = "#393E46", fg = "#F7F7F7", font=("Calibri",14))
            self.l3x = tk.Label(self.resultFrame, text= '3x = ' + str("{:.4f}".format(value*3)), bg = "#393E46", fg = "#F7F7F7", font=("Calibri",14))
            self.l5x = tk.Label(self.resultFrame, text= '5x = ' + str("{:.4f}".format(value*5)), bg = "#393E46", fg = "#F7F7F7", font=("Calibri",14))
            self.l10x = tk.Label(self.resultFrame, text= '10x = ' + str("{:.4f}".format(value*10)), bg = "#393E46", fg = "#F7F7F7", font=("Calibri",14))

            self.l2x.pack()
            self.l3x.pack()
            self.l5x.pack()
            self.l10x.pack()



        self.calcFrame = tk.Frame(self.root, pady = 15 ,padx=10, bg = "#393E46")
        self.calcFrame.columnconfigure(0,weight = 1)


        self.l1 = tk.Label(
            self.calcFrame,
            text='Enter The Coin\'s Value When You Bought It: ', 
            bg = "#393E46", 
            fg = "#F7F7F7",
            font=("Calibri",12)
        )
        self.l1.grid(row=0,column=0)
        self.dollar_value = tk.Entry(self.calcFrame,width=20,fg='black')
        self.dollar_value.grid(row=1,column=0,pady=5)

        self.calcButton = tk.Button(
            self.calcFrame,
            text='Calculate', 
            bg = "#6D9886", 
            fg = "black",
            font=("Calibri",14),
            width = 10, 
            borderwidth = 5,
            command = func1
        )
        self.calcButton.grid(row=2,column=0,pady=10)

        self.resultFrame = tk.Frame(self.root,pady = 5, bg = "#393E46")

        self.l2x = tk.Label(self.resultFrame, bg = "#393E46")
        self.l2x.pack()

        self.l3x = tk.Label(self.resultFrame, bg = "#393E46")
        self.l3x.pack()

        self.l5x = tk.Label(self.resultFrame, bg = "#393E46")
        self.l5x.pack()

        self.l10x = tk.Label(self.resultFrame, bg = "#393E46")
        self.l10x.pack()


        self.calcFrame.pack(fill ='x')
        self.resultFrame.pack(fill ='x')

        f = tkFont.Font(self.label, self.label.cget("font"))
        f.configure(underline = True, weight = 'bold')
        self.label.configure(font=f)



class Window4():
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("850x350+400+225")
        self.root.title("Crypto Price Calculator")
        self.root.configure(bg = "#393E46")

        self.label = tk.Label(
            self.root, 
            text="Useful Links", 
            font=("Calibri",25) ,
            fg = "#F7F7F7", 
            bg = "#393E46"
        )
        self.label.pack(padx = 10, pady = 30)

        def callback(url):
            webbrowser.open_new_tab(url)

        self.linkFrame = tk.Frame(self.root ,pady = 15,padx=50, bg = "#393E46")
        self.linkFrame.columnconfigure(0,weight = 1)
        self.linkFrame.columnconfigure(1,weight = 1)
        self.linkFrame.columnconfigure(2,weight = 1)


        self.l1 = tk.Label(self.linkFrame, text = 'Coin Market Cap', fg="#F7F7F7",bg = "#393E46", cursor="hand2",font=("Calibri",16))
        self.l1.grid(row=0,column=0,pady=10)
        self.l1.bind("<Button-1>", lambda e: callback("https://coinmarketcap.com/"))        
        
        self.l2 = tk.Label(self.linkFrame, text = 'Etheruem Uniswap Price', fg="#F7F7F7",bg = "#393E46", cursor="hand2",font=("Calibri",16))
        self.l2.grid(row=0,column=1,pady=10)
        self.l2.bind("<Button-1>", lambda e: callback("https://uniswap.vision/?ticker=UniswapV2:ETHUSDC&interval=1"))        
        
        self.l3 = tk.Label(self.linkFrame, text = 'Hex Uniswap Price', fg="#F7F7F7",bg = "#393E46", cursor="hand2",font=("Calibri",16))
        self.l3.grid(row=0,column=2,pady=10)
        self.l3.bind("<Button-1>", lambda e: callback("https://uniswap.vision/?ticker=UniswapV2:HEXUSDC&interval=240"))

        self.l4 = tk.Label(self.linkFrame, text = 'Coin Desk', fg="#F7F7F7",bg = "#393E46", cursor="hand2",font=("Calibri",16))
        self.l4.grid(row=1,column=0,pady=10)
        self.l4.bind("<Button-1>", lambda e: callback("https://www.coindesk.com/"))        
        
        self.l5 = tk.Label(self.linkFrame, text = 'Coin Telegraph', fg="#F7F7F7",bg = "#393E46", cursor="hand2",font=("Calibri",16))
        self.l5.grid(row=1,column=1,pady=10)
        self.l5.bind("<Button-1>", lambda e: callback("https://cointelegraph.com/"))        
        
        self.l6 = tk.Label(self.linkFrame, text = 'Crypto News', fg="#F7F7F7",bg = "#393E46", cursor="hand2",font=("Calibri",16))
        self.l6.grid(row=1,column=2,pady=10)
        self.l6.bind("<Button-1>", lambda e: callback("https://cryptonews.com/"))

        self.linkFrame.pack(fill ='x')
        f = tkFont.Font(self.label, self.label.cget("font"))
        f.configure(underline = True, weight = 'bold')
        self.label.configure(font=f)


MyApp()
