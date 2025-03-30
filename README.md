# 🧠 Custom BrainFuck Compiler/Interpreter (Python)

## 📜 Описание
Оптимизирующий компилятор и интерпретатор для языка BrainFuck, написанный на чистом Python. Поддерживает все стандартные инструкции языка с дополнительными оптимизациями.

## 🌟 Ключевые особенности
### 🚀 Основной функционал
- Полная поддержка стандарта BrainFuck (8 операторов)
  
## 📋 Базовые команды

| Команда | Описание                                | Аналог на C          |
|---------|----------------------------------------|----------------------|
| `>`     | Сдвиг указателя вправо                 | `ptr++;`             |
| `<`     | Сдвиг указателя влево                  | `ptr--;`             |
| `+`     | Увеличить значение текущей ячейки на 1 | `(*ptr)++;`          |
| `-`     | Уменьшить значение текущей ячейки на 1 | `(*ptr)--;`          |
| `.`     | Вывести символ из текущей ячейки       | `putchar(*ptr);`     |
| `,`     | Ввести символ в текущую ячейку         | `*ptr = getchar();`  |
| `[`     | Начало цикла (пока *ptr != 0)          | `while (*ptr) {`     |
| `]`     | Конец цикла                            | `}`                  |

## 🔄 Работа с циклами
```brainfuck
[    # Начало цикла
  -  # Уменьшаем значение текущей ячейки
]    # Конец цикла (если *ptr != 0, возврат к [)
```

## 📦 Установка

### Требования
- Python 3.8+
- Не требует дополнительных зависимостей
  
