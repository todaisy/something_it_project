from yandex_neural_api.client import YandexNeuralAPIClient

client = YandexNeuralAPIClient(
    iam_token: str,
    folder_id: str,
    model_type: str = 'pro',
    llm_temperature: float = 0.6,
    llm_max_tokens: int = 1000,
    image_mime_type: str = 'image/png',
    image_width_ratio: int = 1,
    image_height_ratio: int = 1,
    embedding_model: str = 'text-search-doc',
    log_level: int = logging.INFO
)