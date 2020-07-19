# Insilico Medicine

Задача двоичной классификации для проверки общих навыков работы с данными.

Задание заключается в построении бинарного классификатора на представленном наборе данных. Кроме целевой метрики на тесте, будет оцениваться подход к решению задачи, а также код. Приватной тестовой выборки нет, метрика на публичном тесте является окончательной.

Основные критерии оценки
- Целевая метрика на тестовом множестве (ROC-AUC)
- Полнота анализа данных, использование графиков
- Препроцессинг/постпроцессинг
- Выбор моделей, настройка гиперпараметров, метод валидации
- Использование нейронных сетей
- Общая сложность решения
- Прозрачность и структура кода, комментарии

# Основные решения

Препроцессинг заключался, в исключении значений NaN, +-inf из датасета, путем замены на значения близким к 0 в решение папки (kaggel) и удаление столбцов (если количество NaN больше на 5%, чем строк тренировочного и тестового датасета), а также строк в решение папки (expirement).

В качестве построения нейронной сети, взял модель Keras Sequental API. В Jupiter Notebook, есть раздел, описывающий подбор параметров, размер нейронной сети и количества эпох. При выборе параметров, опирался на статьи, документацию и эксперименты с параметрами, чтобы добиться лучшего значения (время - AUC).

Сообственно в репозитории два решения. Одно решения для тестового задания в Kaggel, второе решение Experiment с другим препроцессингом данных и подбором гиперпараметров. Графики представлены для решения Kaggel.

![ROC curve](https://github.com/VladicNaAmure/Insilico-Medicine/raw/master/images/ROC_Kaggel.png)

При построении ROC curve, параметры предсказания из результатов задания (sample_submission.csv), брался за истинные значения и сравнивался с моими значениями.

# Сравнение моделей для задач бинарной классификации

Сравнение ROC-AUC и F1 score, для разных моделей задач бинарной классификации.

![Сравнение моделей](https://github.com/VladicNaAmure/Insilico-Medicine/raw/master/images/models_kaggel.png)

Визуализация некоторых параметров из истории обучения модели keras.

![accuracy_loss](https://github.com/VladicNaAmure/Insilico-Medicine/raw/master/images/accuracy_loss_Kaggel.png)

![f1_score](https://github.com/VladicNaAmure/Insilico-Medicine/raw/master/images/f1_score_Kaggel.png)

--------------------------
Источники по Docker:
[1] https://www.docker.com
[2] https://www.dmosk.ru/miniinstruktions.php?mini=docker-self-image
[3] https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes
[4] https://medium.com/@andreimaksimov/how-to-run-jupiter-keras-tensorflow-pandas-sklearn-and-matplotlib-in-docker-container-35a49fd4b175
