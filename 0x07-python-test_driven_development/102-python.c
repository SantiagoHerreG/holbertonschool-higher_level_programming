#include <Python.h>
#include <stdio.h>
#include <listobject.h>
#include <object.h>
#include <floatobject.h>
/**
 * print_python_string - prints info about python strings
 * @p: python object
 * Return: void
 */

void print_python_string(PyObject *p)
{
	Py_ssize_t length;
	int type;
	void *data;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);
	printf("  length: %li\n", length);

	type = PyUnicode_KIND(p);
	if (type == 1)
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	data = PyUnicode_DATA(p);
	printf("  value: %s\n", (char *)data);
	/*PyUnicode_AsUTF8String(PyObject *unicode)*/
}
