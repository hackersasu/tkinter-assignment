
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

# ... dept_combo.grid ... 바로 아래 추가

# 버튼 클릭 시 실행될 함수
def handle_submit():
    user_name = name_entry.get()
    user_dept = dept_combo.get()

    # 간단하게 터미널에 출력
    print(f"등록 완료: {user_name} ({user_dept})")
    # (시간이 남으면 이 내용을 Label이나 Text 위젯에 표시하도록 수정하면 더 좋습니다)

# "제출" 버튼
submit_button = ttk.Button(main_frame, text="제출", command=handle_submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# ... root.mainloop() ...

# ... root.mainloop() ...

root.mainloop()

