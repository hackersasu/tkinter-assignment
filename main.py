
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My Tkinter App")
root.geometry("400x300")
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0) 

# "이름" 레이블
ttk.Label(main_frame, text="이름:").grid(row=0, column=0, sticky="w")

# "이름" 입력창
name_entry = ttk.Entry(main_frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

# ... name_entry.grid ... 바로 아래 추가

# "부서" 레이블
ttk.Label(main_frame, text="부서:").grid(row=1, column=0, sticky="w")

# "부서" 콤보박스
departments = ["Engineering", "Sales", "Marketing", "HR"]
dept_combo = ttk.Combobox(main_frame, values=departments, width=27)
dept_combo.grid(row=1, column=1, pady=5)

# ... root.mainloop() ...

root.mainloop()

