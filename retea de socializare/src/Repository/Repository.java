package Repository;

import Domain.Entity;
import Domain.validators.ValidationExceptions;

public interface Repository<ID, E extends Entity<ID>> {
    /**
     *
     * @param id
     * @return entitatea cu id-ul id
     */
    E findOne(ID id);

    /**
     *
     * @return returneaza toate entitalile
     */
    Iterable<E> findAll();

    /**
     *
     * @param entity
     * @return null daca entitatea a fost adauagata
     *         returneaza entitatea daca deja exista
     */
    E save(E entity) throws ValidationExceptions;

    /**
     *
     * @param id
     * @return entitatea stearsa daca ea exista
     *         null daca nu exista entitatea dorita
     */
    E delete(ID id);

    /**
     *
     * @param entity
     * @return null daca entitatea a fost actualizata
     *         entitatea noua daca nu se poate realiza actualizarea
     */
    E update(E entity) throws ValidationExceptions;

    int getSize();

}
