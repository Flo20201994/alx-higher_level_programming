0. Safe list printing
mandatory
Write a function that prints x elements of a list.

Prototype: def safe print list(my list=[], x=0):
my list can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
x represents the number of elements to print
x can be bigger than the length of my list
Returns the real number of elements printed
You have to use try: / except:
You are not allowed to import any module
You are not allowed to use len()

1. Safe printing of an integers list
mandatory
Write a function that prints an integer with "{:d}".format().

Prototype: def safe print integer(value):
value can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns True if value has been correctly printed (it means the value is an integer)
Otherwise, returns False
You have to use try: / except:
You have to use "{:d}".format() to print as integer
You are not allowed to import any module
You are not allowed to use type()

2. Print and count integers
mandatory
Write a function that prints the first x elements of a list and only integers.

Prototype: def safe print list integers(my list=[], x=0):
my list can contain any type (integer, string, etc.)
All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
x represents the number of elements to access in my list
x can be bigger than the length of my list - if it’s the case, an exception is expected to occur
Returns the real number of integers printed
You have to use try: / except:
You have to use "{:d}".format() to print an integer
You are not allowed to import any module
You are not allowed to use len()

3. Integers division with debug
mandatory
Write a function that divides 2 integers and prints the result.

Prototype: def safe print division(a, b):
You can assume that a and b are integers
The result of the division should print on the finally: section preceded by Inside result:
Returns the value of the division, otherwise: None
You have to use try: / except: / finally:
You have to use "{}".format() to print the result
You are not allowed to import any module

4. Divide a list
mandatory
Write a function that divides element by element 2 lists.

Prototype: def list division(my list 1, my list 2, list length):
my list 1 and my list 2 can contain any type (integer, string, etc.)
list length can be bigger than the length of both lists
Returns a new list (length = list length) with all divisions
If 2 elements can’t be divided, the division result should be equal to 0
If an element is not an integer or float:
print: wrong type
If the division can’t be done (/0):
print: division by 0
If my list 1 or my list 2 is too short
print: out of range
You have to use try: / except: / finally:
You are not allowed to import any module

5. Raise exception
mandatory
Write a function that raises a type exception.

Prototype: def raise exception():
You are not allowed to import any module

6. Raise a message
mandatory
Write a function that raises a name exception with a message.

Prototype: def raise exception msg(message=""):
You are not allowed to import any module

7. Safe integer print with error message
#advanced
Write a function that prints an integer.

Prototype: def safe print integer err(value):
value can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns True if value has been correctly printed (it means the value is an integer)
Otherwise, returns False and prints in stderr the error precede by Exception:
You have to use try: / except:
You have to use "{:d}".format() to print as integer
You are not allowed to use type()

8. Safe function
#advanced
Write a function that executes a function safely.

Prototype: def safe function(fct, *args):
You can assume fct will be always a pointer to a function
Returns the result of the function,
Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
You have to use try: / except:

9. ByteCode -> Python #4
#advanced
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
Tip: Python bytecode

10. CPython #2: PyFloatObject
#advanced
Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.

Python lists:

Prototype: void print_python_list(PyObject *p);
Format: see example
If p is not a valid PyListObject, print an error message (see example)
Python bytes:

Prototype: void print_python_bytes(PyObject *p);
Format: see example
Line “first X bytes”: print a maximum of 10 bytes
If p is not a valid PyBytesObject, print an error message (see example)
Python float:

Prototype: void print_python_float(PyObject *p);
Format: see example
If p is not a valid PyFloatObject, print an error message (see example)
Read /usr/include/python3.4/floatobject.h
About:

Python version: 3.4
You are allowed to use the C standard library
Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
You are not allowed to use the following macros/functions:
Py SIZE
Py TYPE
PyList Size
PyList GetItem
PyBytes AS STRING
PyBytes GET SIZE
PyBytes AsString
PyBytes AsStringAndSize
PyFloat AS DOUBLE
PySequence GetItem
PySequence Fast GET SIZE
PySequence Fast GET ITEM
PySequence ITEM
PySequence Fast ITEMS
NOTE:

The python script will be launched using the -u option (Force stdout to be unbuffered).
It is strongly advised to either use setbuf(stdout, NULL); or fflush(stdout) in your C functions IF you choose to use printf. The reason to that is that Pythonsprintand libCs printf don’t share the same buffer, and the output can appear disordered.
