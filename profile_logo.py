import instaloader
import os

# Создаем экземпляр Instaloader
L = instaloader.Instaloader()

# Указываем имя профиля
profile_name = 'kusainov6751'

# Указываем директорию для сохранения
directory = 'profiles_logo'

# Проверяем, существует ли директория, если нет - создаем её
if not os.path.exists(directory):
    os.makedirs(directory)

# Меняем текущую директорию
os.chdir(directory)

try:
    # Загружаем профиль
    L.download_profile(profile_name=profile_name, profile_pic_only=True)

    # Удаляем файлы с расширением .json и .json.xz
    for filename in os.listdir(directory):
        if filename.endswith('.json') or filename.endswith('.json.xz'):
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path)  # Удаляем файл
                print(f"Удалён файл: {file_path}")
            except Exception as e:
                print(f"Ошибка при удалении файла {file_path}: {e}")

    print(f"Профиль {profile_name} успешно загружен в директорию {directory}.")
except Exception as e:
    print("")
