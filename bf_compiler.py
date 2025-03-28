def brainfuck_interpreter(code):
    """Интерпретатор языка Brainfuck."""

    memory = [0]  # Начальная память, состоящая из одного нулевого элемента
    pointer = 0  # Указатель на текущий элемент памяти
    code_index = 0  # Индекс текущей инструкции в коде

    while code_index < len(code):
        instruction = code[code_index]

        if instruction == '>':
            pointer += 1
            if pointer >= len(memory):
                memory.append(0)
        elif instruction == '<':
            pointer -= 1
            if pointer < 0:
                pointer = 0
        elif instruction == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif instruction == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif instruction == '.':
            print(chr(memory[pointer]), end='')
        elif instruction == ',':
            memory[pointer] = ord(input())
        elif instruction == '[':
            if memory[pointer] == 0:
                bracket_count = 1
                while bracket_count > 0:
                    code_index += 1
                    if code[code_index] == '[':
                        bracket_count += 1
                    elif code[code_index] == ']':
                        bracket_count -= 1
        elif instruction == ']':
            if memory[pointer] != 0:
                bracket_count = 1
                while bracket_count > 0:
                    code_index -= 1
                    if code[code_index] == ']':
                        bracket_count += 1
                    elif code[code_index] == '[':
                        bracket_count -= 1
        code_index += 1