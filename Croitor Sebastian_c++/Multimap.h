#ifndef CURS8_MULTIMAP_H
#define CURS8_MULTIMAP_H
#include <iostream>
#include <vector>
using namespace std;
template <class Key, class Value>
class Multimap {
private:
    template <class K, class V>
    class MapNode {
    public:
        K key;
        V value;
        MapNode<K,V>* next;
        MapNode(K key, V value) : key(key), value(value){ this->next= nullptr;}
    };
    template<class V>
    class ListNode {
    public:
        V info;
        ListNode<V> *next;
        ListNode(V info, ListNode<V> *next) : info(info), next(next) {}
        ListNode(V info) : info(info) { next = nullptr; }
    };
    int size;
    MapNode<Key,ListNode<Value>*>* first;

    MapNode<Key, ListNode<Value>*>* searchAdress(Key k){
        if(this->size == 0) return nullptr;
        MapNode<Key, ListNode<Value>*>* p = first;
        while(p->next != nullptr){
            if(p->key == k) return p;
            p = p->next;
        }
        return p;
    }


public:
    Multimap(){
        this->first = nullptr;
        this->size = 0;
    }
    void put(Key key, Value value){
        MapNode<Key, ListNode<Value>*>* poz = searchAdress(key);

        if(poz == nullptr){
//            MapNode<Key, ListNode<Value>*>* node = new MapNode<Key, ListNode<Value>*>(key, nullptr);
//            ListNode<Value>* listnode = new ListNode<Value>(value);
//            this->first = node;
//            this->first->value = listnode;
//            this->size++;
//              sau:
            this->first = new MapNode<Key, ListNode<Value>*>(key, new ListNode<Value>(value));
            this->size++;
        }else{
            if(poz->key == key){  //cazul:exista in disctionar o pereche cu cheia egala cu key
                ListNode<Value>* node = new ListNode<Value>(value, poz->value);
                poz->value = node;
            }else{
                poz->next = new MapNode<Key, ListNode<Value>*>(key, new ListNode<Value>(value));
                this->size++;
            }
        }
    }

    vector<Value> remove(Key key){
        MapNode<Key, ListNode<Value>*>* poz = searchAdress(key);
        vector<Value> result;

        if(poz != nullptr && poz->key == key){
            MapNode<Key, ListNode<Value>*>* p = first;
            if(poz == first) this->first = poz->next;
            else {
                while(p->next != poz) p = p->next;
                p->next = poz->next;
            };
            while(poz->value != nullptr){
                ListNode<Value>* node = poz->value;
                result.push_back(node->info);
                poz->value = node->next;
                delete node;
            }
            this->size--;
            delete poz;
        }
        return result;
    }

    void remove(Key key, Value value){

    }

};


#endif
