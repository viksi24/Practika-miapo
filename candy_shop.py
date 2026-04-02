import tkinter as tk
from tkinter import messagebox


# Список сладостей хранится прямо внутри программы.
sweets = ["Шоколад", "Мармелад", "Леденцы", "Печенье", "Торт"]


def update_listbox(items=None):
    """Показывает сладости в списке."""
    sweets_listbox.delete(0, tk.END)

    if items is None:
        items = sweets

    for sweet in items:
        sweets_listbox.insert(tk.END, sweet)


def show_all_sweets():
    """Функция 1: показать полный список сладостей."""
    update_listbox()
    search_entry.delete(0, tk.END)


def add_sweet():
    """Функция 2: добавить новую сладость."""
    new_sweet = name_entry.get().strip().title()

    if not new_sweet:
        messagebox.showwarning("Ошибка", "Введите название сладости.")
        return

    sweets.append(new_sweet)
    name_entry.delete(0, tk.END)
    update_listbox()


def find_sweet():
    """Функция 3: найти сладость по названию."""
    query = search_entry.get().strip().lower()

    if not query:
        messagebox.showwarning("Ошибка", "Введите название для поиска.")
        return

    found_items = [sweet for sweet in sweets if query in sweet.lower()]

    if found_items:
        update_listbox(found_items)
    else:
        sweets_listbox.delete(0, tk.END)
        sweets_listbox.insert(tk.END, "Ничего не найдено")


def delete_sweet():
    """Функция 4: удалить выбранную сладость из списка."""
    selected_item = sweets_listbox.curselection()

    if not selected_item:
        messagebox.showwarning("Ошибка", "Выберите сладость в списке.")
        return

    sweet_name = sweets_listbox.get(selected_item[0])

    if sweet_name in sweets:
        sweets.remove(sweet_name)
        update_listbox()


# Создаем главное окно приложения.
window = tk.Tk()
window.title("Магазин сладостей")
window.geometry("560x700")
window.configure(bg="#f4efe8")
window.resizable(False, False)


# Светлая палитра с более сильным контрастом для текста.
bg_color = "#f4efe8"
panel_color = "#fffaf5"
title_color = "#2f1d14"
text_color = "#46332a"
muted_text = "#5f4a3d"
entry_text_color = "#241915"
button_main = "#b85c38"
button_main_active = "#9f4c2c"
button_light = "#ead8c8"
button_light_active = "#dcc4b1"
button_delete = "#d9b8b2"
button_delete_active = "#cda29b"
list_select = "#d99b7a"
border_color = "#ceb9aa"


# Заголовок приложения.
title_label = tk.Label(
    window,
    text="Магазин сладостей",
    font=("Helvetica", 24, "bold"),
    bg=bg_color,
    fg=title_color
)
title_label.pack(pady=(26, 6))


# Короткая подпись делает интерфейс чуть живее, но не перегружает окно.
subtitle_label = tk.Label(
    window,
    text="Добавляйте, ищите и удаляйте сладости в одном окне",
    font=("Helvetica", 12),
    bg=bg_color,
    fg=muted_text
)
subtitle_label.pack(pady=(0, 18))


section_label = tk.Label(
    window,
    text="Управление списком",
    font=("Helvetica", 11, "bold"),
    bg=bg_color,
    fg="#7a5b4a"
)
section_label.pack(pady=(0, 18))


# Поле для добавления сладости.
name_label = tk.Label(
    window,
    text="Название новой сладости:",
    font=("Helvetica", 12, "bold"),
    bg=bg_color,
    fg=text_color
)
name_label.pack(anchor="w", padx=48)

name_entry = tk.Entry(
    window,
    font=("Helvetica", 13),
    width=34,
    bg=panel_color,
    fg=entry_text_color,
    bd=0,
    relief="flat",
    highlightthickness=1,
    highlightbackground=border_color,
    highlightcolor=button_main,
    insertbackground=entry_text_color
)
name_entry.pack(pady=(7, 12), ipady=12)


# Кнопка добавления.
add_button = tk.Button(
    window,
    text="Добавить сладость",
    font=("Helvetica", 12, "bold"),
    bg=button_main,
    fg="#fffaf5",
    activebackground=button_main_active,
    activeforeground="#fffaf5",
    width=26,
    bd=0,
    relief="flat",
    cursor="hand2",
    command=add_sweet
)
add_button.pack(pady=(0, 22), ipady=12)


# Поле для поиска сладости.
search_label = tk.Label(
    window,
    text="Поиск по названию:",
    font=("Helvetica", 12, "bold"),
    bg=bg_color,
    fg=text_color
)
search_label.pack(anchor="w", padx=48)

search_entry = tk.Entry(
    window,
    font=("Helvetica", 13),
    width=34,
    bg=panel_color,
    fg=entry_text_color,
    bd=0,
    relief="flat",
    highlightthickness=1,
    highlightbackground=border_color,
    highlightcolor=button_main,
    insertbackground=entry_text_color
)
search_entry.pack(pady=(7, 14), ipady=12)


# Кнопки просмотра, поиска и удаления.
show_button = tk.Button(
    window,
    text="Показать все",
    font=("Helvetica", 12, "bold"),
    bg=button_light,
    fg="#38271f",
    activebackground=button_light_active,
    activeforeground="#38271f",
    width=26,
    bd=0,
    relief="flat",
    cursor="hand2",
    command=show_all_sweets
)
show_button.pack(pady=6, ipady=11)

find_button = tk.Button(
    window,
    text="Найти сладость",
    font=("Helvetica", 12, "bold"),
    bg=button_light,
    fg="#38271f",
    activebackground=button_light_active,
    activeforeground="#38271f",
    width=26,
    bd=0,
    relief="flat",
    cursor="hand2",
    command=find_sweet
)
find_button.pack(pady=6, ipady=11)

delete_button = tk.Button(
    window,
    text="Удалить выбранную",
    font=("Helvetica", 12, "bold"),
    bg=button_delete,
    fg="#5a342e",
    activebackground=button_delete_active,
    activeforeground="#5a342e",
    width=26,
    bd=0,
    relief="flat",
    cursor="hand2",
    command=delete_sweet
)
delete_button.pack(pady=(6, 24), ipady=11)


# Список сладостей.
sweets_listbox = tk.Listbox(
    window,
    font=("Helvetica", 13),
    width=36,
    height=12,
    bg=panel_color,
    fg=entry_text_color,
    bd=0,
    relief="flat",
    highlightthickness=1,
    highlightbackground=border_color,
    selectbackground=list_select,
    selectforeground="#1d1411",
    activestyle="none"
)
sweets_listbox.pack(pady=(0, 18), ipady=10)


bottom_note = tk.Label(
    window,
    text="Выберите сладость в списке, чтобы удалить ее",
    font=("Helvetica", 11),
    bg=bg_color,
    fg=muted_text
)
bottom_note.pack()


# Сразу показываем стартовый список сладостей.
update_listbox()

print("Feature 3 branch")

# Запуск программы.
window.mainloop()
