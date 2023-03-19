//
// Created by Next on 5/21/2022.
//

#ifndef PROIECT_SDA_REPOSITORYFRIENDS_H
#define PROIECT_SDA_REPOSITORYFRIENDS_H
#include "Friends.h"

class RepositoryFriends {
private:
    Friend *v;
    int lungime;
    int capacitate;
public:
    RepositoryFriends();
    Friend* get_all();
    void adaugare(const Friend&);
    void stergere(const Friend&);
    void update(const Friend&, const Friend&);
    int size() const;
    int find(const Friend &);
};


#endif //PROIECT_SDA_REPOSITORYFRIENDS_H
