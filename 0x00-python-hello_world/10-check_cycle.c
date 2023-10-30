#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * _strncat - Concatenates two strings, using at most n bytes from src.
 * @dest: Destination string.
 * @src: Source string.
 * @n: Maximum number of bytes from src.
 *
 * Return: 1 if cyclical. 0 otherwise.
 */
 int chech_cycle(listint_t *list)
 {
 listint_t *slow = list, *fast = list;
 while (fast && fast->next)
 {
 slow = slow->next;
 fast = fast->next->next;
 if(slow == fast)
 return (1);
 }
 return (0);
 }
