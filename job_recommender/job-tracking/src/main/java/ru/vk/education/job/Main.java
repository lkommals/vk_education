package ru.vk.education.job;

import java.util.*;
import java.util.stream.Collectors;

public class Main {
    static List<Job> jobs = new ArrayList<>();
    static List<User> users = new ArrayList<>();

    public static void main(String[] args) {
        FileService fileService = new FileService("history.txt");

        List<String> savedCommands = fileService.readCommands();
        for (String cmd : savedCommands) {
            if (cmd.startsWith("user ") || cmd.startsWith("job ")) {
                parseLine(cmd);
            }
        }

        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.isEmpty()) continue;

            if (line.equals("exit")) {
                scanner.close();
                System.exit(0);
            }

            if (line.equals("history")) {
                List<String> commands = fileService.readCommands();
                for (String cmd : commands) {
                    System.out.println(cmd);
                }
                fileService.saveCmd(line);
                continue;
            }

            parseLine(line);
            fileService.saveCmd(line);
        }

        scanner.close();
    }

    private static void parseLine(String line) {
        String[] tokens = line.split(" ");
        String cmd = tokens[0];
        switch (cmd) {
            case "user":
                createUser(tokens);
                break;
            case "user-list":
                userList();
                break;
            case "job":
                createJob(tokens);
                break;
            case "job-list":
                jobList();
                break;
            case "suggest":
                if (tokens.length >= 2) {
                    suggest(tokens[1]);
                }
                break;
            case "stat":
                if (tokens.length >= 2) {
                    processStat(Arrays.copyOfRange(tokens, 1, tokens.length));
                }
                break;
            default:
                break;
        }
    }
    
    private static void processStat(String[] args) {
        if (args.length < 2) return;
        String option = args[0];
        String value = args[1];

        switch (option) {
            case "--exp":
                try {
                    int expThreshold = Integer.parseInt(value);
                    statExp(expThreshold);
                } catch (NumberFormatException e) {
                    System.err.println("Invalid number for --exp");
                }
                break;
            case "--match":
                try {
                    int matchThreshold = Integer.parseInt(value);
                    statMatch(matchThreshold);
                } catch (NumberFormatException e) {
                    System.err.println("Invalid number for --match");
                }
                break;
            case "--top-skills":
                try {
                    int topN = Integer.parseInt(value);
                    statTopSkills(topN);
                } catch (NumberFormatException e) {
                    System.err.println("Invalid number for --top-skills");
                }
                break;
            default:
                break;
        }
    }

    private static void statExp(int minExp) {
        jobs.stream()
                .filter(job -> job.getExperience() >= minExp)
                .sorted(Comparator.comparing(Job::getName))
                .forEach(System.out::println);
    }

    private static void statMatch(int minMatches) {
        users.stream()
                .filter(user -> countMatches(user) >= minMatches)
                .sorted(Comparator.comparing(User::getName))
                .forEach(System.out::println);
    }

    private static void statTopSkills(int topN) {
        if (topN <= 0) return;

        Map<Skill, Long> freq = users.stream()
                .flatMap(user -> user.getSkills().stream())
                .collect(Collectors.groupingBy(skill -> skill, Collectors.counting()));

        List<Skill> topSkills = freq.entrySet().stream()
                .sorted(Map.Entry.<Skill, Long>comparingByValue(Comparator.reverseOrder())
                        .thenComparing(entry -> entry.getKey().getName()))
                .limit(topN)
                .map(Map.Entry::getKey)
                .sorted(Comparator.comparing(Skill::getName))
                .collect(Collectors.toList());

        topSkills.forEach(System.out::println);
    }

    private static long countMatches(User user) {
        return jobs.stream()
                .filter(job -> isMatch(user, job))
                .count();
    }

    private static boolean isMatch(User user, Job job) {
        Set<String> userSkills = user.getSkills().stream()
                .map(Skill::getName)
                .collect(Collectors.toSet());
        Set<String> jobTags = job.getTags().stream()
                .map(Skill::getName)
                .collect(Collectors.toSet());

        long common = userSkills.stream().filter(jobTags::contains).count();
        if (common == 0) return false;

        int score = (int) common;
        if (user.getExperience() < job.getExperience()) {
            score = score / 2;
        }
        return score > 0;
    }

    private static void createUser(String[] tokens) {
        if (tokens.length < 2) return;
        String name = tokens[1];

        if (findUserByName(name) != null) {
            return;
        }

        int experience = 0;
        Set<String> skillsSet = new TreeSet<>();

        for (int i = 2; i < tokens.length; i++) {
            String[] kv = tokens[i].split("=", 2);
            if (kv.length < 2) continue;
            String key = kv[0];
            String value = kv[1];

            if (key.equals("--exp")) {
                try {
                    experience = Integer.parseInt(value);
                } catch (NumberFormatException ignored) {}
            } else if (key.equals("--skills")) {
                if (!value.isEmpty()) {
                    String[] parts = value.split(",");
                    for (String p : parts) {
                        if (!p.isEmpty()) skillsSet.add(p);
                    }
                }
            }
        }

        List<Skill> skills = new ArrayList<>();
        for (String s : skillsSet) skills.add(new Skill(s));

        User newUser = new User(name, skills, experience);
        users.add(newUser);
    }

    private static void createJob(String[] tokens) {
        if (tokens.length < 2) return;
        String title = tokens[1];

        if (findJobByTitle(title) != null) {
            return;
        }

        String company = "";
        int experience = 0;
        Set<String> tagsSet = new TreeSet<>();

        for (int i = 2; i < tokens.length; i++) {
            String[] kv = tokens[i].split("=", 2);
            if (kv.length < 2) continue;
            String key = kv[0];
            String value = kv[1];

            if (key.equals("--company")) {
                company = value;
            } else if (key.equals("--exp")) {
                try {
                    experience = Integer.parseInt(value);
                } catch (NumberFormatException ignored) {}
            } else if (key.equals("--tags")) {
                if (!value.isEmpty()) {
                    String[] parts = value.split(",");
                    for (String p : parts) {
                        if (!p.isEmpty()) tagsSet.add(p);
                    }
                }
            }
        }

        List<Skill> tags = new ArrayList<>();
        for (String t : tagsSet) tags.add(new Skill(t));

        Job newJob = new Job(title, company, tags, experience);
        jobs.add(newJob);
    }

    private static void userList() {
        for (User user : users) {
            System.out.println(user);
        }
    }

    private static void jobList() {
        for (Job job : jobs) {
            System.out.println(job);
        }
    }

    private static void suggest(String username) {
        User user = findUserByName(username);
        if (user == null) return;

        List<JobMatch> matches = new ArrayList<>();

        Set<String> userSkills = new HashSet<>();
        for (Skill s : user.getSkills()) userSkills.add(s.getName());

        for (Job job : jobs) {
            Set<String> jobTags = new HashSet<>();
            for (Skill t : job.getTags()) jobTags.add(t.getName());

            int common = 0;
            for (String us : userSkills) {
                if (jobTags.contains(us)) common++;
            }

            if (common == 0) continue;

            int score = common;
            if (user.getExperience() < job.getExperience()) {
                score = score / 2;
            }

            if (score > 0) {
                matches.add(new JobMatch(job, score));
            }
        }

        matches.sort((a, b) -> Integer.compare(b.getScore(), a.getScore()));

        int limit = Math.min(2, matches.size());
        for (int i = 0; i < limit; i++) {
            System.out.println(matches.get(i).getJob());
        }
    }

    private static User findUserByName(String name) {
        for (User u : users) {
            if (u.getName().equals(name)) return u;
        }
        return null;
    }

    private static Job findJobByTitle(String title) {
        for (Job j : jobs) {
            if (j.getName().equals(title)) return j;
        }
        return null;
    }
}