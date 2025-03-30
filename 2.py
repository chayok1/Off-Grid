import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from tkinter import filedialog

def show_message(message):
    messagebox.showinfo("Інформація", message)

def show_notifications():
    notifications_window = tk.Toplevel(app)
    notifications_window.title("Останні завдання")
    notifications_window.config(bg="#2c3e50")
    notifications_window.geometry("800x400")
    
    title_label = tk.Label(notifications_window, text="Останні завдання", font=("Helvetica", 14, "bold"), bg="#2c3e50", fg="#ecf0f1")
    title_label.pack(pady=10)
    
    tasks = [
        {"task": "Завдання 1: Прочитати 10 сторінок", "time": "2025-03-29 08:00", "button_text": "Прикріпити файл на перевірку"},
        {"task": "Завдання 2: Подивитися подкаст англійською", "time": "2025-03-28 08:00", "button_text": "Пропущено"},
        {"task": "Завдання 3: Написати статтю на 300 слів - Виконано, отримано 10 грідиків", "time": "2025-03-27 08:00", "button_text": "Виконано"}
    ]
    
    for task in tasks:
        task_time = datetime.strptime(task["time"], "%Y-%m-%d %H:%M")
        task_label = tk.Label(notifications_window, text=f"{task['task']} - {task_time.strftime('%H:%M %d-%m-%Y')}", font=("Helvetica", 12), fg="#ecf0f1", bg="#2c3e50")
        task_label.pack(pady=5)

        task_button = tk.Button(notifications_window, text=task["button_text"], command=lambda t=task: handle_task_button(t), bg="#2980b9", fg="white")
        task_button.pack(pady=5)

    close_button = tk.Button(notifications_window, text="Закрити", command=notifications_window.destroy, bg="#e74c3c", fg="white")
    close_button.pack(pady=10)

def handle_task_button(task):
    if task["button_text"] == "Прикріпити файл на перевірку":
        file_path = filedialog.askopenfilename(title="Вибрати файл", filetypes=(("Текстові файли", "*.txt"), ("Всі файли", "*.*")))
        if file_path:
            messagebox.showinfo("Інформація", f"Файл {file_path} додано для перевірки!")
    elif task["button_text"] == "Пропущено":
        show_message("Це завдання пропущено.")
    elif task["button_text"] == "Виконано":
        show_message("Завдання виконано, отримано 10 грідиків!")

def show_profile_window():
    profile_window = tk.Toplevel(app)
    profile_window.title("Профіль")
    profile_window.config(bg="#2c3e50")
    profile_window.geometry("500x300")

    title_label = tk.Label(profile_window, text="Вибір інтересів", font=("Helvetica", 14, "bold"), bg="#2c3e50", fg="#ecf0f1")
    title_label.pack(pady=10)

    interests_label = tk.Label(profile_window, text="Оберіть ваші інтереси:", font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1")
    interests_label.pack(pady=10)

    interests = ["Читання", "Спорт", "Музика", "Технології", "Мандри", "Ігри"]
    selected_interests = {}

    for interest in interests:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(profile_window, text=interest, font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1",
                             variable=var, selectcolor="#2c3e50")
        chk.pack(anchor="w", padx=20)
        selected_interests[interest] = var

    def save_profile():
        chosen_interests = [interest for interest, var in selected_interests.items() if var.get()]
        messagebox.showinfo("Інформація", f"Ви обрали: {', '.join(chosen_interests)}")

    save_button = tk.Button(profile_window, text="Зберегти профіль", font=("Helvetica", 14), fg="white", bg="#2980b9", command=save_profile)
    save_button.pack(pady=20)


app = tk.Tk()
app.title("OffGrid - Формуй корисні звички")
app.geometry("720x750")
app.config(bg="#2c3e50")

header = tk.Label(app, text="OffGrid", font=("Helvetica", 32, "bold"), bg="#2C3E50", fg="white", pady=30)
header.pack(fill="both")

tab_control = ttk.Notebook(app)

tab_about = tk.Frame(tab_control, bg="#2c3e50")
tab_tasks = tk.Frame(tab_control, bg="#2c3e50")
tab_challenges = tk.Frame(tab_control, bg="#2c3e50")
tab_learning = tk.Frame(tab_control, bg="#2c3e50")
tab_content = tk.Frame(tab_control, bg="#2c3e50")
tab_shop = tk.Frame(tab_control, bg="#2c3e50")

tab_control.add(tab_about, text="Про застосунок")
tab_control.add(tab_tasks, text="Завдання")
tab_control.add(tab_challenges, text="Марафони")
tab_control.add(tab_learning, text="Навчання")
tab_control.add(tab_content, text="Контент")
tab_control.add(tab_shop, text="Магазин")

tab_control.pack(expand=1, fill="both")

def create_section_in_tab(tab, title, description, target_tab):
    section_frame = tk.Frame(tab, padx=20, pady=20, relief="flat", bd=0, bg="#34495e", width=500)
    section_frame.pack(padx=20, pady=15, fill="both", expand=True)

    section_title = tk.Label(section_frame, text=title, font=("Helvetica", 20, "bold"), bg="#34495e", fg="white")
    section_title.pack()

    section_desc = tk.Label(section_frame, text=description, font=("Helvetica", 12), bg="#34495e", fg="#ecf0f1", wraplength=440)
    section_desc.pack()

    link_button = tk.Button(tab, text=f"Перейти до вкладки {title}", font=("Helvetica", 14), fg="#2980b9", bg="#34495e", command=lambda: show_message("Soon"))
    link_button.pack(pady=10)

create_section_in_tab(tab_about, "Про застосунок", 
                "OffGrid — це інноваційна гейміфікована програма, яка протидіє відволіканню дофаміну від цифрового вмісту, одночасно сприяючи залученню, концентрації та ефективному навчанню. Ми перетворюємо втрачений час на якісну освіту.", tab_about)
create_section_in_tab(tab_challenges, "Марафони", 
                "Довготривалі челенджі для мотивації. Наприклад, читати кожен день або читати щодня по 30 хвилин.", tab_challenges)
create_section_in_tab(tab_learning, "Навчання", 
                "Віртуальні кімнати для навчання з іншими користувачами, що допомагають підвищити продуктивність.", tab_learning)
create_section_in_tab(tab_content, "Освітній контент", 
                "Цікаві відео та статті для саморозвитку. Заміна бездумного перегляду соцмереж на корисний контент.", tab_content)
create_section_in_tab(tab_shop, "Магазин", 
                "", tab_content)
def add_file_for_review():
    file_path = filedialog.askopenfilename(title="Вибрати файл", filetypes=(("Текстові файли", "*.txt"), ("Всі файли", "*.*")))
    if file_path:
        messagebox.showinfo("Інформація", f"Файл {file_path} додано для перевірки!")
def create_task_section(tab, task_title, task_description, is_completed=False):
    section_frame = tk.Frame(tab, padx=20, pady=20, relief="flat", bd=0, bg="#34495e", width=500)
    section_frame.pack(padx=20, pady=15, fill="both", expand=True)

    section_title = tk.Label(section_frame, text=task_title, font=("Helvetica", 20, "bold"), bg="#34495e", fg="white")
    section_title.pack()

    section_desc = tk.Label(section_frame, text=task_description, font=("Helvetica", 12), bg="#34495e", fg="#ecf0f1", wraplength=440)
    section_desc.pack()

    if is_completed:
        status_label = tk.Label(section_frame, text="Виконано, отримано 10 грідиків", font=("Helvetica", 12, "italic"), bg="#34495e", fg="#2ecc71")
        status_label.pack(pady=5)
    else:
        if task_title == "Завдання 1: Прочитати 10 сторінок":
            add_file_button = tk.Button(section_frame, text="Прикріпити файл на перевірку", font=("Helvetica", 14), fg="white", bg="#2980b9", command=add_file_for_review)
            add_file_button.pack(pady=10)

create_task_section(tab_tasks, "Завдання 1: Прочитати 10 сторінок", "Прочитати 30 сторінок книжки, щоб встигнути закінчити її до літа.")
create_task_section(tab_tasks, "Завдання 2: Подивитися подкаст англійською", "Подивитися подкаст Eliezer Yudkowsky: Dangers of AI and the End of Human Civilization")
create_task_section(tab_tasks, "Завдання 3: Написати статтю на 300 слів", "Написати статтю на 300 слів кожен день для покращення письмових навичок.", is_completed=True)

notification_icon = tk.Label(app, text="🔔", font=("Helvetica", 24), bg="#2c3e50", cursor="hand2")
notification_icon.place(x=500, y=5)

notification_dot = tk.Label(app, text="●", font=("Helvetica", 14), fg="red", bg="#2c3e50")
notification_dot.place(x=520, y=10)

def mark_notifications_as_read():
    notification_dot.place_forget()

notification_icon.bind("<Button-1>", lambda e: [show_notifications(), mark_notifications_as_read()])

profile_button = tk.Button(app, text="Профіль", font=("Helvetica", 14), bg="#2980b9", fg="white", command=show_profile_window)
profile_button.place(x=550, y=10)

footer = tk.Frame(app, bg="#34495e", pady=15)
footer.pack(side="bottom", fill="x")

footer_label = tk.Label(footer, text="© 2025 OffGrid. Всі права захищено.", fg="white", font=("Helvetica", 10), bg="#34495e")
footer_label.pack()

app.mainloop()
