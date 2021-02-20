#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>

#define MAX_TEMP_NODES 10

struct node {
    int data;
    struct node *next;
};

typedef struct node Node;

Node *list_create_node(int i) {
    Node *node = (Node *)malloc(sizeof(struct node));
    if (node == NULL) {
        printf("Memory allocation error\n");
        exit(1);
    }
    node->data = i;
    node->next = NULL;
    return node;
}

/*
 * Add to the end of the list
 */
void list_add_node_i(Node **head, int i) {

    Node *node = list_create_node(i);
    if (*head == NULL) {
        *head = node;
    } else {
        node->next = *head;
        *head = node;
    }
    return;
}

void list_add_node(Node **head, Node *node) {

    if (*head == NULL) {
        *head = node;
    } else {
        node->next = *head;
        *head = node;
    }
    return;
}

bool list_has_cycle(Node *head) {

    Node *slow, *fast;
    slow = head;
    fast = head;
    while (slow && slow->next) {
        slow = slow->next;
        fast = slow->next->next;
        printf("%p, %p, %p", slow, slow->next, (slow->next)->next);
        printf("slow - %d, fast - %d\n", slow->data, fast->data);
        if (fast == slow) {
            return true;
        }
        sleep(1);
    }
    return false;
}

void list_enumerate(Node *head) {
    printf("List Contents: ");
    int count = 0;

    while(head) {
        printf("%p: %d\n", head, head->data);
        head = head->next;
        count += 1;
        if (count > 3*MAX_TEMP_NODES) {
            printf("\n Nodes exceeding 3 times MAX_TEMP_NODES, may have a cycle\n");
            break;
        }
    }

    printf("Detecting Cycle - %d\n", list_has_cycle(head));
    printf("\n");
    return;
}


int main(int argc, char *argv[])
{
    Node *tnodes[MAX_TEMP_NODES];
    Node *head = tnodes[0];

    for (int i = MAX_TEMP_NODES-1; i >=0 ; i--) {
        tnodes[i] = list_create_node(i);
        list_add_node(&head, tnodes[i]);
    }
    list_enumerate(head);

    for (int i = 0; i < MAX_TEMP_NODES; i++) {
      //  printf("%p, %d\n", tnodes[i], tnodes[i]->data);
    }

    printf("Adding a cycle\n");
    tnodes[MAX_TEMP_NODES-1]->next = tnodes[MAX_TEMP_NODES/2];

    //printf("%d, %d\n", tnodes[MAX_TEMP_NODES-1]->data, tnodes[MAX_TEMP_NODES/2]->data);
    list_enumerate(head);

    for (int i = 0; i < MAX_TEMP_NODES; i++) {
       // printf("%p, nextval:%d, val:%d\n", tnodes[i], tnodes[i]->next->data , tnodes[i]->data);
    }

}
