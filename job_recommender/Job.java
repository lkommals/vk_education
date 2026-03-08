import java.util.List; 

public class Job {
    String name; 
    String company; 
    List<Skill> tags; 
    int experience; 

    public Job(String name, String company, List<Skill> tags, int experience) { 
        this.name = name; 
        this.company = company; 
        this.tags = tags; 
        this.experience = experience; 
    }

    @Override 
    public String toString() {
        return this.name + " at " + this.company; 
    }
}

