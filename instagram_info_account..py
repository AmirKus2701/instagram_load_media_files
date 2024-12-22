'''
Этот файл предназначен для того чтобы,
просто узнать статистику аккаунт в
Instagram, просто запускаете программу
ничего не меняете
'''
import instaloader

while True:
    PROFILE_NAME = input("Введите имя пользователя, чтобы просмотреть информацию об этом профиле (или 'выход' для завершения): ")

    if PROFILE_NAME.lower() == 'выход':
        print("Выход из программы.")
        break

    insta = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(insta.context, PROFILE_NAME)

        print()
        print(f"Имя пользователя: {profile.username}")
        print(f"User  ID: {profile.userid}")
        print(f"Кол-во постов: {profile.mediacount}")
        print(f"Кол-во подписчиков: {profile.followers}")
        print(f"Кол-во подписок: {profile.followees}")
        print(f"Описание профиля: {profile.biography}")
        print(f"Внешняя ссылка: {profile.external_url}\n")

    except instaloader.exceptions.ProfileNotExistsException:
        print("Ошибка: Профиль не существует. Пожалуйста, проверьте имя пользователя и попробуйте снова.\n")
    except instaloader.exceptions.ConnectionException:
        print("Ошибка: Проблема с подключением к Instagram. Пожалуйста, проверьте ваше интернет-соединение.\n")
    except Exception as e:
        print(f"Произошла ошибка: {e}\n")

    # Запрос на продолжение или выход
    continue_prompt = input("Хотите просмотреть другой профиль? (да/нет): ")
    if continue_prompt.lower() != 'да':
        break

print("Программа завершена.")