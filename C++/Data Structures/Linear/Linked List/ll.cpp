#include <iostream>

struct  Node {
    int data = 0;
    Node* n;
};


class LinkedList{
    public:
        void addNode(int data) {
	    Node* node = new Node(data);
            std::cout << "You added " << data << " to the list.";
        }



    private:
        Node* head;
};
