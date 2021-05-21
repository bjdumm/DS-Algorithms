#include <stdio.h>
#include <stdlib.h>


typedef struct node {
  int data;
  struct node* next;
} Node;

void printList(Node* node){
  while(node != NULL){
    printf(node->data);
    node = node->next;
  }
}



int main(){
  Node* n1;
  Node* n2;
  Node* n3;
  Node* n4;

  n1 = (Node*)malloc(sizeof(Node));
  n2 = (Node*)malloc(sizeof(Node));
  n3 = (Node*)malloc(sizeof(Node));
  n4 = (Node*)malloc(sizeof(Node));

  n1->data = 1; n2->data = 2; n3->data = 3; n4->data =4;
  n1->next = n2; n2->next = n3; n3->next = n4;
  
  printList(n1);
  
  return 0;
}
