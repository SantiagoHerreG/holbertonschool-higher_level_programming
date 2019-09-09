#include "lists.h"

/**
 * check_cycle - checks if a single list has a cycle into it
 * @list: pointer to the beginning of the list
 * Return: 0 if not, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp, *current;

	temp = list;

	if (!list)
		return (0);

	current = temp;

	while (temp->next)
	{
		if (temp->next == list)
			return (1);
		temp = temp->next;
		if (current->next && current->next->next)
			current = current->next->next;
		if (temp == current)
			break;
	}

	if (!temp->next)
		return (0);
	else
		return (check_cycle(list->next));
}
