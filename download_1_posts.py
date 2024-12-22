from instaloader import Instaloader, Post
import re

def download_post_from_url(url):
    # Извлечение shortcode из полной ссылки
    match = re.search(r'https://www\.instagram\.com/p/([^/]+)/?', url) or re.search(r'https://www\.instagram\.com/reel/([^/]+)/?', url) 
    if match:
        shortcode = match.group(1)
        L = Instaloader()
        
        try:
            # Загрузка поста
            post = Post.from_shortcode(L.context, shortcode)
            L.download_post(post, target='instagram_posts')  # Укажите нужную директорию
            print(f"Пост {shortcode} успешно загружен.\n")
        except Exception as e:
            print(f"Ошибка при загрузке поста: {e}\n")
    else:
        print("Некорректная ссылка.\n")

# Основной цикл программы
while True:
    url = input("Введите ссылку на пост Instagram (или наберите 'exit' для выхода): ")
    
    # keyboard.add_hotkey('ctrl + z', lambda: sys.exit())

    if url.lower() == 'exit':
        print("Выход из программы.")
        break

    download_post_from_url(url) 