import java.util.Scanner; 
import java.util.*; 

public class Recommender {
    static Job[] jobs; 
    static User[] users; 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); 
        String line = scanner.nextLine(); 
        
        while(!line.equals("exit")) {
            parseLine(line); 
            line = scanner.nextLine(); 
        }


        scanner.close(); 
    }

    private static void parseLine(String line) {
       String[] tags = line.split(" "); 
       if(tags[0].equals("user")) {
        createUser(tags); 
       } else if(tags[0].equals("user-list")) {
        userList(); 
       } else if(tags[0].equals("job")) {
        createJob(tags); 
       } else if(tags[0].equals("job-list")) {
        jobList(); 
       } else if(tags[0].equals("suggest")) {
        suggest(); 
       }
    }

    private static void createUser(String[] tags) {
        System.out.println("Creating new user"); 
    }

    private static void userList() {
        System.out.println("Show list of all users"); 
        for(User user: users) {
            System.out.println(user); 
        }
    }

    private static void createJob(String[] tags) {
        System.out.println("Creating new job"); 
    }

    private static void jobList() {
        System.out.println("output jobs:");
        for(Job job : jobs) {
            System.out.println(job); 
        }
    }

    private static void suggest() {
        System.out.println("suggesting jobs to user");
    }
}