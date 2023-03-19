//
// Created by Next on 5/21/2022.
//

#ifndef PROIECT_SDA_REPOSITORYMESSAGE_H
#define PROIECT_SDA_REPOSITORYMESSAGE_H
#include "Message.h"

class RepositoryMessage {
private:
    Message* v;
    int lungime;
    int capacitate;
public:
    RepositoryMessage();
    void adaugare(const Message&);
    void stergere(const Message&);
    void update(const Message&entiate1 , const Message&entitate2);
    int size() const;
    int find(const Message&);
    Message* get_all();
};


#endif //PROIECT_SDA_REPOSITORYMESSAGE_H
