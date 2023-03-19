//
// Created by Next on 5/21/2022.
//

#ifndef PROIECT_SDA_SERVICEFRIENDS_H
#define PROIECT_SDA_SERVICEFRIENDS_H
#include "Friends.h"
#include "RepositoryFriends.h"

class ServiceFriends {
private:
    RepositoryFriends Repo;
public:
    ServiceFriends();
    void add(Friend&);
    void update(Friend &entiate_veche , Friend&entiate_noua);
    void del(Friend&);
    void set_repo(const RepositoryFriends&repo);
    RepositoryFriends& get_Repo();
    Friend* get_all();
    int get_length();

};


#endif //PROIECT_SDA_SERVICEFRIENDS_H
