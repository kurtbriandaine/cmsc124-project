from lexical_analyzer import *


def typecast():
  pass

#! VARIABLE DECLARATION
def expression():
    lexeme_index = len(line)
    loop_index = 0
    operators = 0
    operands = 0

    if line[0]['lexeme'] == "maek":
      return typecast()

    while loop_index < lexeme_index:
        print(loop_index)
        print(line[loop_index]['lexeme'])

        if line[loop_index]['lexeme'] in arithmetic_operations:
            if loop_index +1 == lexeme_index:
                operands+1
                loop_index+=1
                continue

            if line[loop_index+1]['lexeme'] not in arithmetic_operations and line[loop_index+1]['type'] not in ["FLOAT", "INTEGER", "Variable Identifier"]:
                print("Missing an operand")
                return False
            else:
                operators += 1

        if line[loop_index]['type'] in ["FLOAT", "INTEGER", "Variable Identifier"] and operators>0:
            if loop_index +1 == lexeme_index:
                operands+1
                loop_index+=1
                continue

            if line[loop_index+1]['lexeme'] != "AN":
                print("Expression syntax error")
                return False
            else:
                operands += 1

        if line[loop_index]['lexeme'] == "AN":
            if loop_index +1 == lexeme_index:
                operands+1
                loop_index+=1
                continue

            if line[loop_index+1]['lexeme'] in arithmetic_operations:
                operators += 1
            elif line[loop_index+1]['type'] in ["FLOAT", "INTEGER", "Variable Identifier"]:
                operands += 1
            else:
                print("Expression syntax error")
                return False
        loop_index += 1
    if operands - 1 == operators:
        print("YEHEY")
        return True
    else:
        print("Missing Operand")
        return False

def variable_declaration1():
  try:
    if line[0]['lexeme'] == "I HAS A" and line[1]['type'] == "Variable Identifier" and line[2]['lexeme'] == "ITZ" and line[3]['lexeme'] in ["Integer", "Float", "Variable Identifier", "String Literal"]:
      return True
  except:
    pass

  return False

def variable_declaration2():
  try:
    if line[0]['lexeme'] == "I HAS A" and line[1]['type'] == "Variable Identifier":
      return True
  except:
    pass

  return False

def variable_declaration_error():
  try:
    if line[0]['lexeme'] == "I HAS A":
      print("Syntax Error: Missing variable identifier")
      return True
  except:
    pass

  return False


#! VARIABLE INITIALIZATION 
def variable_initialize():
  try:
    if line[0]['type'] == "Variable Identifier" and line[1]['lexeme'] == "R" and line[2]['type'] in ["Integer", "Float", "Variable Identifier", "String Literal"]:
      return True
  except:
    pass

  return False

def variable_initialize_error1():
  try:
    if line[0]['type'] == "Variable Identifier" and line[1]['type'] in ["Integer", "Float", "Variable Identifier", "String Literal"]:
      print("Syntax Error: Missing 'R' keyword")
      return True
  except:
    pass

  return False

def variable_initialize_error2():
  try:
    if line[0]['type'] == "Variable Identifier" and line[1]['lexeme'] == "R":
      return True
  except:
    pass

  return False

#! USER INPUT
def user_input():
  try:
    if line[0]['lexeme'] == "GIMMEH" and line[1]['type'] == "Variable Identifier":
      return True
  except:
    pass

  return False

def user_input_error():
  try:
    if line[0]['lexeme'] == "GIMMEH":
      print("Syntax Error: Missing variable identifier")
      return True
  except:
    pass

  return False

def statements():
  #! VARIABLE DECLARATION
  if variable_declaration1(): return True
  if variable_declaration2(): return True
  if variable_declaration_error(): return False # will not continue to the loop and will cause error

  #! VARIABLE INITIALIZATION  
  if variable_initialize(): return True
  if variable_initialize_error1(): return False
  if variable_initialize_error2():
    print("Syntax Error: Missing literal, variable, or expression")
    return False

  #! USER INPUT
  if user_input(): return True
  if user_input_error(): return False



arithmetic_operations = ["SUM OF", "DIFF OF", "PRODUKT OF", "QUOSHUNT OF" ,"MOD OF", "BIGGR OF", "SMALLR OF"]
hai_flag = False
bye_flag = False
error_flag = False

line_index = 0
for line in all_table:
  lexeme_index = 0
  line_index += 1
  
  for lexeme in line:
    if lexeme['lexeme'] == "HAI":
      hai_flag = not hai_flag

      if len(line) == 2:
        if line[lexeme_index+1]['type'] not in ["Single Line Comment", "Integer", "Float"]:
          print("Error")

    if lexeme['lexeme'] == "KTHXBYE":
      bye_flag = not bye_flag

    lexeme_index += 1

  # show errors
  if statements() == False:
    error_flag = True
    break
  
  if statements() == True:
    continue
  

  # line_index += 1


if error_flag == False and not (hai_flag and bye_flag):
  print("Syntax Error: Missing HAI or KTHXBYE")

print("Line", line_index)

    # pretty_table.add_row([lexeme['lexeme'], lexeme['type']])