#include <iostream>

struct Node {
    Node* n;
    int data = 0;
};


class LinkedList{
    public:
        void addNode(int data) {

            std::cout << "You added " << data << " to the list.";
        }

    private:
        Node* head;
};