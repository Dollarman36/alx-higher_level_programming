#include "lists.h"

/**
 * check_cycle - functions that checks if a singly linked list
 * has a cycle in it
 * @list: head of the singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{

	listint_t *tortoise = NULL, *hare = NULL;
	int ret = 0;

	tortoise = list;
	hare = list;

	while (tortoise != NULL && hare != NULL)
	{
		if (hare->next != NULL)
			hare = hare->next->next;
		else
			break;
		if (hare == NULL)
			break;
		tortoise = tortoise->next;
		if (tortoise == hare)
		{
			ret = 1;
			break;
		}
	}
	return (ret);
}
