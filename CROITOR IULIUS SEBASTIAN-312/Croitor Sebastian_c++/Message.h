//
// Created by Next on 5/20/2022.
//

#ifndef PROIECT_SDA_MESSAGE_H
#define PROIECT_SDA_MESSAGE_H
#include <string>
#include "List.h"
using namespace std;
class Message {
private:
    string sender;
    string reciever;
    string message;
public:
    Message();
    ~Message();
    Message(string s, string r, string msg);
    string &get_sender();
    void set_sender(string sender);
    string &get_reciver();
    void set_reciver(string reciver);
    string &get_message();
    void set_message(string message);
    Message& operator=(const Message&a);
    bool operator==(const Message&);
    List<Message> mesaje;
    friend ostream &operator<<(ostream &os, const Message &);
};


#endif //PROIECT_SDA_MESSAGE_H
