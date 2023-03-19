//
// Created by Next on 5/21/2022.
//

#ifndef PROIECT_SDA_SERVICEUSER_H
#define PROIECT_SDA_SERVICEUSER_H
#include "RepositoryUser.h"

class ServiceUser {
private:
    RepositoryUser Repo;
public:
    ServiceUser();
    void add(User&);
    void update(User &entiate_veche , User&entiate_noua);
    void del(User&);
    void set_repo(const RepositoryUser&repo);
    RepositoryUser& get_Repo();
    User* get_all();
    int get_length();
    User get_user(int id);
};


#endif //PROIECT_SDA_SERVICEUSER_H
