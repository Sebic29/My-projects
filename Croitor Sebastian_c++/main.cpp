#include <iostream>
#include "UserInterface.h"
#include "User.h"
#include "Message.h"
#include "Friends.h"
#include "ServiceUser.h"
#include "ServiceMessage.h"
#include "ServiceFriends.h"
#include "RepositoryUser.h"
#include "RepositoryMessage.h"
#include "RepositoryFriends.h"

using namespace std;
ServiceUser srepo(){
    ServiceUser service_u;
    User u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11,u12,u13,u14,u15;
    u1.set_id(1);
    u2.set_id(2);
    u3.set_id(3);
    u4.set_id(4);
    u5.set_id(5);

    u1.set_varsta(10);
    u2.set_varsta(20);
    u3.set_varsta(30);
    u4.set_varsta(40);
    u5.set_varsta(50);


    u1.set_nume("Bogdan");
    u2.set_nume("Sebi");
    u3.set_nume("Alex");
    u4.set_nume("Gabi");
    u5.set_nume("Daniel");

    u1.set_oras("Suceava");
    u2.set_oras("Cluj");
    u3.set_oras("Bucuresti");
    u4.set_oras("Iasi");
    u5.set_oras("Timisoara");

    service_u.add(u1);
    service_u.add(u2);
    service_u.add(u3);
    service_u.add(u4);
    service_u.add(u5);
    return service_u;
}
ServiceFriends s2repo(){
    ServiceFriends service_f;
    Friend f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,
    f21,f22,f23,f24,f25,f26,f27,f28,f29,f30;
    f1.set_nume1("Bogdan");
    f2.set_nume1("Alex");
    f3.set_nume1("Gabi");
    f4.set_nume1("Daniel");
    f5.set_nume1("Alex");


    f1.set_nume2("Sebi");
    f2.set_nume2("Dani");
    f3.set_nume2("Sebi");
    f4.set_nume2("Alex");
    f5.set_nume2("Bogdan");

    service_f.add(f1);
    service_f.add(f2);
    service_f.add(f3);
    service_f.add(f4);
    service_f.add(f5);
    return service_f;
}
ServiceMessage s3repo(){
    ServiceMessage service_m;
    Message m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16
    ,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30;
    m1.set_sender("Bogdan");
    m2.set_sender("Alex");
    m3.set_sender("Gabi");
    m4.set_sender("Daniel");
    m5.set_sender("Alex");

    m1.set_reciver("Sebi");
    m2.set_reciver("Dani");
    m3.set_reciver("Sebi");
    m4.set_reciver("Alex");
    m5.set_reciver("Bogdan");

    m1.set_message("Salut Sebi");
    m2.set_message("Numele meu este alex");
    m3.set_message("Ma numesc Gabi si sunt din Arad");
    m4.set_message("Am 20 de ani");
    m5.set_message("Salut,de unde esti Bogdan?");

    service_m.add(m1);
    service_m.add(m2);
    service_m.add(m3);
    service_m.add(m4);
    service_m.add(m5);

    return service_m;
}
int main() {

    ServiceFriends service_fr= s2repo();
    ServiceMessage service_msg= s3repo();
    ServiceUser service_us= srepo();
    UI ui( service_fr,service_msg,service_us);
    ui.run_menu();
    return 0;
}
