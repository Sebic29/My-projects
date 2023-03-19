//
// Created by Next on 5/21/2022.
//

#ifndef PROIECT_SDA_SERVICEMESSAGE_H
#define PROIECT_SDA_SERVICEMESSAGE_H
#include "Message.h"
#include "RepositoryMessage.h"

class ServiceMessage {
private:
    RepositoryMessage Repo;
public:
    ServiceMessage();
    void add(Message&);
    void update(Message &entiate_veche , Message&entiate_noua);
    void del(Message&);
    void set_repo(const RepositoryMessage&repo);
    RepositoryMessage& get_Repo();
    Message* get_all();
    int get_length();
    Message get_mesaj(int id);

};


#endif //PROIECT_SDA_SERVICEMESSAGE_H
