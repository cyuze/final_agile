import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import random

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width=800, height=800)
        self.pack()

        master.geometry('600x600')
        master.title('Hello Tkinter')

        self.create_widgets()

    # ウィジェットを配置して画面作るメソッド
    def create_widgets(self):
        # 画像の読み込み
        cimg1 = Image.open("./img/自動販売機.png")

        cimg_ins_coin = Image.open("./img/コイン投入口.png")
        # 画像のリサイズ
        cimg1 = cimg1.resize((480, 653))  # 画像を2倍にする例
        cimg_ins_coin = cimg_ins_coin.resize((132, 95))
        # 画像ファイルのオブジェクトの作成
        self.img1 = ImageTk.PhotoImage(cimg1)
        self.img_ins_coin = ImageTk.PhotoImage(cimg_ins_coin)

        cimg_cola = Image.open("./img/コーラ.png")
        cimg_water = Image.open("./img/水.png")
        cimg_tea = Image.open("./img/お茶.png")
        # 画像のリサイズ
        cimg1 = cimg1.resize((480, 653))  # 画像を2倍にする例
        cimg_cola = cimg_cola.resize((100, 100))
        cimg_water = cimg_water.resize((100, 100))
        cimg_tea = cimg_tea.resize((100, 100))
        # 画像ファイルのオブジェクトの作成
        self.img1 = ImageTk.PhotoImage(cimg1)
        self.img_cola = ImageTk.PhotoImage(cimg_cola)
        self.img_water = ImageTk.PhotoImage(cimg_water)
        self.img_tea = ImageTk.PhotoImage(cimg_tea)

        # 画像オブジェクトをラベルに貼り付けて表示
        # 自販機の画像
        self.zihanki = tk.Label(self, image=self.img1)
        self.zihanki.place(x=0, y=0)
        
        self.label_ret_coin2 = tk.Label(self, text='円',fg='black', bg='#e5231e', font=('', 20))
        self.label_ret_coin2.place(x=255,y=410)
       
        #  水カウント変数
        self.water_count = 10
        #  コーラカウント変数
        self.cola_count = 10
        #  お茶カウント変数
        self.tea_count = 10
        #  全商品カウント変数
        self.all_count = self.water_count + self.cola_count + self.tea_count
        #  購入カウント変数
        self.buy_count = 0
        # 当たりフラグ
        self.hit_flag = False
        # おつり表示
        self.label_show_retcoin = tk.Label(self, text='', bg='#e5231e', font=('', 20), width=8, fg='white', anchor='e')
        self.label_show_retcoin.place(x=140, y=410)
        

        self.label_ins_coin = tk.Label(self, image=self.img_ins_coin, bg='#e5231e')
        self.label_ins_coin.place(x=297,y=360)

        # おつりラベルたち
        self.label_ret_coin1 = tk.Label(self, text='おつり', fg='black', bg='#e5231e', font=('', 20))
        self.label_ret_coin1.place(x=60, y=410)
        
        self.label_ret_coin2 = tk.Label(self, text='円',fg='black', bg='#e5231e', font=('', 20))
        self.label_ret_coin2.place(x=255,y=410)

        # おつり表示
        self.label_show_retcoin = tk.Label(self, text='', bg='#e5231e', font=('', 20), width=8, fg='white', anchor='e')
        self.label_show_retcoin.place(x=140, y=410)

        # コーラの画像
        self.cola = tk.Label(self, image=self.img_cola)
        self.cola.place(x=55, y=120)
        # お茶の画像
        self.tea = tk.Label(self, image=self.img_tea)
        self.tea.place(x=190, y=120)
        # 水の画像
        self.water = tk.Label(self, image=self.img_water)
        self.water.place(x=320, y=120)

        
        # ラベル
        # 商品が出てくる所
        self.juice_output_label = tk.Label(self, text='', font=('', 25), relief='solid')
        # コーラの値段
        self.cola_price = tk.Label(self, text='160円', font=('',15))
        self.cola_price.place(x=90, y=230)
        # コーラの表記
        self.cola_buy = tk.Label(self, text='コーラ', font=('',15))
        self.cola_buy.place(x=90, y=260)
        self.cola_buy.bind("<Button-1>", self.cola_buy_event)
        # コーラの赤いボタン
        self.cola_buy_btn = tk.Label(self, bg='red', width=2)
        self.cola_buy_btn.place(x=65, y=263)
        # お茶の値段
        self.tea_price = tk.Label(self, text='160円', font=('',15))
        self.tea_price.place(x=230, y=230)
        # お茶の表記
        self.tea_buy = tk.Label(self, text='お茶', font=('',15))
        self.tea_buy.place(x=230, y=260)
        self.tea_buy.bind("<Button-1>", self.tea_buy_event)
        # お茶の赤いボタン
        self.tea_buy_btn = tk.Label(self, bg='red', width=2)
        self.tea_buy_btn.place(x=205, y=263)
        # 水の値段
        self.water_price = tk.Label(self, text='110円', font=('',15))
        self.water_price.place(x=365, y=230)
        # 水の表記
        self.water_buy = tk.Label(self, text='水', font=('',15))
        self.water_buy.place(x=365, y=260)
        self.water_buy.bind("<Button-1>", self.water_buy_event)
        # 水の赤いボタン
        self.water_buy_btn = tk.Label(self, bg='red', width=2)
        self.water_buy_btn.place(x=340, y=263)

# ======= rui
        
        cimg2 = Image.open("./img/5円.png")
        cimg2 = cimg2.resize((40, 40)) 
        self.img2 = ImageTk.PhotoImage(cimg2)
        self.goen = tk.Label(self, image=self.img2, bg='#e5231e')
        self.goen.place(x=30, y=455)
        
        self.goen.bind('<Button-1>', self.goen_click)
                
        
        cimg3 = Image.open("./img/10円.png")
        cimg3 = cimg3.resize((40, 40))  
        self.img3 = ImageTk.PhotoImage(cimg3)
        self.juen = tk.Label(self, image=self.img3, bg='#e5231e')
        self.juen.place(x=80, y=455)
        
        self.juen.bind('<Button-1>', self.juen_click)
        
        cimg4 = Image.open("./img/50円.png")
        cimg4 = cimg4.resize((40, 40))  
        self.img4 = ImageTk.PhotoImage(cimg4)
        self.gojuen = tk.Label(self, image=self.img4, bg='#e5231e')
        self.gojuen.place(x=130, y=455)
        
        self.gojuen.bind('<Button-1>', self.gojuen_click)
        
        
        cimg5 = Image.open("./img/100円.png")
        cimg5 = cimg5.resize((40, 40))  
        self.img5 = ImageTk.PhotoImage(cimg5)
        self.hyakuen = tk.Label(self, image=self.img5, bg='#e5231e')
        self.hyakuen.place(x=180, y=455)
        
        self.hyakuen.bind('<Button-1>', self.hyakuen_click)
        
        
        cimg6 = Image.open("./img/500円.png")
        cimg6 = cimg6.resize((40, 40))  
        self.img6 = ImageTk.PhotoImage(cimg6)
        self.gohyakuen = tk.Label(self, image=self.img6, bg='#e5231e')
        self.gohyakuen.place(x=230, y=455)

        self.gohyakuen.bind('<Button-1>', self.gohyakuen_click)
        
        cimg7 = Image.open("./img/1000円.png")
        cimg7 = cimg7.resize((90, 40))  
        self.img7 = ImageTk.PhotoImage(cimg7)
        self.senen = tk.Label(self, image=self.img7, bg='#e5231e')
        self.senen.place(x=280, y=457)
        
        self.tonyu_label1 = tk.Label(self, text='投  入\n金  額', bg='#e5231e', font=('', 20))
        self.tonyu_label1.place(x=60, y=340)
        
        self.coin_count = 0
        self.tonyu_label2 = tk.Label(self, text=f'{self.coin_count}', bg='black', font=('', 20), width=8, fg='green', anchor='e')
        self.tonyu_label2.place(x=140, y=350)
        
        self.tonyu_label3 = tk.Label(self, text='円', bg='#e5231e', font=('', 20))
        self.tonyu_label3.place(x=255, y=350)
        
        self.label_ins_coin.bind('<Button-1>', self.event_return_coin)

        self.senen.bind('<Button-1>', self.senen_click)

    def event_return_coin(self, event):
        self.label_show_retcoin.configure(text=f'{self.coin_count}')
        self.coin_count = 0
        self.tonyu_label2.configure(text=f'{self.coin_count}')
        if self.coin_count == 0:
                self.cola_buy_btn.configure(bg='red')
                self.tea_buy_btn.configure(bg='red')
                self.water_buy_btn.configure(bg='red')

        
        
        self.tonyu_label1 = tk.Label(self, text='投  入\n金  額', bg='#e5231e', font=('', 20))
        self.tonyu_label1.place(x=60, y=340)
        
        self.coin_count = 0
        self.tonyu_label2 = tk.Label(self, text=f'{self.coin_count}', bg='black', font=('', 20), width=8, fg='green', anchor='e')
        self.tonyu_label2.place(x=140, y=350)
        
        self.tonyu_label3 = tk.Label(self, text='円', bg='#e5231e', font=('', 20))
        self.tonyu_label3.place(x=255, y=350)
        
        if self.coin_count >= 160:
            self.cola_buy_btn.configure(bg='blue')
        
    def goen_click(self, event=None):
        messagebox.showinfo('投入エラー', '5円硬貨は使えません')
        
    def juen_click(self, event=None):
        self.coin_count += 10
        self.tonyu_label2.configure(text=f'{self.coin_count}')
        self.update_coin()
        
    def gojuen_click(self, event=None):
        self.coin_count += 50
        self.tonyu_label2.configure(text=f'{self.coin_count}')
        self.update_coin()
        
        
    def hyakuen_click(self, event=None):
        self.coin_count += 100
        self.tonyu_label2.configure(text=f'{self.coin_count}')
        self.update_coin()
        
    def gohyakuen_click(self, event=None):
        self.coin_count += 500
        self.tonyu_label2.configure(text=f'{self.coin_count}')
        self.update_coin()
        
    def senen_click(self, event=None):
        self.coin_count += 1000
        self.tonyu_label2.configure(text=f'{self.coin_count}')
        self.update_coin()
        
    def update_coin(self):
        if self.coin_count >= 160:
            self.cola_buy_btn.configure(bg='blue')
            self.tea_buy_btn.configure(bg='blue')
            
        if self.coin_count >= 110:
            self.water_buy_btn.configure(bg='blue')
        
        # if self.coin_count >= 3000:
        #     messagebox.showwarning('投入エラー', '3000円以上は投入できません')
            
            
        
    def cola_buy_event(self, event):
            cola_lamp = self.cola_buy_btn.cget('bg')  #ランプの色
            if cola_lamp == 'blue' or self.hit_flag:
                    self.juice_output_label.place(x=180, y=530)     
                    self.juice_output_label.configure(text='コーラ')
                    if self.hit_flag:
                         self.coin_count -= 0
                         self.hit_flag = False
                         self.tea_price.configure(text='160円')
                         self.cola_price.configure(text='160円')
                         self.water_price.configure(text='110円')
                    else:
                         self.coin_count -= 160
                    self.tonyu_label2.configure(text=f'{self.coin_count}')
                    if self.coin_count < 160:
                            self.cola_buy_btn.configure(bg='red')
                            self.tea_buy_btn.configure(bg='red')
                    if self.coin_count < 110:
                            self.water_buy_btn.configure(bg='red')
                    self.winning_func()

    def tea_buy_event(self, event):
            tea_lamp = self.tea_buy_btn.cget('bg')  #ランプの色
            if tea_lamp == 'blue' or self.hit_flag:
                    self.juice_output_label.place(x=180, y=530)     
                    self.juice_output_label.configure(text='お茶')
                    if self.hit_flag:
                         self.coin_count -= 0
                         self.hit_flag = False
                         self.tea_price.configure(text='160円')
                         self.cola_price.configure(text='160円')
                         self.water_price.configure(text='110円')
                    else:
                         self.coin_count -= 160
                    self.tonyu_label2.configure(text=f'{self.coin_count}')
                    if self.coin_count < 160:
                            self.cola_buy_btn.configure(bg='red')
                            self.tea_buy_btn.configure(bg='red')
                    if self.coin_count < 110:
                            self.water_buy_btn.configure(bg='red')
                    self.winning_func()
                    
    
    def water_buy_event(self, event):
            water_lamp = self.water_buy_btn.cget('bg')  #ランプの色
            if water_lamp == 'blue' or self.hit_flag:
                    self.juice_output_label.place(x=180, y=530)     
                    self.juice_output_label.configure(text='水')
                    if self.hit_flag:
                         self.coin_count -= 0
                         self.tea_price.configure(text='160円')
                         self.cola_price.configure(text='160円')
                         self.water_price.configure(text='110円')
                    else:
                         self.coin_count -= 110
                    self.tonyu_label2.configure(text=f'{self.coin_count}')
                    if self.coin_count < 160:
                            self.cola_buy_btn.configure(bg='red')
                            self.tea_buy_btn.configure(bg='red')
                    if self.coin_count < 110:
                            self.water_buy_btn.configure(bg='red')
                    self.winning_func()
                    
        
    # 当たり機能関数
    def winning_func(self):
        self.buy_count += 1
        if self.buy_count % 5 == 0:
            self.buy_count = 0
            random_num = random.randint(0, 1)
            if random_num == 0:
                messagebox.showinfo('当たり', '当たりです！一本無料です！')
                self.hit_flag = True
                self.cola_price.configure(text='無料')
                self.tea_price.configure(text='無料')
                self.water_price.configure(text='無料')
            elif random_num == 1:
                messagebox.showinfo('ハズレ', 'ハズレです！')
        

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
