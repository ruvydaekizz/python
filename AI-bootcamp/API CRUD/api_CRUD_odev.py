from requests import get
from pprint import pprint


# API'ye request'te bulunalım. API bize response döndürecek.
endpoint = 'https://newsapi.org/v2/everything?q=apple&from=2025-02-27&to=2025-02-27&sortBy=popularity&apiKey=89dd9aa7cff74e17b11768cef97bbb23'
response = get(url=endpoint)              # API'ye gidip talepte bulunacak

data = response.json()              # response'u yani datayı -->  json'a dönüştürme işlemi
pprint(data)


# CREATE
def create_article_element(article_index: int, key: str, value: str):
    """
    API'den çekilen bir makaleye yeni bir eleman ekler.

    :param article_index: Güncellenecek makalenin sırası (0,1,2,...)
    :param key: Yeni eklenecek anahtar (örneğin 'example')
    :param value: Yeni eklenecek değeri (örneğin 'zzzzzzzzzzz')
    """
    try:
        data['articles'][article_index][key] = value
        return data['articles'][article_index]                # Güncellenen makaleyi döndür
    except IndexError:
        return "Hata: Belirtilen index'te bir makale bulunamadı!"

# READ
# Kullanıcıdan yazar ismini ve yayınlama bilgisini alalım - searching

def read_articles():
    author_name = input("Author Name: ")
    for article in data.get('articles', []):
        if article.get('author') == author_name:
            pprint(article)

    published = input("PublishedAt: ")
    for article in data.get('articles', []):
        if article.get('publishedAt') == published:
            pprint(article)


# UPDATE
def update_article_element(article_index: int, key: str, new_value: str):
    try:
        if key in data['articles'][article_index]:  # Eğer key varsa güncelle
            data['articles'][article_index][key] = new_value
            return data['articles'][article_index]  # Güncellenmiş makaleyi döndür
        else:
            return f"Hata: '{key}' adlı anahtar bu makalede bulunamadı!"
    except IndexError:
        return "Hata: Belirtilen index'te bir makale bulunamadı!"

# DELETE
def delete_article_element(article_index: int, key: str):
    try:
        if key in data['articles'][article_index]:  # Eğer key varsa sil
            del data['articles'][article_index][key]
            return data['articles'][article_index]  # Güncellenmiş makaleyi döndür
        else:
            return f"Hata: '{key}' adlı anahtar bu makalede bulunamadı!"
    except IndexError:
        return "Hata: Belirtilen index'te bir makale bulunamadı!"


while True:
    process = input('Yapmak istediğiniz işlemi giriniz (create, read, update, delete, exit): ')

    match process:
        case 'create':
            index = int(input("Hangi makaleye ekleme yapmak istiyorsun? (0,1,2...): "))
            key = input("Eklemek istediğin anahtar adını gir (örneğin 'example'): ")
            value = input("Bu anahtarın değerini gir: ")
            pprint(create_article_element(index, key, value))  # Güncellenmiş makaleyi göster

        case 'read':
            read_articles()

        case 'update':
            index = int(input("Hangi makaledeki değeri güncellemek istiyorsun? (0,1,2...): "))
            key = input("Güncellemek istediğin anahtar adını gir (örneğin 'example'): ")
            new_value = input("Yeni değeri gir: ")
            pprint(update_article_element(index, key, new_value))

        case 'delete':
            index = int(input("Hangi makaleden bir eleman silmek istiyorsun? (0,1,2...): "))
            key = input("Silmek istediğin anahtar adını gir (örneğin 'example'): ")
            pprint(delete_article_element(index, key))

        case 'exit':
            print("Programdan çıkılıyor...")
            break

        case _:
            print('Lütfen geçerli bir işlem girin! (create, read, update, delete, exit)')
