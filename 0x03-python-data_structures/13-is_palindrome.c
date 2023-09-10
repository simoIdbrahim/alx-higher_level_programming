#include "lists"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - function one.
 * @head: pointer arg.
 * Return: reversed pointer.
 */

listint_t *reverse_listint(listint_t **head)
{
	  listint_t *node = *head, *next, *prev = NULL;

    for (; node; node = next)
    {
        next = node->next;
        node->next = prev;
        prev = node;
    }

    *head = prev;
    return (*head);
}

/**
 * is_palindrome - function two
 * @head: pointer arg
 * Return: int
 */

int is_palindrome(listint_t **head)
{
    listint_t *tmp, *rev, *mid;
    size_t s = 0, i;

    if (*head == NULL || (*head)->next == NULL)
    {
        return (1);
    }

    tmp = *head;
    for (; tmp; tmp = tmp->next)
    { 
        s++;
    }

    tmp = *head;
    for (i = 0; i < (s / 2) - 1; i++)
    {
        tmp = tmp->next;
    }

    if ((s % 2) == 0 && tmp->n != tmp->next->n)
    {
        return (0);
    }

    tmp = tmp->next->next;
    rev = reverse_listint(&tmp);
    mid = rev;

    tmp = *head;
    for (; rev; tmp = tmp->next, rev = rev->next)
    { 
        if (tmp->n != rev->n)
            return (0);
    }
    reverse_listint(&mid);

    return (1);
}
