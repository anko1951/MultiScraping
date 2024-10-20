import tkinter as tk
from tkinter import filedialog

# メインウィンドウの作成
root = tk.Tk()
root.title("Scraping Layout")
root.geometry("800x600")  # ウィンドウサイズを800x600に設定

# 行と列の重みを設定（各行と列を均等に広げる）
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.grid_rowconfigure(0, weight=1)  # URL入力エリア
root.grid_rowconfigure(1, weight=1)  # URL入力フォーム
root.grid_rowconfigure(2, weight=2)  # ボタン1〜5
root.grid_rowconfigure(3, weight=1)  # 保存先フォルダ
root.grid_rowconfigure(4, weight=1)  # フォルダ入力エリアとScrapingボタン

# URL入力エリアのラベルと入力フィールド
title_label = tk.Label(root, text="Multi Scraping", font=("Bold", 50))
title_label.grid(row=0, column=0, columnspan=4, padx=20, sticky="ew")


url_label = tk.Label(root, text="URL:", font=("Arial", 14))
url_label.grid(row=1, column=0, padx=20, pady=20)


url_entry = tk.Entry(root, width=50, font=("Arial", 14))
url_entry.grid(row=1, column=0, columnspan=4, padx=20, pady=5)

# ボタン1〜5の配置
btn_width = 12  # ボタンの幅を調整
btn_height = 4

button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=4, pady=20,)

# ボタン1〜4を整列
button1 = tk.Button(button_frame, text="Images", width=btn_width, height=btn_height, font=("Arial", 14))
button1.grid(row=0, column=0, padx=20, pady=(0,15), sticky="nsew")

button2 = tk.Button(button_frame, text="HTML", width=btn_width, font=("Arial", 14))
button2.grid(row=0, column=1, padx=20, pady=(0,15), sticky="nsew")

button3 = tk.Button(button_frame, text="CSS", width=btn_width, height=btn_height, font=("Arial", 14))
button3.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")

button4 = tk.Button(button_frame, text="JS", width=btn_width, font=("Arial", 14))
button4.grid(row=1, column=1, padx=20, pady=5, sticky="nsew")

# ボタン5の配置（2行にまたがる）
button5 = tk.Button(button_frame, text="ALL", width=btn_width, font=("Arial", 14))
button5.grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky="nsew")

# 保存先フォルダのラベルとボタン
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

folder_label = tk.Label(root, text="保存先", font=("Arial", 14))
folder_label.grid(row=3, column=0, padx=20, pady=20, sticky='e')

folder_entry = tk.Entry(root, width=50, font=("Arial", 14))
folder_entry.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky='ew')

folder_button = tk.Button(root, text="選択", font=("Arial",14))
folder_button.grid(row=3, column=1,padx=20, pady=10,)

# Scrapingボタンの配置
scraping_button = tk.Button(root, text="Scraping!", width=12, font=("Arial", 14))
scraping_button.grid(row=3, column=3, padx=20, pady=10)

# ウィンドウを表示
root.mainloop()

