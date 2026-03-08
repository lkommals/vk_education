import java.util.List; 

public class User { 
    String name; 
    List<Skill> skills; 
    int experience; 

    public User(String name, List<Skill> skills,int experience) { 
        this.name = name;
        this.skills = skills; 
        this.experience = experience; 
    }

    @Override 
    public String toString() {
        int skillsSize = this.skills.size(); 
        String strSkills = ""; 
        for(int i = 0;i < skillsSize - 1; i+=1) { 
            strSkills += this.skills.get(i);
            strSkills += ',';
        }
        strSkills += this.skills.get(skillsSize - 1);
        return this.name + " " + strSkills + " " + this.experience; 
    }
}