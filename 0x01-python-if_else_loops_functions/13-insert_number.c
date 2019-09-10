#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a node in a sorted linked list
 * @head: pointer to the beginning of the list
 * @number: number to add
 * Return: pointer to the new node, or null if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	if (!head || !*head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if ((*head)->next == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next)
	{
		if (current->next->n < number)
			current = current->next;
		else
		{
			new_node->next = current->next;
			current->next = new_node;
			break;
		}
	}
	return (new_node);
}
