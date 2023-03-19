//
// Created by Next on 5/21/2022.
//

#include "UserInterface.h"
#include <iostream>
#include <cstring>
#include "Exceptions.h"
using namespace std;
void UI::show_menu() {
    cout<<"Add user(AU)"<<endl<< "Add friend(AF) " << endl << "Send message(AM)" <<endl;
    cout<<"----------------"<<endl;
    cout<<"Delete user(DU)"<<endl << "Delete friend(DF) " << endl << "Delete message(DM)"  << endl;
    cout<<"----------------"<<endl;
    cout<<"Show users(SU)"<<endl << "Show friends(SF) " << endl << "Show message(SM)"  << endl<<endl;
}

void UI::run_menu() {
    char optiune[100];
    show_menu();
    cout<<"Introduceti optiunea: " << endl;
    cin >> optiune;
    while (strcmp(optiune, "0") != 0)
    {
        if (strcmp(optiune, "AF") == 0)
            adaugare_friends();
        if (strcmp(optiune, "AM") == 0)
            adaugare_mesaj();
        if (strcmp(optiune, "AU") == 0)
            adaugare_user();
        if (strcmp(optiune, "DF") == 0)
            stergere_friends();
        if (strcmp(optiune, "DM") == 0)
            stergere_mesaj();
        if (strcmp(optiune, "DU") == 0)
            stergere_user();
        if  (strcmp(optiune, "SU") == 0)
            show_all_user();
        if  (strcmp(optiune, "SF") == 0)
            show_all_friends();
        if  (strcmp(optiune, "SM") == 0)
            show_all_messages();
        show_menu();
        cout << "Introduceti optiunea: " <<  endl;
        cin >> optiune;
    }
}
UI::UI(const ServiceFriends &fr, const ServiceMessage &msg, const ServiceUser &us){
    this->service_friends = fr;
    this->service_message = msg;
    this->service_user = us;
}
void UI::adaugare_user(){
    cout<<endl;
    User u;
    int varsta,id;
    string nume;
    string oras;
    cout<<"Dati id-ul user-ului: "<<endl;
    cin>>id;
    cout<<"Dati numele "<<endl;
    cin>>nume;
    cout<<"Dati orasul: "<<endl;
    cin>>oras;
    cin.get();
    cout<<"Dati varsta: "<<endl;
    cin>>varsta;
    int ok = 1;
    User* all = service_user.get_all();
    for(int i = 0;i<service_user.get_length();i++)
        if(all[i].get_id() == id)
            ok = 0;
    if(ok == 0)
        cout<<"Exista un user cu id ul introdus:"<<endl;
        else
    {u.set_id(id);
    u.set_varsta(varsta);
    u.set_nume(nume);
    u.set_oras(oras);
    //u.useri.add(u);
    service_user.add(u);
    }


}
void UI::adaugare_friends() {
   cout<<endl; int ok = 0 ,  ok2 = 0;
   Friend f;
   User* all = service_user.get_all();
   string nume1,nume2;
   cout<<"Dati primul user: " << endl;
   cin>>nume1;
   cout<<"Dati al doilea user: " << endl;
   cin>>nume2;
   for(int i = 0;i<service_user.get_length();i++)
        if(all[i].get_nume() == nume1)
            ok = 1;
    for(int i = 0;i<service_user.get_length();i++)
        if(all[i].get_nume() == nume2)
            ok2 = 1;
   if((ok == 0 && ok2 == 0) or( ok == 1 && ok2==0) or(ok==0 && ok2 ==1))
       cout << "Nu exista userii introdusi!"<<endl;
   else if (ok == 1 && ok2 == 1) {
           f.set_nume1(nume1);
           f.set_nume2(nume2);
           //f.prietenii.add(f);
           service_friends.add(f);
       }

}

void UI::adaugare_mesaj() {
    cout<<endl;
    Message msg; int ok1 = 0;
    string sender,reciver,message;
    Friend* all = service_friends.get_all();
    cout<< "Dati sender ul: " << endl;
    cin>>sender;
    cout<<"Dati reciver ul: " <<endl;
    cin>>reciver;
    cout<<"Dati mesajul: " << endl;
    //cin>>message;
    char s[40];
    cin.get();
    cin.getline(s,40);
    message = (string)s;
    for(int i = 0;i<service_friends.get_length();i++)
        if((all[i].get_nume1() == sender && all[i].get_nume2() == reciver) or(all[i].get_nume1() == reciver && all[i].get_nume2() == sender))
            ok1 = 1;
    if (ok1 == 0)
        cout << "Nu exista sender ul/reciver ul introdus"<<endl ;
    else {
        msg.set_reciver(reciver);
        msg.set_sender(sender);
        msg.set_message(message);
        //msg.mesaje.add(msg);
        service_message.add(msg);
    }

}

void UI::stergere_user() {
    int id; User u;
    cout<<"Dati id ul user ului pe care vreti sa il stergeti: "<<endl;
    cin>>id;
    int ok = 0;
    User* all = service_user.get_all();
    for(int i = 0;i<service_user.get_length();i++)
        if(all[i].get_id() == id)
            ok = 1;
    if(ok == 0)
        cout<<"Nu exista user ul pe care doriti sa il stergeti:"<<endl;
    else {
        u = this->service_user.get_user(id);
        //u.useri.remove(u);
        //u.useri.remove(u);
        this->service_user.del(u);
    }


}

void UI::stergere_friends() {
    Friend f , g;
    Friend* all = service_friends.get_all();
    string nume1,nume2;
    int ok1 = 0 , ok2 = 0;
    cout<<endl;
    cout<<"Dati primul nume: "<<endl;
    cin>>nume1;
    cout<<"Dati al doilea nume: "<<endl;
    cin>>nume2;
    for(int i = 0;i<service_friends.get_length();i++)
        if((all[i].get_nume1() == nume1 && all[i].get_nume2() == nume2))
        {
            f = all[i];
            ok1 = 1;
        }
    for(int i = 0;i<service_friends.get_length();i++)
        if((all[i].get_nume1() == nume2 && all[i].get_nume2() == nume1))
        {
            g = all[i];
            ok2 = 1;
        }
    if (ok1==1 && ok2==1)
    {
        this->service_friends.del(f);
        this->service_friends.del(g);
    }
    else if(ok1 == 1 && ok2 == 0)
            this->service_friends.del(f);
    else if (ok1 == 0 && ok2 ==1)
    {
        this->service_friends.del(g);
    }
    else if(ok1 == 0 && ok2 ==0)
        cout<<"Prietenia introdusa nu exista! "<<endl;

}

void UI::stergere_mesaj() {
    Message mesaj; int ok = 0;
    cout<<"Dati mesajul care va fi sters: "<<endl;
    string sender,reciver,message;
    char s[40];
    cin.get();
    cin.getline(s,40);
    message = (string)s;
    cout<< "Dati sender ul: " << endl;
    cin>>sender;
    cout<<"Dati reciver ul: " <<endl;
    cin>>reciver;
    Message* all = service_message.get_all();
    for(int i = 0;i<service_message.get_length();i++)
        if(all[i].get_sender() == sender && all[i].get_reciver() == reciver && all[i].get_message() == message)
        {
            mesaj = all[i];
            ok = 1;
        }
    if (ok!=1)
        cout<<"Nu exista mesajul introdus dintre cei doi prieteni: ";
    else
        this->service_message.del(mesaj);
}

void UI::show_all_user(){
    User* all = service_user.get_all();
    for(int i = 0;i<service_user.get_length();i++)
        cout<<all[i]<<endl;
    cout<<endl;
}
void UI::show_all_friends(){
    Friend* all = service_friends.get_all();
    for(int i = 0;i<service_friends.get_length();i++)
        cout<<all[i]<<endl;
    cout<<endl;
}

void UI::show_all_messages(){
    Message* all= service_message.get_all();
    for(int i = 0;i<service_message.get_length();i++)
        cout<<all[i]<<endl;
    cout<<endl;
}