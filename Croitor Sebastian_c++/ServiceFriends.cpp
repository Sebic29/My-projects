//
// Created by Next on 5/21/2022.
//

#include "ServiceFriends.h"

ServiceFriends::ServiceFriends() {
    this->Repo;
}

void ServiceFriends::add(Friend &entitate) {
    Repo.adaugare(entitate);
}

void ServiceFriends::update(Friend &entiate_veche, Friend &entiate_noua) {
    Repo.update(entiate_veche, entiate_noua);
}

void ServiceFriends::del(Friend &entitate) {
    Repo.stergere(entitate);
}

void ServiceFriends::set_repo(const RepositoryFriends &repo) {
    this->Repo = repo;
}

RepositoryFriends &ServiceFriends::get_Repo() {
    return this->Repo;
}

Friend *ServiceFriends::get_all() {
    return this->Repo.get_all();
}

int ServiceFriends::get_length() {
    return this->Repo.size();
}