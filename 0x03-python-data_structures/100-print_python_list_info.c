#include "Python.h"

/**
 * print_python_list_info - print info about a Python list object
 * @p: pointer to PyObject
 */
void print_python_list_info(PyObject *p)
{
    if (PyList_Check(p))
    {
        PyListObject *list = (PyListObject *)p;
        Py_ssize_t size = PyList_Size(p);
        Py_ssize_t allocated = list->allocated;

        if (size < 0 || allocated < 0)
        {
            printf("Error: Unable to retrieve list information.\n");
            return;
        }

        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", allocated);

        for (Py_ssize_t i = 0; i < size; i++)
        {
            PyObject *element = list->ob_item[i];
            const char *type = Py_TYPE(element)->tp_name;
            printf("Element %ld: %s\n", i, type);
        }
    }
    else
    {
        printf("Error: Input is not a Python list.\n");
    }
}
