#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a polindrome
 * @head: first node of the list
 * Return: 0 if not or 1 if it is palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *last;
	int stored_values[100000], cmp = 0, count = 0;

	last = *head;

	if (!last->next)
		return (1);

	while (last->next)
	{
		stored_values[count] = last->n;
		last = last->next;
		count++;
	}
	stored_values[count] = last->n;

	while (count >= 0 && count >= cmp)
	{
		if (stored_values[cmp] != stored_values[count])
			return (0);
		count--;
		cmp++;
	}
	return (1);
}
