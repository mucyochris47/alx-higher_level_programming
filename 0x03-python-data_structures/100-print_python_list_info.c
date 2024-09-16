#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A PyObject list object
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;
    PyObject *item;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

