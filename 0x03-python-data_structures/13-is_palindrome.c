#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - function that checks if a list is palindrome
 * @head: pointer to linked list
 * Return: 0 if not palindrome and 1 if its palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *fast = *head;
	listint_t *new = *head;
	int k  = 0;
	int n = 0;

	if (!*head)
		return (0);
	while (current != NULL)
	{
		current = current->next;
		k++;
		n++;
	}
	int i = 0;
	int count = 0;

	while (new != NULL)
	{
		while (i < k - 1)
		{
			fast = fast->next;
			i++;
		}
		if (count == n / 2)
			return (1);
		if (new->n == fast->n)
		{
			k--;
			new = new->next;
			fast = *head;
			i = 0;
			count = count + 1;
		}
		else
			return (0);
	}
	return (0);
}
