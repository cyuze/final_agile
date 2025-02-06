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
        # 画像のリサイズ
        cimg1 = cimg1.resize((480, 653))  # 画像を2倍にする例
        # 画像ファイルのオブジェクトの作成
        self.img1 = ImageTk.PhotoImage(cimg1)
        # 画像オブジェクトをラベルに貼り付けて表示
        self.zihanki = tk.Label(self, image=self.img1)
        self.zihanki.place(x=0, y=0)
        
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
        
        
        

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
