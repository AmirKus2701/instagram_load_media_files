import instaloader
import os
from loguru import logger

# Создаем экземпляр Instaloader
L = instaloader.Instaloader()

# Отключаем логирование для instaloader с помощью loguru

# Указываем директорию для сохранения
directory = 'profiles_logo'

# Проверяем, существует ли директория, если нет - создаем её
if not os.path.exists(directory):
    os.makedirs(directory)

# Меняем текущую директорию
try:
    os.chdir(directory)
except Exception as e:
    logger.error(f"Ошибка при изменении директории: {e}")
    exit(1)

while True:
    # Указываем имя профиля
    profile_name = input("Введите имя пользователя, чтобы просмотреть информацию об этом профиле (или 'выход' для завершения): ")

    if profile_name.lower() == 'выход':
        print("Выход из программы.")
        break

    try:
        # Загружаем профиль
        L.download_profile(profile_name=profile_name, profile_pic_only=True)

        # Удаляем файлы с расширением .json и .json.xz
        for filename in os.listdir('.'):
            if filename.endswith('.json') or filename.endswith('.json.xz'):
                try:
                    os.remove(filename)  # Удаляем файл
                    print(f"Удалён файл: {filename}")
                except Exception as e:
                    print(f"Ошибка при удалении файла {filename}: {e}")

        logger.debug(f"Профиль {profile_name} успешно загружен в директорию {directory}.\n")
    except instaloader.ProfileNotExistsException:
        logger.error(f"Профиль '{profile_name}' не существует. Пожалуйста, проверьте имя пользователя.\n")
    except Exception as e:
        logger.critical(f"Произошла ошибка при загрузке профиля {profile_name}: {e}\n")
