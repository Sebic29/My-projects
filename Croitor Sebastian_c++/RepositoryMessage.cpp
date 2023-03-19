//
// Created by Next on 5/21/2022.
//

#include "RepositoryMessage.h"
#include "Message.h"
RepositoryMessage::RepositoryMessage(){
    this->v = new Message[50];
    this->lungime = 0;
    this->capacitate = 100;
}
Message* RepositoryMessage::get_all() {
    return this->v;
}
int RepositoryMessage::size() const{
    return this->lungime;
}
int RepositoryMessage::find(const Message &entiate) {
    for (int i = 0; i < this->lungime; i++)
        if(this->v[i] == entiate)
            return i;
    return -1;

}

void RepositoryMessage::adaugare(const Message &entitate) {
    this->v[this->lungime] = entitate;
    this->lungime++;
}

void RepositoryMessage::stergere(const Message &entitate) {
    int pozitie = this->find(entitate);
    for (int i = pozitie; i < this->lungime - 1; i++)
        this->v[i] = this->v[i+1];
    this->lungime--;

}

void RepositoryMessage::update(const Message &entiate1, const Message &entitate2) {
    for (int i = 0; i < this->size() ; i++)
        if (this->v[i] == entiate1)
            this->v[i] = entitate2;

}