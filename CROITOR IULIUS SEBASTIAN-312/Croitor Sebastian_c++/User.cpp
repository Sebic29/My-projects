//
// Created by Next on 5/20/2022.
//

#include "User.h"

User::User() {
    this->varsta = 0;
    this->nume = "";
    this->oras = "";
    this->id = 0;
}
User::~User() {}
void User::set_id(int id2) {
   this->id = id2;
}

int User::get_id() {
    return this->id;
}

void User::set_varsta(int v) {
    this->varsta = v;
}

int User::get_varsta() {
    return this->varsta;
}

void User::set_nume(string nume) {
    this->nume = nume;
}

string User::get_nume() {
    return this->nume;
}

void User::set_oras(string oras) {
    this->oras = oras;
}

string User::get_oras() {
    return this->oras;
}

bool User::operator==(const User &a) {
    return ((this->varsta == a.varsta) && (this->nume == a.nume) && (this->oras == a.oras));
}

User& User::operator=(const User &a) {
    if(this != &a) {
        this->id = a.id;
        this->varsta = a.varsta;
        this->nume = a.nume;
        this->oras = a.oras;
    }
    return *this;
}
bool User::operator!=(const User &S) {
    return ((this->id != S.id) || (this->varsta!=S.varsta)
            || (this->oras!=S.oras) || (this->nume != S.nume));
}
ostream &operator<<(ostream &os, const User &us){
    os<<"Id: " << us.id<<endl;
    os<<"Varsta: "<<us.varsta<<endl;
    os<<"Nume: "<<us.nume<<endl;
    os<<"Oras: "<<us.oras<<endl;
    return os;
}