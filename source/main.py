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


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
