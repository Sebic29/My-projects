//
// Created by Next on 5/21/2022.
//

#include "RepositoryUser.h"
RepositoryUser::RepositoryUser() {
    this->lungime = 0;
    this->capacitate = 100;
    this->v = new User[capacitate];
}
int RepositoryUser::size()  const {
    return this->lungime;
}
int RepositoryUser::find(const User &entitate) {
    for (int i = 0; i < this->lungime ; i++)
        if(this->v[i] == entitate)
            return i;
    return -1;
}
void RepositoryUser::adaugare(const User &entitate) {
    this->v[this->lungime] = entitate;
    this->lungime++;
}

void RepositoryUser::update(const User &entitate1, const User &entiate2) {
    for (int i = 0; i < this->size() ; ++i)
        if (v[i] == entitate1)
            v[i] = entiate2;

}
void RepositoryUser::stergere(const User &entitate) {
    int i = 0, j = 0;
    User *new_hotel = new User[capacitate];
    while (i < lungime) {
        if (this->v[i] != entitate)
            new_hotel[j++] = v[i];
        i++;
    }
    delete[] this->v;
    this->lungime = j;
    this->v = new_hotel;

}

User *RepositoryUser::get_all() {
    return this->v;
}