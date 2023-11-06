#include "lists.h"
#include <Python.h>
#include <object.h>
#include <listobject.h>
/**
 * print_python_list_infot - prints basic info about pyton lists
 * @p: objet list
 *
 * Return: empty
 */
void print_python_list_info(PyObject *p)
{
	long int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListobjet *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0 ; i < size ; i++)
	{
		printf("Element %d:", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}