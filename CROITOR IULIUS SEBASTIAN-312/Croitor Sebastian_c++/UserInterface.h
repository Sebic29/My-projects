//
// Created by Next on 5/21/2022.
//

#ifndef PROIECT_SDA_USERINTERFACE_H
#define PROIECT_SDA_USERINTERFACE_H
#include "ServiceFriends.h"
#include "ServiceMessage.h"
#include "ServiceUser.h"

class UI {
private:
    ServiceFriends service_friends;
    ServiceMessage service_message;
    ServiceUser service_user;

    void adaugare_friends();
    void adaugare_mesaj();
    void adaugare_user();

    void stergere_friends();
    void stergere_mesaj();
    void stergere_user();
    void show_all_user();
    void show_all_friends();
    void show_all_messages();
public:
    UI();
    UI(const ServiceFriends&fr , const ServiceMessage&msg , const ServiceUser&u);
    static void show_menu();
    void run_menu();

};


#endif //PROIECT_SDA_USERINTERFACE_H
