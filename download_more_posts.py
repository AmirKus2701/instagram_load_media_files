from instaloader import Instaloader, Post
import re, logging, os
from concurrent.futures import ThreadPoolExecutor

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

os.chdir('instagram_posts')

def download_post_from_url(url):
    # Извлечение shortcode из полной ссылки
    match = re.search(r'https://www\.instagram\.com/(?:p|reel)/([^/]+)/?', url)
    if match:
        shortcode = match.group(1)
        L = Instaloader()
        
        try:
            # Загрузка поста
            post = Post.from_shortcode(L.context, shortcode)
            username = post.owner_username  # Получаем имя пользователя
            post_number = post.mediaid  # Используем mediaid как уникальный идентификатор поста
            
            # Создание директории для поста
            user_post_folder = f'{username}_post_{post_number}'
            
            # Загрузка поста в созданную папку
            L.download_post(post, target=user_post_folder)  # Укажите нужную директорию
            
            logging.info(f"Пост {shortcode} успешно загружен в {user_post_folder}.\n")
        except Exception as e:
            logging.error(f"Ошибка при загрузке поста {shortcode}: {e}\n")
    else:
        logging.warning(f"Некорректная ссылка: {url}\n")

def main():
    # Основной цикл программы
    while True:
        urls = input("Введите ссылки на посты Instagram, разделенные пробелом (или наберите 'exit' для выхода): ")
        
        if urls.lower() == 'exit':
            logging.info("Выход из программы.")
            break

        # Разделение введенных ссылок по пробелу
        url_list = urls.split()
        
        # Использование пула потоков для загрузки постов
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(download_post_from_url, url_list)

if __name__ == "__main__":
    main()