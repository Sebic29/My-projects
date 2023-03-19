package Service;

import Domain.Prietenie;
import Domain.Utilizator;
import Domain.validators.ValidationExceptions;
import Repository.Repository;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class Service {
    Repository<Long, Utilizator> repoUtilizator;

    Repository<String, Prietenie> repoPrietenie;

    public Service(Repository<Long, Utilizator> repoUtilizator, Repository<String, Prietenie> repoPrietenie){
        this.repoUtilizator = repoUtilizator;
        this.repoPrietenie = repoPrietenie;
    }
    public boolean addUser(Long ID, String nume, String prenume, String email, String parola, String dataNasterii){
        Utilizator user = new Utilizator(ID, nume, prenume, email, parola, dataNasterii);
        try {
            repoUtilizator.save(user);
            return true;
        }
        catch (ValidationExceptions e) {
            System.out.println(e.getMessage());
            return false;
        }
    }
    public boolean updateUser(Long ID, String nume, String prenume, String email, String parola, String dataNasterii){
        Utilizator user = new Utilizator(ID, nume, prenume, email, parola, dataNasterii);
        try {
            return repoUtilizator.update(user) == null;
        }
        catch (ValidationExceptions e) {
            System.out.println(e.getMessage());
            return false;
        }
    }
    public Utilizator findUser(Long ID){

        return repoUtilizator.findOne(ID);
    }
    public boolean addFriendship(Long ID1, Long ID2){
        Utilizator u1 = repoUtilizator.findOne(ID1);
        Utilizator u2 = repoUtilizator.findOne(ID2);

        if (u1 == null || u2 == null) {
            throw new Error("Utilizator inexistent!");
        }
        Prietenie friendship = new Prietenie(ID1, ID2);
        try {
            repoPrietenie.save(friendship);
            return true;
        }
        catch (ValidationExceptions e) {
            System.out.println(e.getMessage());
            return false;
        }
    }
    public boolean deleteUser(Long ID){

        return repoUtilizator.delete(ID) != null;
    }
    public boolean deleteFriendship(String ID){

        return repoPrietenie.delete(ID) != null;
    }
    public Iterable<Utilizator> getAll(){
        return repoUtilizator.findAll();
    }

    public Iterable<Prietenie> getAllPrietenii(){
        return repoPrietenie.findAll();
    }

    public List<Utilizator> getListUtilizatori(){
        Iterable<Utilizator> utilizatorIterable = repoUtilizator.findAll();
        List<Utilizator> listaUtilizator = new ArrayList<>();
        utilizatorIterable.forEach(listaUtilizator::add);
        return listaUtilizator;
    }

    public List<Prietenie> getListPrietenie(){
        Iterable<Prietenie> prietenieIterable = repoPrietenie.findAll();
        List<Prietenie> listaPrietenie = new ArrayList<>();
        prietenieIterable.forEach(listaPrietenie::add);
        return listaPrietenie;
    }
    public int getNrUtilizatori(){

        return repoUtilizator.getSize();
    }
}
