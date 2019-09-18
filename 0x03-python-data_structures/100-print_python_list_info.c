#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints the basic info of a python object
 * @p: python list
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size_obj, index;
	PyObject *type;


	size_obj = PyList_Size(p);


	printf("[*] Size of the Python List = %li\n", size_obj);
	printf("[*] Allocated = %li\n", Py_SIZE(p));

	for (index = 0; index < size_obj; index++)
	{
		type = PyList_GetItem(p, index);
		if (*((char *)Py_TYPE(type)) == 'C')
			printf("Element %li: int\n", index);
		if (*((char *)Py_TYPE(type)) == 'I')
			printf("Element %li: str\n", index);
		if (*((char *)Py_TYPE(type)) == '\'')
			printf("Element %li: list\n", index);
		if (*((char *)Py_TYPE(type)) == '3')
			printf("Element %li: float\n", index);
		if (*((char *)Py_TYPE(type)) == '9')
			printf("Element %li: tuple\n", index);
	}
}
