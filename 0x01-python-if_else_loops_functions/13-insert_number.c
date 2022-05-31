#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - function that inserts a node in a given index.
 * @head: pointer to singly linked list
 * @number: position to place the node.
 * Return: pointer to new linked list.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *prev = *head;
	listint_t *temp = *head;
	int pos = 0;
	listint_t *new = malloc(sizeof(listint_t));
	
	if (!new)
		return (NULL);
	new->n = number;
        new->next = NULL;
	if (!current)
	{
		*head = new;
		return(*head);
	}

	if (new->n < current->n)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}

	while (current->n < new->n)
	{
		current = current->next;
		pos++;
		if (pos == 1)
			continue;
		else
			prev = prev->next;
		if (current->next == NULL)
		{
			current->next = new;
			new->next = NULL;
			return (*head);
		}
	}
	temp = prev->next;
	prev->next = new;
	new->next = temp;
	return (*head);
	free(new);
}
