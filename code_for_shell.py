from datacenter.models import Schoolkid, Commendation, Lesson
from datacenter.models import Schoolkid, Chastisement
import random
from datacenter.models import Schoolkid, Mark


def fix_marks(schoolkid):
    all_bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    good_mark = 5
    for one_bad_mark in all_bad_marks:
        one_bad_mark.points = good_mark
        one_bad_mark.save()


def remove_chastisements(schoolkid):
    our_kid = Chastisement.objects.filter(schoolkid=schoolkid)
    our_kid.delete()


phrases = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!'
]


def create_commendation(schoolkid_name, subject_title):
    try:
        schoolkid = Schoolkid.objects.get(full_name=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print(f"Ученик '{schoolkid_name}' не найден")
        return
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid_name}'")
        return

    year = schoolkid.year_of_study
    group = schoolkid.group_letter
    lesson = Lesson.objects.filter(
        year_of_study=year, group_letter=group, subject__title=subject_title).order_by('-date').first()

    if not lesson:
        return

    Commendation.objects.create(text=random.choice(
        phrases), created=lesson.date, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher)
