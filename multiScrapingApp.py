import tkinter as tk
from tkinter import filedialog,messagebox
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time

# メインウィンドウの作成
root = tk.Tk()
root.title("Multi Scraping")
root.geometry("800x600")  # ウィンドウサイズを800x600に設定

# 行と列の重みを設定（各行と列を均等に広げる）
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.grid_rowconfigure(0, weight=1)  # URL入力エリア
root.grid_rowconfigure(1, weight=1)  # URL入力フォーム
root.grid_rowconfigure(2, weight=2)  # ボタン1〜5
root.grid_rowconfigure(3, weight=1)  # 保存先フォルダ
root.grid_rowconfigure(4, weight=1)  # フォルダ入力エリアとScrapingボタン
root.grid_rowconfigure(5, weight=1)  #プログレスバー

# URL入力エリアのラベルと入力フィールド
title_label = tk.Label(root, text="Multi Scraping", font=("Bold", 50))
title_label.grid(row=0, column=0, columnspan=4, padx=20, sticky="ew")

# URLラベルと入力フォームをFrameでまとめる
url_frame = tk.Frame(root)
url_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=20, sticky="ew")

url_label = tk.Label(url_frame, text="URL:", font=("Arial", 14))
url_label.grid(row=0, column=0, padx=(50,5), sticky="e")

url_entry = tk.Entry(url_frame, width=50, font=("Arial", 14))
url_entry.grid(row=0, column=1, sticky="ew")

#select flag
selected_elements = {"Images": False, "HTML": False, "CSS": False, "JS": False, "ALL": False}

def toggle_button(button,element):
    if selected_elements[element]:
        button.config(bg="SystemButtonFace")
        selected_elements[element] = False
    else:
        button.config(bg="lightblue")
        selected_elements[element] = True

#All_btn
def toggle_all_button(button):
    if selected_elements["ALL"]:
        button.config(bg="SystemButtonFace")
        selected_elements["ALL"] = False
        for btn, elem in buttons.items():
            btn.config(bg="SystemButtonFace")
            selected_elements[elem] = False

    else:
        button.config(bg="lightblue")
        selected_elements["ALL"] = True
        for btn, elem in buttons.items():
            btn.config(bg="lightblue")
            selected_elements[elem] = True

# ボタン1〜5の配置
btn_width = 12  # ボタンの幅を調整
btn_height = 4

button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=4, pady=20)

# ボタン1〜4を整列
button1 = tk.Button(button_frame, text="Images", width=btn_width, height=btn_height, font=("Arial", 14),command=lambda: toggle_button(button1, "Images"))
button1.grid(row=0, column=0, padx=20, pady=(0,15), sticky="nsew")

button2 = tk.Button(button_frame, text="HTML", width=btn_width, font=("Arial", 14),command=lambda: toggle_button(button2, "HTML"))
button2.grid(row=0, column=1, padx=20, pady=(0,15), sticky="nsew")

button3 = tk.Button(button_frame, text="CSS", width=btn_width, height=btn_height, font=("Arial", 14),command=lambda: toggle_button(button3, "CSS"))
button3.grid(row=1, column=0, padx=20, pady=5, sticky="nsew")

button4 = tk.Button(button_frame, text="JS", width=btn_width, font=("Arial", 14),command=lambda: toggle_button(button4, "JS"))
button4.grid(row=1, column=1, padx=20, pady=5, sticky="nsew")

# ボタン5の配置（2行にまたがる）
button5 = tk.Button(button_frame, text="ALL", width=btn_width, font=("Arial", 14),command=lambda: toggle_all_button(button5))
button5.grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky="nsew")

buttons = {button1:"Images", button2: "HTML", button3: "CSS", button4: "JS"}

# 保存先フォルダのラベルとボタン
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

# 保存先フォルダのラベル、エントリ、ボタンをFrameでまとめる
folder_frame = tk.Frame(root)
folder_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=20, sticky="ew")

folder_label = tk.Label(folder_frame, text="保存先:", font=("Arial", 14))
folder_label.grid(row=0, column=0, padx=(50, 5), sticky='e')

folder_entry = tk.Entry(folder_frame, width=40, font=("Arial", 14))
folder_entry.grid(row=0, column=1, columnspan=2, pady=10, sticky='ew')

folder_button = tk.Button(folder_frame, text="選択", font=("Arial", 14), command=select_folder)
folder_button.grid(row=0, column=3, padx=20, pady=10)

# プログレスバーの作成
progress_bar = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
progress_bar.grid(row=5, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

#Scrapingの処理
def scrape():
    url = url_entry.get()
    folder = folder_entry.get()

    if not url or not folder:
        messagebox.showerror("Error","スクレイピング先URLと保存先を設定してください")
        return

    #ボタンで選択された要素を確認
    elements = [key for key, value in selected_elements.items() if value and key != "ALL"]

    if not elements:
        messagebox.showerror("Error","要素を選択してください")
        return

    #スクレイピング実行処理
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text,"html.parser",from_encoding="utf-8")

        total_elements = sum([len(soup.find_all(tag)) for tag in ["img", "link", "script"]])
        progress_bar["maximum"] = total_elements
        progress_bar["value"] = 0

        if "Images" in elements:
            images = soup.find_all("img")
            for img in images:
                img_url = img.get("src")
                if img_url:
                    download_resource(img_url,folder,"Images")
                    progress_bar["value"] += 1
                    root.update_idletasks()
                    time.sleep(1)

        if "HTML" in elements:
            html_content = soup.prettify()
            save_to_file(folder,"HTML",html_content)
            progress_bar["value"] += 1
            root.update_idletasks()
            time.sleep(1)


        if "CSS" in elements:
            css_links = soup.find_all("link",{"rel":"stylesheet"})
            for link in css_links:
                css_url = link.get("href")
                if css_url:
                    full_css_url = urljoin(url, css_url)  # 相対パスを絶対パスに変換
                    download_resource(full_css_url, folder, "CSS")
                    progress_bar["value"] += 1
                    root.update_idletasks()
                    time.sleep(1)

        if "JS" in elements:
            js_scripts = soup.find_all("script",{"src":True})
            for script in js_scripts:
                js_url = script.get("src")
                if js_url:
                    full_js_url = urljoin(url, js_url)  # 相対パスを絶対パスに変換
                    download_resource(full_js_url, folder, "JS")
                    progress_bar["value"] += 1
                    root.update_idletasks()
                    time.sleep(1)

        messagebox.showinfo("Success","スクレイピングが完了しました")

    except requests.RequestException as e:
        messagebox.showerror("Error",f"エラーが発生しました:{e}")

def download_resource(resource_url, folder, file_type):
    full_url = urljoin(url, resource_url)
    
    try:
        response = requests.get(full_url, timeout=10)
        response.raise_for_status()
        
        # リソースを保存
        save_to_file(response.content, folder, file_type, resource_url)
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {resource_url}: {e}")

def save_to_file(folder,file_type,content):
    """
    保存先にファイルを保存する関数。ファイル名はリソースのタイプに応じて動的に決定される。
    """
    if file_type == "HTML":
        file_name = "index.html"  # HTMLの場合はindex.htmlとして保存
        file_path = os.path.join(folder, file_name)
    elif file_type == "CSS" or file_type == "JS":
        # CSSやJSのリソースは元のURLからファイル名を抽出して保存
        file_name = os.path.basename(resource_url)
        file_path = os.path.join(folder, file_name)
    elif file_type == "Images":
        # 画像の場合も元のURLから拡張子を保持したままファイル名を決定
        file_name = os.path.basename(resource_url)
        file_path = os.path.join(folder, file_name)
    else:
        # その他のタイプについては例外を発生させる
        raise ValueError("Unsupported file type for saving")
    
    # ファイルを保存する
    with open(file_path, "wb") as f:
        f.write(content)
    print(f"Saved {file_type} to {file_path}")


# Scrapingボタンの配置
scraping_button = tk.Button(root, text="Scraping!", width=12, font=("Arial", 14), command=scrape)
scraping_button.grid(row=4, column=3, padx=20, pady=10)

# ウィンドウを表示
root.mainloop()

