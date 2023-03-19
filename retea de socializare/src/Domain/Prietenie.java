package Domain;

import java.util.Objects;

public class Prietenie extends Entity<String> {

    private final Long ID1, ID2;

    public Prietenie(Long ID1, Long ID2) {
        super((ID1 < ID2) ? String.valueOf(ID1) + "_" + String.valueOf(ID2) : String.valueOf(ID2) + "_" + String.valueOf(ID1));
        this.ID1 = ID1;
        this.ID2 = ID2;

    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        return Objects.equals(this.getID(), ((Prietenie) o).getID());
    }

    public Long getID1() {
        return ID1;
    }

    public Long getID2() {
        return ID2;
    }

    public int hashCode() {
        return Objects.hash(ID1, ID2);
    }


}
