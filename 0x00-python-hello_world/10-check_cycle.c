#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: List to check for cycle
 * Return: 0 if no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast != NULL && slow != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
