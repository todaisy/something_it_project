import asyncio
import logging
from yandex_neural_api.client import YandexNeuralAPIClient
import numpy as np
from scipy.spatial.distance import cdist
import json

def main():
    # Настройка логирования
    logging.basicConfig(level=logging.INFO)

    # Инициализация клиента
    client = YandexNeuralAPIClient(
        iam_token="YOUR_IAM_TOKEN",
        folder_id="YOUR_FOLDER_ID",
        model_type='pro',
        llm_temperature=0.7,
        llm_max_tokens=1000,
        log_level=logging.DEBUG
    )

    # Синхронная генерация текста
    print("Синхронная генерация текста:")
    prompt_text_sync = "Напиши короткое стихотворение о программировании."
    text_sync = client.generate_text(prompt_text_sync)
    print(text_sync)
    print("="*50)

    # Асинхронная генерация текста
    async def async_text_generation():
        print("Асинхронная генерация текста:")
        prompt_text_async = "Напиши краткое описание об искусственном интеллекте."
        text_async = await client.generate_text_async(prompt_text_async)
        print(text_async)
        print("="*50)
    asyncio.run(async_text_generation())

    # Синхронная стриминговая генерация текста
    print("Синхронная стриминговая генерация текста:")
    def sync_streaming_callback(data):
        try:
            json_data = json.loads(data)
            text = json_data['result']['alternatives'][0]['message']['text']
            print(text, end='', flush=True)
        except json.JSONDecodeError:
            pass  # Игнорируем некорректные части ответа
        except KeyError:
            pass  # Игнорируем неполные данные

    prompt_stream_sync = "Расскажи интересный факт о Вселенной."
    client.generate_text(prompt_stream_sync, stream=True, callback=sync_streaming_callback)
    print("\n" + "="*50)

    # Асинхронная стриминговая генерация текста
    async def async_streaming():
        print("Асинхронная стриминговая генерация текста:")
        def async_streaming_callback(data):
            try:
                json_data = json.loads(data)
                text = json_data['result']['alternatives'][0]['message']['text']
                print(text, end='', flush=True)
            except json.JSONDecodeError:
                pass
            except KeyError:
                pass

        prompt_stream_async = "Опиши закат над морем."
        await client.generate_text_async(prompt_stream_async, stream=True, callback=async_streaming_callback)
        print("\n" + "="*50)
    asyncio.run(async_streaming())

    # Токенизация текста
    print("Токенизация текста:")
    text_to_tokenize = "Привет, как у тебя дела?"
    tokenization_result = client.tokenize_text(text_to_tokenize)
    print(tokenization_result)
    print("="*50)

    # Получение эмбеддингов
    print("Получение эмбеддингов:")
    doc_texts = [
        "Машинное обучение - это область искусственного интеллекта.",
        "Кошки любят играть с клубками ниток.",
        "Python - это популярный язык программирования."
    ]
    query_text = "Что такое машинное обучение?"

    doc_embeddings = [client.get_text_embedding(text, text_type='doc') for text in doc_texts]
    query_embedding = client.get_text_embedding(query_text, text_type='query')

    doc_embeddings_np = np.array(doc_embeddings)
    query_embedding_np = np.array(query_embedding)

    distances = cdist([query_embedding_np], doc_embeddings_np, metric='cosine')
    similarities = 1 - distances

    most_similar_index = np.argmax(similarities)
    most_similar_doc = doc_texts[most_similar_index]
    similarity_score = similarities[0][most_similar_index]

    print(f"Поисковый запрос: {query_text}")
    print(f"Наиболее похожий документ: {most_similar_doc}")
    print(f"Коэффициент сходства: {similarity_score}")
    print("="*50)

    # Асинхронная генерация изображения
    async def async_image_generation():
        print("Асинхронная генерация изображения:")
        prompt_image = "Нарисуй красивый пейзаж с горами и рекой."
        image_data = await client.generate_image_async(prompt_image)
        with open("generated_image.png", "wb") as f:
            f.write(image_data)
        print("Изображение сохранено как generated_image.png")
    asyncio.run(async_image_generation())

if __name__ == "__main__":
    main()
