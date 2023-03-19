//
// Created by Next on 5/21/2022.
//

#include "ServiceUser.h"

ServiceUser::ServiceUser() {
    this->Repo;
}

void ServiceUser::add(User &entitate) {
    Repo.adaugare(entitate);
}

void ServiceUser::update(User &entiate_veche, User &entiate_noua) {
    Repo.update(entiate_veche, entiate_noua);
}

void ServiceUser::del(User &entitate) {
    Repo.stergere(entitate);
}

void ServiceUser::set_repo(const RepositoryUser &repo) {
    this->Repo = repo;
}

RepositoryUser &ServiceUser::get_Repo() {
    return this->Repo;
}

User *ServiceUser::get_all() {
    return this->Repo.get_all();
}

int ServiceUser::get_length() {
    return this->Repo.size();
}
User ServiceUser::get_user(int id) {
    return this->Repo.get_all()[id-1];
}