package Repository;

import Domain.Entity;
import Domain.validators.ValidationExceptions;
import Domain.validators.Validator;

import java.util.HashMap;
import java.util.Map;

public class InMemoryRepository <ID, E extends Entity<ID>> implements Repository<ID,E> {
    private final Validator<E> validator;
    protected Map<ID,E> entities;
    public InMemoryRepository(Validator<E> validator){
        this.validator=validator;
        entities=new HashMap<ID,E>();
    }
    @Override
    public E findOne(ID id) {
        if (id==null)
            throw new IllegalArgumentException("ID must be not null");
        return entities.get(id);
    }

    @Override
    public Iterable<E> findAll() {
        return entities.values();
    }

    @Override
    public E save(E entity) throws ValidationExceptions {
        if (entity==null)
            throw new IllegalArgumentException("Entity must be not null");
        validator.validate(entity);
        if(entities.get(entity.getID()) != null) { //daca mai avem un user cu acelasi id
            //return entity;
            throw new ValidationExceptions("ID existent!");
        }
        else entities.put(entity.getID(),entity);
        return null;
    }

    @Override
    public E delete(ID id) {
        if(id == null)
            throw new IllegalArgumentException("ID is null! Cannot delete!");

        if(entities.get(id) != null) {
            return entities.remove(id);
        }
        else return null;
    }

    @Override
    public E update(E entity) throws ValidationExceptions {
        if(entity == null)
            throw new IllegalArgumentException("entitatea nu poate fi null!");
        validator.validate(entity);
        if(entities.get(entity.getID()) != null) {
            entities.put(entity.getID(),entity);
            return null;
        }
        return entity;
    }

    @Override
    public int getSize() {
        return entities.size();
    }
}
