# Скрипты для работы с электронным дневником

Этот репозиторий содержит скрипты для автоматизации работы с электронным дневником школы.

## Скрипты для работы с дневником

В файле ```code_for_shell.py``` находятся функции для автоматической работы с дневником:

1. ```fix_marks(schoolkid)``` - исправляет плохие оценки (2 и 3) на 5
2. ```remove_chastisements(schoolkid)``` - удаляет все замечания ученика
3. ```create_commendation(schoolkid_name, subject_title)``` - создаёт похвалу от учителя

## Способы запуска:

### Способ 1: Импорт (рекомендуется)
Поместите `code_for_shell.py` рядом с `manage.py`, затем импортируйте функции в Django shell.

### Способ 2: Копирование в shell
Скопируйте весь код из `code_for_shell.py` и вставьте в Django shell.

## Как использовать

### 1. Клонируйте репозиторий
```bash
git clone <ваш-репозиторий>
cd e-diary
```
### 2. Создайте виртуальное окружение
```bash
python -m venv venv
```
Активация:
```bash
venv\Scripts\activate
```
### 3. Установите зависимости
```bash
pip install -r requirements.txt
```
### 4. Создайте .env файл
Создайте файл .env рядом с manage.py и добавьте:
```text
DEBUG=True
SECRET_KEY=ваш_секретный_ключ
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_NAME=schoolbase.sqlite3
```
### 5. Запустите Django shell
```bash
python manage.py shell
```
### 6. Импортируйте функции
```python
from code_for_shell import fix_marks, remove_chastisements, create_commendation
```
## Пример использования
```python
# Сначала найдите ученика
from datacenter.models import Schoolkid
schoolkid = Schoolkid.objects.get(full_name="Фролов Иван", year_of_study=10, group_letter="А")


# Исправить оценки
fix_marks(schoolkid)

# Удалить замечания
remove_chastisements(schoolkid)

# Создать похвалу
create_commendation("Фролов Иван", "Математика")
```