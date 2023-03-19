//
// Created by Next on 5/21/2022.
//

#include "ServiceMessage.h"


ServiceMessage::ServiceMessage() {
    this->Repo;
}

void ServiceMessage::add(Message &entitate) {
    Repo.adaugare(entitate);
}

void ServiceMessage::update(Message &entiate_veche, Message &entiate_noua) {
    Repo.update(entiate_veche, entiate_noua);
}

void ServiceMessage::del(Message &entitate) {
    Repo.stergere(entitate);
}

void ServiceMessage::set_repo(const RepositoryMessage &repo) {
    this->Repo = repo;
}

RepositoryMessage &ServiceMessage::get_Repo() {
    return this->Repo;
}

Message *ServiceMessage::get_all() {
    return this->Repo.get_all();
}

int ServiceMessage::get_length() {
    return this->Repo.size();
}
Message ServiceMessage::get_mesaj(int id) {
    return this->Repo.get_all()[id];
}