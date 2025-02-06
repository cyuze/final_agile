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
        cimg_ins_coin = Image.open("./img/コイン投入口.png")
        # 画像のリサイズ
        cimg1 = cimg1.resize((480, 653))  # 画像を2倍にする例
        cimg_ins_coin = cimg_ins_coin.resize((132, 95))
        # 画像ファイルのオブジェクトの作成
        self.img1 = ImageTk.PhotoImage(cimg1)
        self.img_ins_coin = ImageTk.PhotoImage(cimg_ins_coin)
        # 画像オブジェクトをラベルに貼り付けて表示
        self.zihanki = tk.Label(self, image=self.img1)
        self.zihanki.place(x=0,y=0)
        
        self.label_ins_coin = tk.Label(self, image=self.img_ins_coin, bg='#e5231e')
        self.label_ins_coin.place(x=297,y=360)
        
        self.label_ret_coin = tk.Label(self, text='おつり　　　　　円', fg='white', bg='#e5231e', font=('', 20))
        self.label_ret_coin.place(x=60, y=420)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
