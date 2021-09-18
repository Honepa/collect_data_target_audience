# 1. Общие положения

## 1.1 Полное наименование системы и ее условное обозначение

1.1.1. Информационнная система сбора информации целевой аудитоии

## 1.2. Наименование организаций заказчика и разработчика

1.2.1. Заказчик Косинцев Роман Игоревич.

1.2.2. Разработчик Духанин Алексей Владиславович.

## 1.3. Порядок оформления и предоставления заказчику результатов работ

Система передается в виде функционирующего комплекса на базе средств вычислительной техники Заказчика. Работы принимаются комиссией, состоящей из представителей Заказчика и Исполнителя. Подписывается акт сдачи-приёмки результата работ.

# 2. Назначения и цели создания системы
## 2.1.  Назначение

Система предназначена для сбора информации данных с сайта "vk.com" в базу данных.

## 2.2. Цели и задачи создания системы

Система создаётся с целью получения инструмента обработки информации данных целевой аудитории Заказчика с сайта "vk.com".

В результате создания Системы должны быть решены следующие задачи:


1. получение координат точек с шагом 500 метров в г. Москва (Россия);
2. проектирование Базы Данных;
3. написание прогрммы сбора данных.



## 3.1. Требования к системе в целом

### 3.1.1. Требования к структуре и функционированию системы

#### 3.1.1.1 Перечень подсистем, их назначение и основные характеристики

В Системе предполагается выделить следующие функциональные модули:
1. модуль программы сборы данных;
2. модуль базы данных.

#### 3.1.1.1 Описание базы данных

Одна таблица. Столбцы:
1) Номер строки ("ID")
2) Координата 1 ("KOOR_X")
3) Координата 2 ("KOOR_Y")
4) Название категории ("CATEGORY_NAME")
5) Ссылка на "vk.com" с текущим названием категории ("LINK")
6) Количество жителей ("COUNT_PERSON")

### 3.2.1. Требования к программному обеспечению системы

При проектировании, разработке и эксплуатации Системы следует использовать следующее программное обеспечение:
1. язык программирования Python 3;
2. VK API;
3. СУБД mysql.

### 3.2.2. Требования к техническому обеспечению

Операционная система Ubuntu, СУБД mysql. 

### 3.2.3. Требования к организационному обеспечению

Требования не предъявляются.

### 3.2.4. Требования к методическому обеспечению

Требования не предъявляются.

# 4. Состав и содержание работ по разработке системы

Основные этапы создания Системы.

1. Техническое задание.

1.1. Согласование технического задания с Заказчиком.

2. Разработка Системы.

2.1. Сбор координат точек с шагом 500 метров.

2.2. Описание базы данных.

2.3. Получение тестовых данных с "VK API".

2.4. Заполнение Базы данных

3. Сдача работы Заказчику


# 5. Требования к документации

Требования не предъявляются.

