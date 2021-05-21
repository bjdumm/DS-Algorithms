#include <iostream>

class Node{
  public:
    int data;
    Node* next = NULL;
};

class LinkedList{
  public:
    LinkedList(Node* head):
    Node* head = NULL;
};


void main{
  Node* n1 = new Node();
  Node* n2 = new Node();
  Node* n3 = new Node();
  
  n1->data = 1;
  n2->data = 2;
  n3->data = 3;
  
  n1->next = n2;
  n2->next = n3;
  
  LinkedList::printList(n1);
}
