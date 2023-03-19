//
// Created by Next on 5/22/2022.
//

#ifndef MAIN_CPP_EXCEPTIONS_H
#define MAIN_CPP_EXCEPTIONS_H
#include <exception>

class MyExceptions : public std::exception {
private:
    const char *mesaj;
public:

    MyExceptions(const char *message) : mesaj(message) {}

    const char *what() const noexcept override {
        return mesaj;
    }
};

class DateException : public MyExceptions{
    using MyExceptions::MyExceptions;
};
class CRUDEXCEPTIONS : public MyExceptions{
    using MyExceptions::MyExceptions;
};

#endif  //MAIN_CPP_EXCEPTIONS_H
