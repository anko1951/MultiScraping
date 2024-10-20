import tkinter as tk

# メインウィンドウの作成
root = tk.Tk()
root.title("Scraping Layout")
root.geometry("500x250")

# 列の重みを設定（中央寄せに役立つ）
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# URL入力エリアのラベルと入力フィールド
url_label = tk.Label(root, text="URLを入力してください")
url_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=1, column=0, columnspan=4, padx=10, pady=5)


# ボタン1〜5の配置
btn_width = 10

button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=4, pady=10)

button1 = tk.Button(button_frame, text="Images", width=btn_width)
button1.grid(row=2, column=0, padx=10, pady=(0,10))

button2 = tk.Button(button_frame, text="HTML", width=btn_width)
button2.grid(row=2, column=1, padx=10, pady=(0,10))

button3 = tk.Button(button_frame, text="CSS", width=btn_width)
button3.grid(row=3, column=0, padx=10,)

button4 = tk.Button(button_frame, text="JS", width=btn_width)
button4.grid(row=3, column=1, padx=10,)

button5 = tk.Button(button_frame, text="ALL", width=btn_width)
button5.grid(row=2, column=2, rowspan=2, padx=10, sticky='ns')

# 保存先フォルダのラベルと入力フィールド
folder_label = tk.Label(root, text="保存先フォルダ:")
folder_label.grid(row=4, column=0, padx=10, pady=10, sticky='e')

folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky='w')

# Scrapingボタンの配置
scraping_button = tk.Button(root, text="Scraping!")
scraping_button.grid(row=4, column=3, padx=10, pady=10)

# ウィンドウを表示
root.mainloop()

