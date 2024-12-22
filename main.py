import instaloader
import os
import json

L = instaloader.Instaloader()

# Получаем имя пользователя
profile_name = "repair_auto"


profile = instaloader.Profile.from_username(L.context, profile_name)

os.chdir("instagram_profiles")
# Создаем основную папку с именем пользователя
user_folder = os.path.join(os.getcwd(), profile_name)
os.makedirs(user_folder, exist_ok=True)

# Меняем текущую рабочую директорию на папку пользователя
os.chdir(user_folder)

# Файл для хранения информации о загруженных публикациях
data_file = f"{profile_name}_posts.json"

# Загружаем существующие данные, если файл существует
if os.path.exists(data_file):
    with open(data_file, "r") as f:
        existing_posts = json.load(f)
else:
    existing_posts = []

# Список для новых публикаций
new_posts = []

# Счетчик для отслеживания количества загруженных постов
count = 0


def download_posts():
    global count
    for post in profile.get_posts():

        if count < 10000000:
            # Проверяем, есть ли уже этот пост
            if post.mediaid not in existing_posts:
                # Формируем имя файла с номером публикации и датой
                post_file_name = (
                    f"post_{count + 1}_{post.date_utc.strftime('%d_%m_%Y')}.jpg"
                )

                # Сохраняем пост с корректным именем файла
                L.download_post(post, target=post_file_name)

                # Добавляем идентификатор поста в список новых постов
                new_posts.append(post.mediaid)
                count += 1
            else:
                print(f"Публикация {post.mediaid} уже загружена.")
        else:
            break

    # Если есть новые публикации, обновляем файл
    if new_posts:
        existing_posts.extend(new_posts)
        with open(data_file, "w") as f:
            json.dump(existing_posts, f)
        print(f"Загружено новых публикаций: {len(new_posts)}")
    else:
        print("Новых публикаций не найдено.")


# Запуск основной функции
download_posts()
