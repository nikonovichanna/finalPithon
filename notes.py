import json
import datetime

def load_notes():
    try:
        with open('notes.json', 'r', encoding='utf-8') as file:
            notes = json.load(file)
    except FileNotFoundError: 
        notes = []
    return notes

def save_notes(notes):
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)

def display_notes(notes):
    if not notes:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело заметки: {note['body']}")
            print(f"Дата создания: {note['created_at']}")
            print(f"Дата изменения: {note['updated_at']}")
            print("==============================")

def add_note():
    notes = load_notes()
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'updated_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")

def edit_note():
    notes = load_notes()
    id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            note['title'] = title
            note['body'] = body
            note['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note():
    notes = load_notes()
    id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")

def main_menu():
    while True:
        print("==============================")
        print("1. Вывести список заметок")
        print("2. Добавить новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти из приложения")
        print("==============================")
        choice = input("Введите номер действия: ")
        if choice == '1':
            notes = load_notes()
            display_notes(notes)
        elif choice == '2':
            add_note()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Некорректный выбор.")
            
if __name__ == "__main__":
    main_menu()
