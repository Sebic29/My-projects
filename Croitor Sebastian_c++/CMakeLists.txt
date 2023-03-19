cmake_minimum_required(VERSION 3.21)
project(Proiect_sda)

set(CMAKE_CXX_STANDARD 14)

add_executable(Proiect_sda main.cpp Message.cpp Message.h User.cpp User.h Friends.cpp Friends.h RepositoryFriends.cpp RepositoryFriends.h RepositoryMessage.cpp RepositoryMessage.h RepositoryUser.cpp RepositoryUser.h UserInterface.cpp UserInterface.h ServiceFriends.cpp ServiceFriends.h ServiceMessage.cpp ServiceMessage.h ServiceUser.cpp ServiceUser.h Multimap.h List.h Node.h Exceptions.cpp Exceptions.h)
