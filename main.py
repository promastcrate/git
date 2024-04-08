import requests

def get_got_quote():
    api_url = 'https://api.gameofthronesquotes.xyz/v1/random'
    response = requests.get(api_url)

    if response.status_code == 200:
        quote_data = response.json()
        character = quote_data['character']
        quote = quote_data['sentence']
        return character, quote
    else:
        return None, None

if __name__ == "__main__":
    character, quote = get_got_quote()

    if character is not None and quote is not None:
        print(f"Случайная цитата из игры Престолов:")
        print(f"Персонаж: {character}")
        print(f"Цитата: {quote}")
    else:
        print("Ошибка при получении данных. Пожалуйста, проверьте подключение к интернету.")
