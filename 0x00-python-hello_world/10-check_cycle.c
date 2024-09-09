#include "lists.h"

/**
 * detect_cycle - function to determine if a singly linked list contains a cycle.
 * @head: Pointer to the start of the singly-linked list.
 *
 * Return: 0 if there is no cycle, 1 if a cycle is detected.
 */
int detect_cycle(listint_t *head)
{
    listint_t *slow_ptr, *fast_ptr;

    if (head == NULL || head->next == NULL)
        return (0);

    slow_ptr = head;
    fast_ptr = head->next;

    while (slow_ptr && fast_ptr && fast_ptr->next)
    {
        if (slow_ptr == fast_ptr)
            return (1);

        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;
    }

    return (0);
}

