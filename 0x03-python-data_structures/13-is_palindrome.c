#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if a linked list is a polindrome
 * @head: first node of the list
 * Return: 0 if not or 1 if it is palindrome
 */


int is_palindrome(listint_t **head)
{
	listint_t *last;

	if (!head)
		return (0);

	if (!*head)
		return (1);

	last = *head;

	while (last->next->next)
		last = last->next;
	if (last->next->n != (*head)->n)
		return (0);
	last->next = NULL;

	return (is_palindrome(&((*head)->next)));
}
