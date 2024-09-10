#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: pointer to head pointer
 * @number: number to insert
 * 
 * Return: listint_t* - pointer to the newly inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *prev = NULL;
    listint_t *new;
    listint_t *current;

    current = *head;
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;

    if (current == NULL)
    {
        new->next = NULL;
        *head = new;
        return (new);
    }

    while (current != NULL)
    {
        if (current->n >= number)
        {
            break;
        }

        prev = current;
        current = current->next;
    }

    new->next = current;
    if (prev == NULL)
    {
        *head = new;
    }
    else
    {
        prev->next = new;
    }

    return (new);
}

