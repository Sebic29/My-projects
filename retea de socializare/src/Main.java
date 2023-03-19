import Domain.Prietenie;
import Domain.Utilizator;
import Domain.validators.PrietenieValidator;
import Domain.validators.UtilizatorValidator;
import Domain.validators.Validator;
import Repository.Repository;
import Repository.InMemoryRepository;
import Service.Service;
import UI.UI;

public class Main {
    public static void main(String[] args) {
        Validator<Utilizator> validatorUtilizator= new UtilizatorValidator();
        Validator<Prietenie> validatorPrietenie = new PrietenieValidator();

        Repository<Long,Utilizator> repoUser = new InMemoryRepository<>(validatorUtilizator);
        Repository<String,Prietenie> repoPrieten = new InMemoryRepository<>(validatorPrietenie);

        Service service = new Service(repoUser, repoPrieten);

        UI ui = new UI(service);
        ui.start();
    }
}