
#ifndef LSI_CURS6_LIST_H
#define LSI_CURS6_LIST_H
#include "vector"

#include "Node.h"
template <class T>
class List {
private:
    Node<T>* head;
public:
    List(){head = nullptr;}
    void add(T elem){
        if (head==nullptr)
        {
            head=new Node<T>(elem);
        }
        else
        {
            Node<T>* p=head;
            while (p->next!=nullptr) p=p->next;
            p->next=new Node<T>(elem);
        }
    }

    T remove(T e){
        Node<T> *nodeToDelete = nullptr;
        T infoToReturn;

        if (head!= nullptr) { // if the list is not empty
            if (head->info == e) {
                nodeToDelete = head;
                head = head->next; //head points to the next node
            } else {
                Node<T> *p= head->next;
                Node <T> *q=head;
                while (p!= nullptr)
                    if (p->info == e) {
                        nodeToDelete = p;
                        p= nullptr;
                    } else {
                        p = p->next;
                        q = q->next;
                    }
                if (nodeToDelete != nullptr)
                    q->next= nodeToDelete->next;
            }
        }
        if (nodeToDelete != nullptr) { // if the elem e was found
            infoToReturn = nodeToDelete->info;
            delete nodeToDelete;
            return infoToReturn;
        }
        return T(); // e does not exist in the list or the list is empty
    }
    void update(T old_element, T new_element) {
        if (head != nullptr) {
            if (head->info == old_element) {
                head->info = new_element;
            } else {
                Node<T> *p = head->next;
                while (p != nullptr)
                    if (p->info == old_element) {
                        p->info = new_element;
                        p = p->next;
                    } else {
                        p = p->next;
                    }
            }
        }
    }
    std::vector<T> get_all() {
        Node<T> *temp = head;
        std::vector<T> all;
        while (temp) {
            all.push_back(temp->info);
            temp = temp->next;
        }
        return all;
    }
    T search(){}
    T get(int index){}
    T operator[](int index){}

};


#endif //LSI_CURS6_LIST_H
