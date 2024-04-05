#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
*insert_node - inserts a number into a sorted singly linked list.
*@head: head
*@number: int
*
*Return: new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *node = NULL;

	if (head == NULL)
		return (NULL);

	node = malloc(sizeof(listint_t *));
	if (node == NULL)
		return (NULL);
	node->next = NULL;
	node->n = number;

	tmp = *head;
	while (tmp)
	{
		if (tmp->n >= number)
		{
			node->next = tmp;
			*head = node;
			return (node);
		}
		else if (tmp->n <= number && tmp->next->n >= number)
		{
			if (tmp->next != NULL)
			{
				node->next = tmp->next;
				tmp->next = node;
				return (node);
			}
		}
		tmp = tmp->next;
	}
	return (NULL);
}
