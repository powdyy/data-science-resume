
# GeometryLib 🔺🟠

Библиотека Python для вычисления площади фигур:

- 🔘 Круг по радиусу
- 🔺 Треугольник по трем сторонам, с возможностью проверки на прямоугольность

## Возможности

- Вычисление площади
- Абстрактная и расширяемая архитектура
- Проверка на прямоугольность треугольника
- Юнит-тесты
- Расширение на другие фигуры через фабрику

## Установка

```
pip install .
```

## Использование

```python
from geometry.shapes import ShapeFactory

circle = ShapeFactory.create_shape('circle', 5)
print("Circle Area:", circle.area())

triangle = ShapeFactory.create_shape('triangle', 3, 4, 5)
print("Triangle Area:", triangle.area())
print("Is Right Triangle?", triangle.is_right_triangle())
```

## Тесты

```bash
python -m unittest discover tests
```

## Структура

- `geometry/` — исходный код библиотеки
- `tests/` — модульные тесты

