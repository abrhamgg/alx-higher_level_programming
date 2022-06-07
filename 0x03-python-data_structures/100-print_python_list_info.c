#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - prints some info about python lists
 * @p: points to pyobject
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	printf("[*] Size of the Python List = %d\n", PyList_Size(p));
}
