#include "lists.h"

/**
 * check_cycle - main function
 * @list: arg
 * Return: int true or false
 */

int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
	{
		return(0);
	}

	while (s && f && f->next)
	{
		s = s->next;
		f = fast->next->next;
		if (s == f)
		{
			return (1);
		}
	}

	return (0);
}
