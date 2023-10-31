#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Insert a node with a number into a sorted linked list.
 * @head: Pointer to the head of the list.
 * @number: The number to add to the list.
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!head || !new_node)
	{
		new_node->n = number;
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}

	new_node->n = number;
	if (number <= (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	node = *head;
	while (node)
	{
		if (!node->next)
		{
			return (add_nodeint_end(head, number));
		}

		if (number > node->n && number <= (node->next)->n)
		{
			new_node->next = node->next;
			node->next = new_node;
			return (new_node);
		}

		node = node->next;
	}
	free(new_node);
	return (NULL);
}

