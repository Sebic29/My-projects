//
// Created by Next on 5/21/2022.
//

#ifndef PROIECT_SDA_FRIENDS_H
#define PROIECT_SDA_FRIENDS_H
#include "User.h"

using namespace std;

class Friend {
private:
    string nume1;
    string nume2;
public:
    Friend();
    Friend(const string nume1,const string nume2);
    Friend(const Friend &);
    Friend &operator=(const Friend &);
    bool operator==(const Friend&);
    string get_nume1();
    void set_nume1(string nume1);
    string get_nume2();
    void set_nume2(string nume2);
    List<Friend> prietenii;
    friend ostream &operator<<(ostream &os, const Friend &);
};


#endif //PROIECT_SDA_FRIENDS_H
