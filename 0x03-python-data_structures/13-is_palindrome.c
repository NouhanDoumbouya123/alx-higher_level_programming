#include <stddef.h> /* for NULL definition */
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int values[1000];  /* Assuming the list contains at most 1000 nodes */
	int count = 0;
	int i;

    /* Store the values of each node in an array */
	while (current != NULL)
	{
		values[count] = current->n;
		count++;
		current = current->next;
	}

    /* Check if the values array is a palindrome */
	for (i = 0; i < count / 2; i++)
	{
		if (values[i] != values[count - 1 - i])
			return (0);  /* Not a palindrome */
	}

	return (1);  /* Palindrome */
}
