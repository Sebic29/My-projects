//
// Created by Next on 5/21/2022.
//

#ifndef PROIECT_SDA_REPOSITORYUSER_H
#define PROIECT_SDA_REPOSITORYUSER_H
#include "User.h"

class RepositoryUser {
private:
    User* v;
    int capacitate;
    int lungime;
public:
    RepositoryUser();
    void adaugare(const User&);
    void stergere(const User&);
    void update(const User&entiate1 , const User&entitate2);
    int size() const;
    int find(const User&);
    User* get_all();
};


#endif //PROIECT_SDA_REPOSITORYUSER_H
