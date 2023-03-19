//
// Created by Next on 5/20/2022.
//

#ifndef PROIECT_SDA_USER_H
#define PROIECT_SDA_USER_H
#include <string>
#include "List.h"
#include "Multimap.h"
#include "Message.h"
using namespace std;
class User {
private:
    int id;
    int varsta;
    string nume;
    string oras;
public:
    User();
    ~User();
    void set_id(int id);
    void set_varsta(int varsta);
    void set_nume(string nume);
    void set_oras(string oras);

    int get_id();
    int get_varsta();
    string get_nume();
    string get_oras();

    bool operator==(const User&);
    User& operator=(const User& a);
    bool operator!=(const User&);
    List<User> useri;
    //friend istream &operator>>(istream &is, User &);
    friend ostream &operator<<(ostream &os, const User &);
};


#endif //PROIECT_SDA_USER_H
