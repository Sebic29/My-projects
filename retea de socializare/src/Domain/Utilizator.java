package Domain;

public class Utilizator extends Entity<Long> {

    private String nume;

    private String prenume;

    private String email;

    private String parola;

    private String dataNasterii;


    public Utilizator(Long id, String nume, String prenume, String email, String parola, String dataNasterii) {
        super(id);
        this.nume = nume;
        this.prenume = prenume;
        this.email = email;
        this.parola = parola;
        this.dataNasterii = dataNasterii;
    }
    public String getNume()
    {
        return this.nume;
    }

    public String getPrenume(){return this.prenume;}

    public String getEmail()
    {
        return this.email;
    }

    public String  getDataNastere()
    {
        return this.dataNasterii;
    }

    public String getParola()
    {
        return this.parola;
    }

    public String toString()
    {
        return getID()+" "+nume+" "+prenume+" "+email+" "+dataNasterii;
    }

}
