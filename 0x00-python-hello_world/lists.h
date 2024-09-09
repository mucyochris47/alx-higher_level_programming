#ifndef NODE_LISTS_H
#define NODE_LISTS_H

#include <stdlib.h>

/**
 * struct int_list_node - singly linked list node
 * @data: integer value
 * @next_node: pointer to the next node
 *
 * Description: Structure representing a node in a singly linked list.
 */
typedef struct int_list_node
{
    int data;
    struct int_list_node *next_node;
} int_list_node_t;

size_t display_list(const int_list_node_t *start);
int_list_node_t *insert_node_at_start(int_list_node_t **head_ptr, const int value);
void release_list(int_list_node_t *start);
int detect_cycle(int_list_node_t *start);

#endif /* NODE_LISTS_H */

