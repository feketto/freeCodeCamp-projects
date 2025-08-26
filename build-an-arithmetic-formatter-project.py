def arithmetic_arranger(problems, show_answers=False):
    numof_problems = ''
    if len(problems) > 5:
        numof_problems = 'Error: Too many problems.'
        return numof_problems

    arranged = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    signs_not_valid = "Error: Operator must be '+' or '-'."
    numbers_not_valid = 'Error: Numbers must only contain digits.'
    length_not_valid = 'Error: Numbers cannot be more than four digits.'


    for problem in problems:
        num1, sign, num2 = problem.split()
        if sign not in ['+', '-']:
            return signs_not_valid
        if not num1.isdigit() or not num2.isdigit():
            return numbers_not_valid
        if len(num1)>4 or len(num2)>4:
            return length_not_valid
        width = max(len(num1), len(num2)) + 2

        line1 += num1.rjust(width) + '    '
        line2 += sign + num2.rjust(width - 1) + '    '
        line3 += ('-' * width) + '    '

        result = str(int(num1) + int(num2) if sign == '+' else int(num1) - int(num2))
        line4 += result.rjust(width) + '    '

    if show_answers is False:
        arranged = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip()
    elif show_answers is True:
        arranged = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip() + '\n' + line4.rstrip()
    
    return arranged

print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
