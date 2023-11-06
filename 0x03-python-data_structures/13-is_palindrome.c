#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - Concatenates two strings, using at most n bytes from src.
 * @head: head of list.
 *
 * Return: 0 is not 1.
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (pal_ind(head, *head));
}
/**
 * pal_ind - function to know if is palindrome
 * @head: head og list.
 * @end: end of list.
 *
 * Return: int.
 */
int pal_ind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (pal_ind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
