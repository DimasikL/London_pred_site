import os
import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def load_saved_artifacts(artifacts_dir):
    print("loading saved artifacts...start")

    # Загружаем данные из артефактов
    global __data_columns
    global __locations

    # Путь к файлу с колонками
    columns_path = os.path.join(artifacts_dir, 'columns.json')

    with open(columns_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]  # первые 4 столбца - это sqft, bedroom, bathroom, reception

    global __model
    if __model is None:
        # Путь к модели
        model_path = os.path.join(artifacts_dir, 'london_house__prices_model.pickle')

        with open(model_path, "rb") as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_estimated_price(location, sqft, bedroom, bathroom, reception):
    """
    Рассчитывает стоимость на основе параметров
    """
    try:
        loc_index = __data_columns.index(location.lower())  # Ищем индекс локации
    except:
        loc_index = -1

    # Создаем вектор признаков
    x = np.zeros(len(__data_columns))
    x[0] = sqft  # Площадь
    x[1] = bedroom  # Количество спален
    x[2] = bathroom  # Количество ванных
    x[3] = reception  # Количество приемных комнат

    # Если индекс локации найден, добавляем значение 1 для этой локации
    if loc_index >= 0:
        x[loc_index] = 1

    # Прогнозируем цену
    return round(__model.predict([x])[0], 2)

def get_location_names():
    """
    Возвращает список локаций для выпадающего списка
    """
    return __locations

def get_data_columns():
    """
    Возвращает все доступные колонки для обработки
    """
    return __data_columns
