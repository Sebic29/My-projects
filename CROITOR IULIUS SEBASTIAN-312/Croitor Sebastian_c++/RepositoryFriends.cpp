//
// Created by Next on 5/21/2022.
//

#include "RepositoryFriends.h"

RepositoryFriends::RepositoryFriends(){
    this->v = new Friend[100];
    this->lungime = 0;
    this->capacitate= 100;
}

int RepositoryFriends::size() const {
    return this->lungime;
}
int RepositoryFriends::find(const Friend &entitate) {
    for (int i = 0; i < this->lungime ; i++)
            if(this->v[i] == entitate)
                return i;
    return -1;
}
void RepositoryFriends::adaugare(const Friend &entitate) {
   this->v[this->lungime] = entitate;
   this->lungime++;
}

void RepositoryFriends::update(const Friend &entitate1, const Friend &entiate2) {
    for (int i = 0; i < this->size() ; ++i)
        if (v[i] == entitate1)
            v[i] = entiate2;

}
void RepositoryFriends::stergere(const Friend &entitate) {
    int pozitie = this->find(entitate);
    for (int i = pozitie; i < this->lungime-1 ; i++)
        this->v[i] = this->v[i+1];
    this->lungime--;

}

Friend *RepositoryFriends::get_all() {
    return this->v;
}