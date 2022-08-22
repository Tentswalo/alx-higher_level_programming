#include "lists.h"

/**
 * check_cycle - checks a singly linked list
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
  listint_t *slow = list;
  listint_t *fast = list;

  if (!list)
    return (0);

  while (slow && fast && fast->next)
    {
      if (slow == fast)
	return (1);
      slow = slow->next;
      fast = fast->next->next;
    }
  return (0);
}
