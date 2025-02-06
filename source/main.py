import tkinter as tk
from PIL import Image, ImageTk

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
# <<<<<<< dev_kody
        cimg_ins_coin = Image.open("./img/コイン投入口.png")
        # 画像のリサイズ
        cimg1 = cimg1.resize((480, 653))  # 画像を2倍にする例
        cimg_ins_coin = cimg_ins_coin.resize((132, 95))
        # 画像ファイルのオブジェクトの作成
        self.img1 = ImageTk.PhotoImage(cimg1)
        self.img_ins_coin = ImageTk.PhotoImage(cimg_ins_coin)
# =======
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
# >>>>>>> main
        # 画像オブジェクトをラベルに貼り付けて表示
        # 自販機の画像
        self.zihanki = tk.Label(self, image=self.img1)
# <<<<<<< dev_kody
        self.zihanki.place(x=0,y=0)
        
        self.label_ins_coin = tk.Label(self, image=self.img_ins_coin, bg='#e5231e')
        self.label_ins_coin.place(x=297,y=360)
        
        self.label_ret_coin = tk.Label(self, text='おつり　　　　　円', fg='white', bg='#e5231e', font=('', 20))
        self.label_ret_coin.place(x=60, y=420)
=======
        self.zihanki.place(x=0, y=0)
# <<<<<<< dev_yuze
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
        self.juice_output_label.place(x=180, y=530)
        # コーラの表記
        self.cola_buy = tk.Label(self, text='コーラ', font=('',15))
        self.cola_buy.place(x=90, y=230)
        # コーラを買う赤いボタン
        self.cola_buy_btn = tk.Label(self, bg='red', width=2)
        self.cola_buy_btn.place(x=65, y=233)
        # お茶の表記
        self.tea_buy = tk.Label(self, text='お茶', font=('',15))
        self.tea_buy.place(x=230, y=230)
        # お茶を買う赤いボタン
        self.tea_buy_btn = tk.Label(self, bg='red', width=2)
        self.tea_buy_btn.place(x=205, y=233)
        # 水の表記
        self.water_buy = tk.Label(self, text='水', font=('',15))
        self.water_buy.place(x=365, y=230)
        # 水を買う赤いボタン
        self.water_buy_btn = tk.Label(self, bg='red', width=2)
        self.water_buy_btn.place(x=340, y=233)

# ======= rui
        
        cimg2 = Image.open("./img/5円.png")
        cimg2 = cimg2.resize((40, 40)) 
        self.img2 = ImageTk.PhotoImage(cimg2)
        self.goen = tk.Label(self, image=self.img2, bg='#e5231e')
        self.goen.place(x=30, y=455)
        
        cimg3 = Image.open("./img/10円.png")
        cimg3 = cimg3.resize((40, 40))  
        self.img3 = ImageTk.PhotoImage(cimg3)
        self.juen = tk.Label(self, image=self.img3, bg='#e5231e')
        self.juen.place(x=80, y=455)
        
        cimg4 = Image.open("./img/50円.png")
        cimg4 = cimg4.resize((40, 40))  
        self.img4 = ImageTk.PhotoImage(cimg4)
        self.gojuen = tk.Label(self, image=self.img4, bg='#e5231e')
        self.gojuen.place(x=130, y=455)
        
        cimg5 = Image.open("./img/100円.png")
        cimg5 = cimg5.resize((40, 40))  
        self.img5 = ImageTk.PhotoImage(cimg5)
        self.hyakuen = tk.Label(self, image=self.img5, bg='#e5231e')
        self.hyakuen.place(x=180, y=455)
        
        cimg6 = Image.open("./img/500円.png")
        cimg6 = cimg6.resize((40, 40))  
        self.img6 = ImageTk.PhotoImage(cimg6)
        self.goen = tk.Label(self, image=self.img6, bg='#e5231e')
        self.goen.place(x=230, y=455)
        
        cimg7 = Image.open("./img/1000円.png")
        cimg7 = cimg7.resize((90, 40))  
        self.img7 = ImageTk.PhotoImage(cimg7)
        self.senen = tk.Label(self, image=self.img7, bg='#e5231e')
        self.senen.place(x=280, y=457)
        
        self.tonyu_label = tk.Label(self, text='投  入\n金  額', bg='#e5231e', font=('', 20))
        self.tonyu_label.place(x=60, y=340)
        
        self.tonyu_label = tk.Label(self, text='            ', bg='black', font=('', 20))
        self.tonyu_label.place(x=140, y=350)
        
        self.tonyu_label = tk.Label(self, text='円', bg='#e5231e', font=('', 20))
        self.tonyu_label.place(x=250, y=350)
        
        
# >>>>>>> main

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
