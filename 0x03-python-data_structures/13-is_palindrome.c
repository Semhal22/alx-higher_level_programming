#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of list
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *next = NULL;
	int result = 1;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	while (slow != NULL)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	while (prev != NULL && *head != NULL)
	{
		if (prev->n != (*head)->n)
		{
			result = 0;
			break;
		}
		prev = prev->next;
		*head = (*head)->next;
	}
	return (result);
}
