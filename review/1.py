import tkinter as tk
def myfunc():
    if u.get() == "root" and p.get() == "123":
        r.set("welcome")
root = tk.Tk()
u = tk.StringVar()
p = tk.StringVar()
r = tk.StringVar()
first_frame = tk.Frame(root)
first_frame.pack(pady=10)
user_label = tk.Label(first_frame, text="username")
user_label.pack(side="left")
user_input = tk.Entry(first_frame, textvariable=u)
user_input.pack(side="left")
second_frame = tk.Frame(root)
second_frame.pack()
pass_label = tk.Label(second_frame, text="password")
pass_label.pack(side="left")
pass_input = tk.Entry(second_frame, textvariable=p)
pass_input.pack(side="left")
login_btn = tk.Button(root, text="login", command=myfunc)
login_btn.pack()
output = tk.Label(root, textvariable=r)
output.pack()
root.mainloop()