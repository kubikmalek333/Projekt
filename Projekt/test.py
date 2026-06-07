import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"


# načtení tasku

def load_tasks():

    if os.path.exists(FILE_NAME):

        try:
            f = open(FILE_NAME, "r", encoding="utf-8")
            data = json.load(f)
            f.close()

            for t in data:
                if "done" not in t:
                    t["done"] = False
                if "time" not in t:
                    t["time"] = "bez termínu"

            return data

        except:
            return []

    return []

# uložení tasku

def save_tasks():

    f = open(FILE_NAME, "w", encoding="utf-8")
    json.dump(tasks, f, ensure_ascii=False, indent=4)
    f.close()


# refresh list

def refresh():

    listbox.delete(0, tk.END)

    done_count = 0

    for t in tasks:

        text = t["text"] + " | " + t["time"]

        if t["done"]:
            text += " ✔"
            done_count += 1

        listbox.insert(tk.END, text)

    counter.config(text=f"Hotové: {done_count} / {len(tasks)}")


# přidání tasku

def add_task():

    text = entry.get()
    time = time_entry.get()

    if text != "" and time != "":

        tasks.append({
            "text": text,
            "time": time,
            "done": False
        })

        entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)

        save_tasks()
        refresh()

    else:
        messagebox.showwarning("Chyba", "Zadej úkol i čas")


# smazání tasku

def delete_task():

    try:
        i = listbox.curselection()[0]
        tasks.pop(i)

        save_tasks()
        refresh()

    except:
        messagebox.showwarning("Chyba", "Nic není vybrané")


# za fajfkování

def toggle_done():

    try:
        i = listbox.curselection()[0]
        tasks[i]["done"] = not tasks[i]["done"]

        save_tasks()
        refresh()

    except:
        messagebox.showwarning("Chyba", "Vyber úkol")


# smazání všech tasků

def clear_all():

    if messagebox.askyesno("Otázka", "Smazat všechny úkoly?"):

        tasks.clear()
        save_tasks()
        refresh()


# Dark Mode

BG = "#1e1e1e"
FG = "white"
ENTRY_BG = "#2d2d2d"
BTN_BG = "#333333"
LIST_BG = "#2d2d2d"


# window

root = tk.Tk()
root.title("Úkolníček")
root.geometry("650x600")
root.configure(bg=BG)
root.resizable(False, False)

tasks = load_tasks()


# UI TEXT

title = tk.Label(root, text="Moje úkoly", font=("Arial", 20, "bold"), bg=BG, fg=FG)
title.pack(pady=10)

label = tk.Label(root, text="Úkol:", bg=BG, fg=FG)
label.pack()

entry = tk.Entry(root, width=40, bg=ENTRY_BG, fg=FG, insertbackground=FG, relief="flat")
entry.pack(pady=5)

time_label = tk.Label(root, text="Čas / termín:", bg=BG, fg=FG)
time_label.pack()

time_entry = tk.Entry(root, width=40, bg=ENTRY_BG, fg=FG, insertbackground=FG, relief="flat")
time_entry.pack(pady=5)


# BUTTONS (2 vedle sebe)

row1 = tk.Frame(root, bg=BG)
row1.pack(pady=3)

btn_add = tk.Button(row1, text="Přidat", width=20, bg=BTN_BG, fg=FG, command=add_task)
btn_add.pack(side="left", padx=5)

btn_done = tk.Button(row1, text="Hotovo / Nehotovo", width=20, bg=BTN_BG, fg=FG, command=toggle_done)
btn_done.pack(side="left", padx=5)

row2 = tk.Frame(root, bg=BG)
row2.pack(pady=3)

btn_del = tk.Button(row2, text="Smazat", width=20, bg=BTN_BG, fg=FG, command=delete_task)
btn_del.pack(side="left", padx=5)

btn_clear = tk.Button(row2, text="Vymazat vše", width=20, bg=BTN_BG, fg=FG, command=clear_all)
btn_clear.pack(side="left", padx=5)

# counter

counter = tk.Label(root, text="Hotové: 0 / 0", bg=BG, fg=FG)
counter.pack(pady=5)


# listbox

listbox = tk.Listbox(
    root,
    width=70,
    height=15,
    font=("Arial", 12),
    bg=LIST_BG,
    fg=FG,
    selectbackground="#444444",
    highlightthickness=0,
    relief="flat"
)
listbox.pack(pady=10)


# start

refresh()
root.mainloop()