#include <Python.h>

/**
 * print_python_list_info - Prints basic python list information.
 * @p: The individual object
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t id;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t n = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", n);

	for (id = 0; id < size; id++)
	{
		printf("Element %li: %s\n", id, (Py_TYPE(PyList_GetItem(p, id)))->tp_name);
	}
}
