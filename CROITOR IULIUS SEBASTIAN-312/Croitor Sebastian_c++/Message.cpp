//
// Created by Next on 5/20/2022.
//

#include "Message.h"
#include <cstring>
#include <iostream>
Message::Message() {
    sender = "";
   reciever = "";
    message = "";
}

Message::Message(string s, string r, string msg) {
    this->sender = s;
    this->reciever = r;
    this->message = msg;
}
string &Message::get_message(){
    return this->message;
}

void Message::set_message(string message) {
    this->message = message;
}

string &Message::get_sender(){
    return sender;
}

void Message::set_sender(string sender) {
    this->sender = sender;
}
string &Message::get_reciver() {
    return this->reciever;
}
void Message::set_reciver(string reciver) {
    this->reciever = reciver;
}
bool Message::operator==(const Message &a) {
    return ((this->message == a.message) && (this->reciever == a.reciever) && (this->sender == a.sender));
}

Message &Message::operator=(const Message &a) {
    if (this != &a) {
        this->message = a.message;
        this->sender = a.sender;
        this->reciever = a.reciever;
    }
}
Message::~Message() {
}

ostream &operator<<(ostream &os, const Message &A){
    os<<"Message: "<< A.message<<endl;
    os<<"Sender: "<<A.sender<<endl;
    os<<"Reciver: "<<A.reciever<<endl;
};