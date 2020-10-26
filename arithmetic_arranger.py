max_digits = 4
max_problems = 5
space_between_problems = 4

def has_too_many_problems(problems, max_problems):
  if len(problems) > max_problems:
    return True
  else:
    False

def has_incorrect_operators(split_problem):
  correct_operators = ["+", "-"]
  operator = split_problem[1]

  if operator in correct_operators:
    return False

  else:
    return True

def has_too_many_digits(split_problem, max_digits):
  max_lenght = get_max_length(split_problem)

  if max_lenght > max_digits:
    return True
  
  else:
    return False

def not_number(top_operand, bottom_operand):
  

  if top_operand.isnumeric() and bottom_operand.isnumeric():
    return False

  else:
    return True

def get_problem_elements(split_problem):
  top_operand = split_problem[0]
  operator = split_problem[1]
  bottom_operand = split_problem[2]

  return top_operand, operator, bottom_operand

def get_max_length(split_problem):
  width = 0
  for i in split_problem:
    if len(i) > width:
      width = len(i)
  return width

def get_result(top_operand, operator, bottom_operand):
  if operator == "+":
    result = int(top_operand) + int(bottom_operand)
  
  elif operator == "-":
    result = int(top_operand) - int(bottom_operand)

  return result


def arithmetic_arranger(problems, want_answer = False):
  if has_too_many_problems(problems, max_problems):
    error = "Error: Too many problems."
    return error

  else: 
    top_row = ""
    bottom_row = "\n"
    dashes = "\n"
    results = "\n"

    for problem in problems:
      split_problem = problem.split()

      if has_too_many_digits(split_problem, max_digits):
        error = "Error: Numbers cannot be more than four digits."
        return error

      if has_incorrect_operators(split_problem):
        error = "Error: Operator must be '+' or '-'." 
        return error

      max_lenght = get_max_length(split_problem)

      t_operand, operator, b_operand = get_problem_elements(split_problem)

      if not_number(t_operand, b_operand):
        error = "Error: Numbers must only contain digits."
        return error

      bottom_element = operator + " " + b_operand.rjust(max_lenght)
      width = len(bottom_element)
      top_element = t_operand.rjust(width) 
      top_row += top_element + " "*space_between_problems
      bottom_row += bottom_element + " "*space_between_problems
      dashes += "-"*width + " "*space_between_problems

      if want_answer:
        result = get_result(t_operand, operator, b_operand)
        results += str(result).rjust(width) + space_between_problems*" "
        
    arranged_problems = top_row.rstrip() + bottom_row.rstrip() + dashes.rstrip() + results.rstrip()
    
    return arranged_problems
