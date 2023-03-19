//
// Created by Next on 5/21/2022.
//

#include "Friends.h"
#include "User.h"

Friend::Friend() {
    this->nume1 = " ";
    this->nume2 = " ";
}
string Friend::get_nume1() {
    return this->nume1;
}
string Friend::get_nume2() {
    return this->nume2;
}
void Friend::set_nume1(string nume1) {
    this->nume1 = nume1;
}
void Friend::set_nume2(string nume2) {
    this->nume2 = nume2;
}
Friend::Friend(string nume1,string nume2) {
    this->nume1 = nume1;
    this->nume2 = nume2;
}
Friend::Friend(const Friend &S) {
    this->nume1 = S.nume1;
    this->nume2 = S.nume2;
}

Friend &Friend::operator=(const Friend &a) {
        if(this != &a) {
            this->nume1 = a.nume1;
            this->nume2 = a.nume2;
        }
        return *this;
    }
bool Friend::operator==(const Friend &a) {
    return ((this->nume1 == a.nume1) && (this->nume2 == a.nume2));
}

ostream &operator<<(ostream &os, const Friend &A){
    os<<"Prieten 1:"<<A.nume1<<endl;
    os<<"Prieten 2:"<<A.nume2<<endl;
};