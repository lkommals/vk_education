package ru.vk.education.job;

import java.util.List;
import java.util.stream.Collectors;

public class User {
    private final String name;
    private final List<Skill> skills;
    private final int experience;

    public User(String name, List<Skill> skills, int experience) {
        this.name = name;
        this.skills = skills;
        this.experience = experience;
    }

    public String getName() {
        return name;
    }

    public List<Skill> getSkills() {
        return skills;
    }

    public int getExperience() {
        return experience;
    }

    @Override
    public String toString() {
        String skillsStr = skills.stream()
                .map(Skill::toString)
                .collect(Collectors.joining(","));
        return name + " " + skillsStr + " " + experience;
    }
}